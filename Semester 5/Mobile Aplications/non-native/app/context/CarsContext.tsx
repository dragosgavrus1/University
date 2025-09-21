import { demoCars } from "@/constants/cars";
import { Car } from "@/domain/Car";
import { createContext, ReactNode, useEffect, useState } from "react";
import * as SQLite from "expo-sqlite";
import {
  addCarDb,
  addToSyncQueue,
  deleteCarDb,
  syncPendingOperations,
  updateCarDb,
} from "@/db/SQLRepository";
import { showMessage } from "react-native-flash-message";
import {
  addCarToServer,
  deleteCarFromServer,
  getAllFromServer,
  updateCarOnServer,
} from "@/db/ServerRepository";

export type CarContextProps = {
  cars: Car[];
  addCar: (car: Car) => void;
  updateCar: (car: Car) => void;
  deleteCar: (carId: number) => void;
  getCar: (carId: number) => Car | undefined;
};

export type CarContextProviderType = {
  children: ReactNode;
};

export const CarContext = createContext<CarContextProps | null>(null);

export default function CarContextProvider({
  children,
}: CarContextProviderType) {
  const [cars, setCars] = useState<Car[]>([]);
  const [dbConnection, setDbConnection] = useState<SQLite.SQLiteDatabase>();

  const addCar = async (car: Car) => {
    try {
      const insertedCar = await addCarToServer(car);
      await addCarDb(dbConnection!, insertedCar!, insertedCar?.carId);
      setCars([...cars, insertedCar!]);
    } catch (error) {
      throw new Error("Failed to add car!");
    }
  };

  const updateCar = async (carToUpdate: Car) => {
    try {
      await updateCarDb(dbConnection!, carToUpdate);

      setCars((prevCars) =>
        prevCars.map((car) =>
          car.carId === carToUpdate.carId ? carToUpdate : car
        )
      );

      try {
        await updateCarOnServer(carToUpdate);
      } catch (serverError) {
        console.log("Failed to update on server:", serverError);

        await addToSyncQueue(
          dbConnection!,
          carToUpdate.carId,
          "UPDATE",
          JSON.stringify(carToUpdate)
        );
      }
    } catch (dbError) {
      console.error("Failed to update car locally:", dbError);
      throw new Error("Car update failed.");
    }
  };

  const deleteCar = async (carId: number) => {
    try {
      await deleteCarDb(dbConnection!, carId);

      setCars((prevCars) =>
        prevCars.filter((car) => car.carId !== carId)
      );

      try {
        await deleteCarFromServer(carId);
      } catch (serverError) {
        console.error("Failed to delete on server:", serverError);

        // Add to Sync Queue
        await addToSyncQueue(dbConnection!, carId, "DELETE", "");
      }
    } catch (dbError) {
      console.error("Failed to delete car locally:", dbError);
      throw new Error("Car deletion failed.");
    }
  };

  const getCar = (carId: number) => {
    const car = cars.find((car) => carId == car.carId);

    return car;
  };

  useEffect(() => {
    const connection = SQLite.openDatabaseSync("cars.db");
    setDbConnection(connection);
    createTable(connection);

    async function getAll() {
    try {
      console.log("start fetch cars");
      try {
        await fetchCarsFromServer();
      } catch (error) {
        console.log("fetch from server failed...");
        console.log("fetching from local db");
        await fetchCars(connection);
      }
    } catch (error) {
      console.error(error);

      showMessage({
        message: "Failed to load cars",
        type: "warning",
        duration: 2000,
      });
    }
  }

  getAll();
    const syncInterval = setInterval(() => {
      syncPendingOperations(connection);
    }, 1000); // Sync every 60 seconds

    return () => clearInterval(syncInterval);
  }, []);

  // WebSocket
  useEffect(() => {
    const socket = new WebSocket("ws://192.168.38.94:3001");
    socket.onopen = () => {
      console.log("WebSocket connection established");
    };

    socket.onmessage = async (event) => {
      const { type, payload } = JSON.parse(event.data);

      if (type === "add") {
        const carToAdd = {
          carId: payload.id,
          name: payload.name,
          price: payload.price,
          kilometers: payload.kilometers,
          transmission: payload.transmission,
          fuelType: payload.fuelType,
        };

        await addCarDb(dbConnection!, carToAdd, carToAdd.carId);

        setCars((prevCars) => [...prevCars, carToAdd]);
      } else if (type === "update") {
        const updatedCar = {
          carId: payload.id,
          name: payload.name,
          price: payload.price,
          kilometers: payload.kilometers,
          transmission: payload.transmission,
          fuelType: payload.fuelType,
        };

        await updateCarDb(dbConnection!, payload);
        setCars((prevCars) =>
          prevCars.map((car) =>
            car.carId == updatedCar.carId ? updatedCar : car
          )
        );
      } else if (type === "delete") {
        setCars((prevCars) =>
          prevCars.filter((car) => car.carId != payload.carId)
        );
      }
    };

    socket.onerror = (error) => {
      console.error("WebSocket error:", error);
    };

    socket.onclose = () => {
      console.log("WebSocket connection closed");
    };

    return () => {
      socket.close();
    };
  }, []);

  const createTable = (connection: SQLite.SQLiteDatabase) => {
    connection.execSync(
      "CREATE TABLE IF NOT EXISTS cars(\n\
      id INTEGER PRIMARY KEY AUTOINCREMENT,\n\
      name TEXT not null,\n\
      price REAL not null,\n\
      kilometers REAL not null,\n\
      transmission TEXT not null,\n\
      fuelType TEXT not null);"
    );

    connection.execSync(
      `CREATE TABLE IF NOT EXISTS sync_queue (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        carId INTEGER NOT NULL,
        syncAction TEXT NOT NULL,
        payload TEXT NOT NULL
      );`
    );
  };

  const fetchCars = async (connection: SQLite.SQLiteDatabase) => {
    const allCars = await connection.getAllAsync("SELECT * FROM cars");
    const cars: Car[] = [];

    for (const car of allCars) {
      const carId = (car as any).id;
      const name = (car as any).name;
      const price = (car as any).price;
      const kilometers = (car as any).kilometers;
      const transmission = (car as any).transmission;
      const fuelType = (car as any).fuelType;

      const currentCar: Car = {
        carId: carId,
        name: name,
        price: price,
        kilometers: kilometers,
        transmission: transmission,
        fuelType: fuelType,
      };

      cars.push(currentCar);
    }

    setCars(cars);
  };

  const fetchCarsFromServer = async () => {
    let cars = await getAllFromServer();
    setCars(cars);

    cars.forEach((car: Car) => {
      addCarDb(dbConnection!, car, car.carId);
    });

    console.log("fetched cars from server!");
  };

  return (
    <CarContext.Provider
      value={{
        cars: cars,
        addCar: addCar,
        updateCar: updateCar,
        deleteCar: deleteCar,
        getCar: getCar,
      }}
    >
      {children}
    </CarContext.Provider>
  );
}

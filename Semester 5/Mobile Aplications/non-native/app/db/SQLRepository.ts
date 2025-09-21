import { Car } from "@/domain/Car";
import { SQLiteDatabase } from "expo-sqlite";
import { deleteCarFromServer, updateCarOnServer } from "./ServerRepository";

export async function addCarDb(
  dbConnection: SQLiteDatabase,
  car: Car,
  carId?: number
) {
  if (carId === undefined)
    return dbConnection?.runAsync(
      "INSERT INTO cars(name, price, kilometers, transmission, fuelType) values (?, ?, ?, ?, ?)",
      car.name,
      car.price,
      car.kilometers,
      car.transmission,
      car.fuelType
    );

  return dbConnection?.runAsync(
    "INSERT OR REPLACE INTO cars(id, name, price, kilometers, transmission, fuelType) values (?, ?, ?, ?, ?, ?)",
    carId,
    car.name,
    car.price,
    car.kilometers,
    car.transmission,
    car.fuelType
  );
}

export async function updateCarDb(
  dbConnection: SQLiteDatabase,
  carToUpdate: Car
) {
  return dbConnection?.runAsync(
    "UPDATE cars\
      SET name=?, price=?, kilometers=?, transmission=?, fuelType=? where id=?",
    carToUpdate.name,
    carToUpdate.price,
    carToUpdate.kilometers,
    carToUpdate.transmission,
    carToUpdate.fuelType,
    carToUpdate.carId
  );
}

export async function deleteCarDb(
  dbConnection: SQLiteDatabase,
  carId: number
) {
  return dbConnection?.runAsync("DELETE FROM cars where id = ?", carId);
}

export const addToSyncQueue = async (
  connection: SQLiteDatabase,
  carId: number,
  syncAction: string,
  payload: string
) => {
  await connection.runAsync(
    `INSERT INTO sync_queue (carId, syncAction, payload)
     VALUES (?, ?, ?);`,
    [carId, syncAction, payload]
  );
};

export const getSyncQueue = async (
  connection: SQLiteDatabase
): Promise<{ id: number; carId: number; syncAction: string; payload: string }[]> => {
  const result = await connection.getAllAsync(`SELECT * FROM sync_queue`);
  return result.map((row: any) => ({
    id: row.id,
    carId: row.carId,
    syncAction: row.syncAction,
    payload: row.payload,
  }));
};

export const removeFromSyncQueue = async (
  connection: SQLiteDatabase,
  id: number
) => {
  await connection.runAsync(`DELETE FROM sync_queue WHERE id = ?;`, [id]);
};

export const syncPendingOperations = async (dbConnection: SQLiteDatabase) => {
  try {
    const pendingOperations = await getSyncQueue(dbConnection);

    for (const operation of pendingOperations) {
      const { id, carId, syncAction, payload } = operation;

      try {
        if (syncAction === "UPDATE" && payload) {
          const car = JSON.parse(payload);

          await updateCarOnServer(car);
        } else if (syncAction === "DELETE") {
          await deleteCarFromServer(carId);
        }

        // Remove successfully synced operation from the queue
        await removeFromSyncQueue(dbConnection!, id);
      } catch (syncError) {
        console.error(`Failed to sync operation with id ${id}:`, syncError);
      }
    }
  } catch (error) {
    console.error("Error fetching pending operations from sync_queue:", error);
  }
};

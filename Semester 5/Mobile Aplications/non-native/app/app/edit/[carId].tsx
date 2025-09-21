import { CarContext } from "@/context/CarsContext";
import { useLocalSearchParams } from "expo-router";
import { useContext } from "react";
import AddOrEdit from "../add_or_edit";

export default function Edit() {
  const carContext = useContext(CarContext)!;
  const { carId } = useLocalSearchParams();

  const car = carContext.getCar(Number(carId));

  if (car === undefined) return;

  return <AddOrEdit car={car} />;
}
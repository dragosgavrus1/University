import { Car } from "@/domain/Car";
import CarCard from "./CarCard";
import { FlatList } from "react-native";

interface CarsListProps {
  tasks: Car[];
}

export default function CarsList({ tasks }: CarsListProps) {
  return (
    <FlatList
      style={{ width: "100%", marginTop: 16, paddingTop: 8 }}
      data={tasks}
      renderItem={({ item }) => <CarCard car={item} />}
      keyExtractor={(item) => item.carId.toString()}
      showsVerticalScrollIndicator={false}
    />
  );
}
import { Car } from "@/domain/Car";
import { Alert, Image, Pressable, StyleSheet, Text, View } from "react-native";
import { useContext, useState } from "react";
import { CarContext } from "@/context/CarsContext";
import { useRouter } from "expo-router";

type CarCardProps = {
  car: Car;
};

const maxTextLength = 25;

function getName(car: Car): string {
  return car.name.length > maxTextLength
    ? car.name.slice(0, maxTextLength) + "..."
    : car.name;
}

export default function CarCard({ car }: CarCardProps) {
  const carContext = useContext(CarContext)!;
  const router = useRouter();

  const deleteCar = () => carContext.deleteCar(car.carId);

  const createConfirmDialog = () => {
    Alert.alert(
      "Delete confirmation",
      "Are you sure you want to remove this car?",
      [
        {
          text: "No",
          style: "cancel",
        },

        {
          text: "Yes",
          onPress: deleteCar,
        },
      ]
    );
  };

  return (
    <View style={styles.carCard}>

      <Text style={{ fontSize: 16, flex: 1 }}>{getName(car)}</Text>

      <View style={styles.row}>
        <Pressable
          onPress={() => {
            console.log(car.carId);

            router.navigate(`./edit/${car.carId}`);
          }}
          style={styles.editButton}
        >
          <Text style={styles.buttonText}>Edit</Text>
        </Pressable>

        <Pressable onPress={createConfirmDialog}>
          <Image source={require("../assets/images/trash.png")} />
        </Pressable>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  row: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-between",
    gap: 16,
  },

  carCard: {
    width: "100%",
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-between",
    marginBottom: 16,
  },

  editButton: {
    borderRadius: 12,
    backgroundColor: "#1A73D1",
    paddingHorizontal: 24,
    paddingVertical: 10,
  },

  buttonText: {
    color: "#F7FAFA",
    fontSize: 16,
    fontWeight: "bold",
  },
});
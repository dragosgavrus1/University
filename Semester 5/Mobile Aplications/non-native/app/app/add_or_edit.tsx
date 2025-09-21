import CustomButton from "@/components/CustomButton";
import { primary_text_color, secondary_text_color } from "@/constants/colors";
import { CarContext } from "@/context/CarsContext";
import { useNavigation } from "expo-router";
import { useContext, useState } from "react";
import { Pressable, StyleSheet, Text, TextInput, View, Alert } from "react-native";
import { SafeAreaProvider, SafeAreaView } from "react-native-safe-area-context";
import { Car } from "@/domain/Car";

interface AddOrEditProps {
  car: Car | undefined;
}

export default function AddOrEdit({ car }: AddOrEditProps) {
  const navigation = useNavigation();
  const carsContext = useContext(CarContext)!;

  const [name, setName] = useState<string>(car ? car.name : "");
  const [price, setPrice] = useState<number>(car ? car.price : 0);
  const [kilometers, setKilometers] = useState<number>(car ? car.kilometers : 0);
  const [transmission, setTransmission] = useState<string>(car ? car.transmission : "");
  const [fuelType, setFuelType] = useState<string>(car ? car.fuelType : "");

  const validate = () => {
    const errors: string[] = [];
    if (name.length < 3) {
      errors.push("Car name must be at least 3 characters long.");
    }

    if (price <= 0) {
      errors.push("Price must be greater than 0.");
    }

    if (kilometers < 0) {
      errors.push("Kilometers cannot be negative.");
    }

    if (!transmission) {
      errors.push("Transmission type is required.");
    }

    if (!fuelType) {
      errors.push("Fuel type is required.");
    }

    if (errors.length > 0) {
      Alert.alert("Invalid values!", errors.join("\n"), [{ text: "Ok" }]);
    }

    return errors.length > 0;
  };

  const onSave = () => {
    if (validate()) return;

    const carToAdd: Car = {
      carId: car ? car.carId : 0,
      name,
      price,
      kilometers,
      transmission,
      fuelType,
    };

    car ? carsContext.updateCar(carToAdd) : carsContext.addCar(carToAdd);
    navigation.goBack();
  };

  return (
    <SafeAreaProvider>
      <SafeAreaView style={styles.container}>
        <Text style={styles.title}>{car ? "Edit Car" : "New Car"}</Text>

        <View style={styles.mainContent}>
          <View style={styles.fields}>
            <View>
              <Text style={styles.fieldLabel}>Name</Text>
              <TextInput
                style={styles.input}
                placeholder="Car Name"
                onChangeText={setName}
                value={name}
              />
            </View>

            <View>
              <Text style={styles.fieldLabel}>Price</Text>
              <View style={styles.row}>
                <TextInput
                  style={[styles.input, styles.flexInput]}
                  placeholder="Price"
                  keyboardType="numeric"
                  onChangeText={(text) => setPrice(Number(text))}
                  value={price.toString()}
                />
                <Text style={styles.unitText}>$/day</Text>
              </View>
            </View>

            <View>
              <Text style={styles.fieldLabel}>Kilometers</Text>
              <View style={styles.row}>
                <TextInput
                  style={[styles.input, styles.flexInput]}
                  placeholder="Kilometers"
                  keyboardType="numeric"
                  onChangeText={(text) => setKilometers(Number(text))}
                  value={kilometers.toString()}
                />
                <Text style={styles.unitText}>km</Text>
              </View>
            </View>

            <View>
              <Text style={styles.fieldLabel}>Transmission</Text>
              <TextInput
                style={styles.input}
                placeholder="Transmission (e.g., Automatic, Manual)"
                onChangeText={setTransmission}
                value={transmission}
              />
            </View>

            <View>
              <Text style={styles.fieldLabel}>Fuel Type</Text>
              <TextInput
                style={styles.input}
                placeholder="Fuel Type (e.g., Gasoline, Diesel, Electric)"
                onChangeText={setFuelType}
                value={fuelType}
              />
            </View>
          </View>

          <CustomButton onClick={onSave} text="Save" />
        </View>
      </SafeAreaView>
    </SafeAreaProvider>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    margin: 16,
  },
  title: {
    fontWeight: "bold",
    fontSize: 18,
    marginBottom: 16,
  },
  mainContent: {
    flex: 1,
    justifyContent: "space-between",
    width: "100%",
  },
  fields: {
    marginBottom: 16,
  },
  fieldLabel: {
    marginBottom: 8,
    fontWeight: "bold",
  },
  input: {
    height: 56,
    borderWidth: 1,
    borderRadius: 12,
    backgroundColor: "#E8EDF2",
    borderColor: "transparent",
    width: "100%",
    marginBottom: 16,
    paddingHorizontal: 16,
  },
  row: {
    flexDirection: "row",
    alignItems: "center",
  },
  
  flexInput: {
    flex: 1,
  },
  
  unitText: {
    marginLeft: 8,
    color: "#555",
    fontSize: 16,
  },
});

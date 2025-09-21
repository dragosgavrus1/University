import CustomButton from "@/components/CustomButton";
import CarsList from "@/components/CarsList";
import { CarContext } from "@/context/CarsContext";
import { useNavigation, useRouter } from "expo-router";
import { useContext } from "react";
import { StyleSheet, Text, View } from "react-native";
import { SafeAreaProvider, SafeAreaView } from "react-native-safe-area-context";


export default function Index() {
  const router = useRouter();

  const carContext = useContext(CarContext)!;

  return (
    <SafeAreaProvider>
      <SafeAreaView
        style={{
          paddingBottom: 16,
          flex: 1,
          justifyContent: "space-between",
          alignItems: "center",
          flexDirection: "column",
          margin: 16,
        }}
      >
        <Text
          style={{
            alignContent: "center",
            fontWeight: "bold",
            fontSize: 18,
          }}
        >
          Car Rental
        </Text>

        <CarsList tasks={carContext.cars} />

        <View style={{ marginTop: 16 }}>
          <CustomButton
            onClick={() => router.navigate("/add_or_edit")}
            text="New Car"
          />
        </View>
      </SafeAreaView>
    </SafeAreaProvider>
  );
}

const styles = StyleSheet.create({
  input: {
    marginTop: 16,
    height: 48,
    borderWidth: 1,
    borderRadius: 12,
    backgroundColor: "#E8EDF2",
    borderColor: "transparent",
    width: "100%",
    paddingStart: 16,
  },
  tasks_list: {
    marginTop: 16,
    flex: 1,
  },
});
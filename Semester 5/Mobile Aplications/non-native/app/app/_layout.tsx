import CarContextProvider from "@/context/CarsContext";
import { Stack } from "expo-router";

export default function RootLayout() {
  return (
    <CarContextProvider>
      <Stack>
        <Stack.Screen name="index" options={{ headerShown: false }} />
        <Stack.Screen name="add_or_edit" options={{ headerShown: false }} />
        <Stack.Screen name="edit/[carId]" options={{ headerShown: false }} />
      </Stack>
    </CarContextProvider>
  );
}
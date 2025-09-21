import { Car } from "@/domain/Car";

const BASE_API_URL = 'http://192.168.38.94:3000';

export async function getAllFromServer() {
  try {
    const controller = new AbortController();
    const timeout = 2000;
    const timeoutId = setTimeout(() => controller.abort(), timeout);

    const response = await fetch(BASE_API_URL + '/cars', {signal: controller.signal});
    const cars = await response.json();

    return cars.map((car: any) => ({
      carId: car.id,
      name: car.name,
      price: car.price,
      kilometers: car.kilometers,
      transmission: car.transmission,
      fuelType: car.fuelType,
    }));
  } catch (error: any) {
    console.error('Failed to fetch cars:', error);
    throw new Error();
  }
}

export async function addCarToServer(car: Car) {
  try {
    const response = await fetch(BASE_API_URL + '/cars', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: car.name,
        price: car.price,
        kilometers: car.kilometers,
        transmission: car.transmission,
        fuelType: car.fuelType,
      }),
    });
    const result: any = await response.json();
    console.log('Car added with ID:', result.id);

    return {
      carId: result.id,
      name: result.name,
      price: result.price,
      kilometers: result.kilometers,
      transmission: result.transmission,
      fuelType: result.fuelType,
    };
  } catch (error) {
    console.error('Failed to add car:', error);
    throw new Error();
  }
}

export async function updateCarOnServer(car: Car) {
  try {
    const controller = new AbortController();
    const timeout = 2000;
    const timeoutId = setTimeout(() => controller.abort(), timeout);
    await fetch(`${BASE_API_URL}/cars/${car.carId}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: car.name,
        price: car.price,
        kilometers: car.kilometers,
        transmission: car.transmission,
        fuelType: car.fuelType,
      }), signal: controller.signal
    });
    console.log(`Car ${car.carId} updated`);
  } catch (error) {
    console.error('Failed to update car:', error);
    throw new Error();
  }
}

export async function deleteCarFromServer(carId: number) {
  const controller = new AbortController();
  const timeout = 2000;
  const timeoutId = setTimeout(() => controller.abort(), timeout);

  try {
    await fetch(`${BASE_API_URL}/cars/${carId}`, { method: 'DELETE', signal: controller.signal });
    console.log(`Car ${carId} deleted`);
  } catch (error) {
    console.error('Failed to delete car:', error);
    throw new Error();
  }
}

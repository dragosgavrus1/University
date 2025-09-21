// File: fragments/CarEditFragment.kt
package com.example.carrentalapp.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import androidx.navigation.fragment.navArgs
import com.example.carrentalapp.R
import com.example.carrentalapp.databinding.FragmentCarEditBinding
import com.example.carrentalapp.models.Car
import com.example.carrentalapp.models.CarData

class CarEditFragment : Fragment() {

    private var _binding: FragmentCarEditBinding? = null
    private val binding get() = _binding!!
    private val args: CarEditFragmentArgs by navArgs() // Get the car data from arguments

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentCarEditBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // Load car data from arguments and populate fields
        val car = args.car
        binding.carNameEditText.setText(car.name)
        binding.carPriceEditText.setText(car.price)
        binding.carKilometersEditText.setText(car.kilometers)
        binding.carTransmissionEditText.setText(car.transmission)
        binding.carFuelTypeEditText.setText(car.fuelType)

        // Set up the Update button
        binding.updateButton.setOnClickListener {
            updateCar(car)
        }
        binding.homeButton.setOnClickListener {
            findNavController().navigate(R.id.carListFragment)
        }
    }

    private fun updateCar(car: Car) {
        // Get updated values from input fields
        val updatedName = binding.carNameEditText.text.toString()
        val updatedPrice = binding.carPriceEditText.text.toString()
        val updatedKilometers = binding.carKilometersEditText.text.toString()
        val updatedTransmission = binding.carTransmissionEditText.text.toString()
        val updatedFuelType = binding.carFuelTypeEditText.text.toString()

        // Validate fields
        if (updatedName.isBlank() || updatedPrice.isBlank() || updatedKilometers.isBlank() ||
            updatedTransmission.isBlank() || updatedFuelType.isBlank()) {
            Toast.makeText(requireContext(), "Please fill in all fields", Toast.LENGTH_SHORT).show()
            return
        }

        // Update car details in the in-memory list
        car.name = updatedName
        car.price = updatedPrice
        car.kilometers = updatedKilometers
        car.transmission = updatedTransmission
        car.fuelType = updatedFuelType

        // Update the car in the list
        val index = CarData.cars.indexOfFirst { it.id == car.id }
        if (index != -1) {
            CarData.cars[index] = car
        }

        // Show a message and navigate back
        Toast.makeText(requireContext(), "Car updated successfully!", Toast.LENGTH_SHORT).show()
        findNavController().popBackStack()
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}

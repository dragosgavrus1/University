// File: fragments/CarAddFragment.kt
package com.example.carrentalapp.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import com.example.carrentalapp.R
import com.example.carrentalapp.databinding.FragmentCarAddBinding
import com.example.carrentalapp.models.Car
import com.example.carrentalapp.models.CarData

class CarAddFragment : Fragment() {

    private var _binding: FragmentCarAddBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentCarAddBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // Set up the "Add" button click listener
        binding.addButton.setOnClickListener {
            addCar()
        }
        binding.homeButton.setOnClickListener {
            findNavController().navigate(R.id.carListFragment)
        }
    }

    private fun addCar() {
        // Retrieve values from input fields
        val name = binding.carNameEditText.text.toString()
        val price = binding.carPriceEditText.text.toString()
        val kilometers = binding.carKilometersEditText.text.toString()
        val transmission = binding.carTransmissionEditText.text.toString()
        val fuelType = binding.carFuelTypeEditText.text.toString()

        // Basic validation to ensure required fields are filled
        if (name.isBlank() || price.isBlank() || kilometers.isBlank() || transmission.isBlank() || fuelType.isBlank()) {
            Toast.makeText(requireContext(), "Please fill in all fields", Toast.LENGTH_SHORT).show()
            return
        }

        // Create a new Car object
        val newCar = Car(
            id = (1..1000).random(), // Assign a random ID for simplicity
            name = name,
            price = price,
            kilometers = kilometers,
            transmission = transmission,
            fuelType = fuelType
        )

        // Add the car to the in-memory list
        CarData.cars.add(newCar)

        // Navigate back to the CarListFragment
        findNavController().popBackStack()
        Toast.makeText(requireContext(), "Car added successfully!", Toast.LENGTH_SHORT).show()

    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}

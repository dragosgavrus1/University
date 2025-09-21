// File: CarDetailFragment.kt
package com.example.carrentalapp.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import androidx.fragment.app.Fragment
import androidx.appcompat.app.AlertDialog
import androidx.navigation.fragment.findNavController
import androidx.navigation.fragment.navArgs
import com.example.carrentalapp.R
import com.example.carrentalapp.databinding.FragmentCarDetailBinding
import com.example.carrentalapp.models.Car
import com.example.carrentalapp.models.CarData

class CarDetailFragment : Fragment() {

    private var _binding: FragmentCarDetailBinding? = null
    private val binding get() = _binding!!

    private val args: CarDetailFragmentArgs by navArgs()

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentCarDetailBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // Retrieve car data from arguments
        val car = args.car

        // Set data to views
        binding.carNameTextView.text = car.name
        binding.priceTextView.text = "$${car.price}/day"
        binding.kilometersTextView.text = "${car.kilometers} km"
        binding.transmissionTextView.text = car.transmission
        binding.fuelTypeTextView.text = car.fuelType

        // Set up edit button click listener to navigate to CarEditFragment
        binding.editButton.setOnClickListener {
            val action = CarDetailFragmentDirections.actionCarDetailFragmentToCarEditFragment(car)
            findNavController().navigate(action)
        }

        binding.deleteButton.setOnClickListener {
            showDeleteConfirmationDialog(car)
        }

        binding.homeButton.setOnClickListener {
            findNavController().navigate(R.id.carListFragment)
        }
    }

    private fun showDeleteConfirmationDialog(car: Car) {
        AlertDialog.Builder(requireContext())
            .setTitle("Delete Car")
            .setMessage("Are you sure you want to delete ${car.name}?")
            .setPositiveButton("Yes") { _, _ ->
                deleteCar(car)
            }
            .setNegativeButton("No", null)
            .show()
    }

    private fun deleteCar(car: Car) {
        // Remove the car from CarData
        CarData.cars.remove(car)

        // Show a Toast confirmation message
        Toast.makeText(requireContext(), "${car.name} has been deleted.", Toast.LENGTH_SHORT).show()

        // Navigate back to the CarListFragment
        findNavController().popBackStack()
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}

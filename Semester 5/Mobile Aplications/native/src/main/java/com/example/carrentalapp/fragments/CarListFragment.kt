// File: fragments/CarListFragment.kt
package com.example.carrentalapp.fragments

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.navigation.fragment.findNavController
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.carrentalapp.R
import com.example.carrentalapp.adapters.CarListAdapter
import com.example.carrentalapp.databinding.FragmentCarListBinding
import com.example.carrentalapp.models.Car
import com.example.carrentalapp.models.CarData

class CarListFragment : Fragment() {

    private var _binding: FragmentCarListBinding? = null
    private val binding get() = _binding!!

    private val carList = listOf(
        Car(1, "Maserati 867", "$540/day", "45k km", "Automatic", "Petrol"),
        Car(2, "Jaguar F Pace", "$400/day", "60k km", "Automatic", "Diesel"),
        Car(3, "Range Rover Evoque", "$350/day", "100k km", "Automatic", "Petrol")
    )
    private lateinit var carListAdapter: CarListAdapter

    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentCarListBinding.inflate(inflater, container, false)
        return binding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        binding.carRecyclerView.layoutManager = LinearLayoutManager(context)
        carListAdapter = CarListAdapter(CarData.cars) { car ->
            val action = CarListFragmentDirections.actionCarListFragmentToCarDetailFragment(car)
            findNavController().navigate(action)
        }
        binding.carRecyclerView.adapter = carListAdapter

        binding.addCarButton.setOnClickListener {
            // Navigate to Add Car Fragment
            val action = CarListFragmentDirections.actionCarListFragmentToCarAddFragment()
            findNavController().navigate(action)
        }
        binding.homeButton.setOnClickListener {
            findNavController().navigate(R.id.carListFragment)
        }
    }

    override fun onResume() {
        super.onResume()
        carListAdapter.notifyDataSetChanged() // This will refresh the RecyclerView
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}

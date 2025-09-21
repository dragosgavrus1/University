// File: adapters/CarListAdapter.kt
package com.example.carrentalapp.adapters

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.example.carrentalapp.databinding.ItemCarBinding
import com.example.carrentalapp.models.Car

class CarListAdapter(
    private val cars: List<Car>,
    private val onItemClick: (Car) -> Unit
) : RecyclerView.Adapter<CarListAdapter.CarViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CarViewHolder {
        val binding = ItemCarBinding.inflate(LayoutInflater.from(parent.context), parent, false)
        return CarViewHolder(binding)
    }

    override fun onBindViewHolder(holder: CarViewHolder, position: Int) {
        holder.bind(cars[position])
    }

    override fun getItemCount(): Int = cars.size

    inner class CarViewHolder(private val binding: ItemCarBinding) : RecyclerView.ViewHolder(binding.root) {
        fun bind(car: Car) {
            binding.apply {
                carName.text = car.name
                carPrice.text = "$${car.price}/day"
                root.setOnClickListener { onItemClick(car) }
            }
        }
    }
}

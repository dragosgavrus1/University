package com.example.carrentalapp.models

import android.os.Parcelable
import kotlinx.parcelize.Parcelize

@Parcelize
data class Car(
    val id: Int,
    var name: String,
    var price: String,
    var kilometers: String,
    var transmission: String,
    var fuelType: String
) : Parcelable
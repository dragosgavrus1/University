// File: MainActivity.kt
package com.example.carrentalapp

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.carrentalapp.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Set the layout using view binding
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
    }
}

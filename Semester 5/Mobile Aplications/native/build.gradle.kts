// Top-level build file where you can add configuration options common to all sub-projects/modules.
plugins {
    alias(libs.plugins.android.application) apply false
    alias(libs.plugins.kotlin.android) apply false
    alias(libs.plugins.kotlin.compose) apply false
}
buildscript {
    dependencies {
        // Add this Safe Args classpath
        classpath(libs.androidx.navigation.safe.args.gradle.plugin) // Latest stable version
    }
}
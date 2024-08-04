<?php

    function get_all_flights($city, $date){
        require "config.php";
        $entities = array();

        $sql = "SELECT * FROM flights WHERE date = ? and destinationCity = ? and availableSeats > 0";
        $select_stmt = mysqli_stmt_init($conn);

        if(mysqli_stmt_prepare($select_stmt, $sql)) {
            mysqli_stmt_bind_param($select_stmt, "ss", $date, $city);
            mysqli_stmt_execute($select_stmt);
            $results = mysqli_stmt_get_result($select_stmt);
    
            while ($row = mysqli_fetch_assoc($results)) {
                array_push($entities, $row);
            }
        }

        return $entities;

    }

    function get_all_hotels($city, $date) {
        require "config.php";

        $sql = "SELECT * FROM hotels WHERE date = ? and city = ? and availableRooms > 0";
        $select_stmt = mysqli_stmt_init($conn);

        if(mysqli_stmt_prepare($select_stmt, $sql)) {
            mysqli_stmt_bind_param($select_stmt, "ss", $date, $city);
            mysqli_stmt_execute($select_stmt);
            $results = mysqli_stmt_get_result($select_stmt);

            $entities = array();
            while ($row = mysqli_fetch_assoc($results)) {
                array_push($entities, $row);
            }
        }

        return $entities;
    }
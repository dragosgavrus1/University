<?php

    require 'actions/action_get_all.php';
    session_start();
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flights</title>
</head>

<style>
    .entity {
        border: 1px solid black;
        padding: 10px;
        margin: 10px;
    }

    .entity:hover {
        background-color: #eee;
        cursor: pointer;
    }
</style>

<body>
<h2>Flights</h2>
    <button onclick="window.location.href = 'hotels.php';">View Hotels</button>
    <button onclick="window.location.href = 'actions/cancel_reservations.php';">Cancel All Reservations</button>
    <div id="content">
        <?php
            $flights = get_all_flights($_SESSION["city"] , $_SESSION["date"]);
            if(count($flights)>0){
                for ($i = 0; $i < count($flights); $i++) {
                    echo "<div class='entity'>";
                    echo "<span> Flight ". $flights[$i]["flightID"] . " Available seats: " . $flights[$i]["availableSeats"]  ."</span>";
                    echo "<form method='post' action='actions/reserve_flight.php' style='display:inline;'>";
                    echo "<input type='hidden' name='flightID' value='" . $flights[$i]["flightID"] . "'>";
                    echo "<button type='submit'>Reserve</button>";
                    echo "</form>";
                    echo "</div>";
                }
            }
            else {
                echo "<div class='entity'>";
                echo "<a><span>No  flights for selected date and city!</span></a>";
                echo "</div>";
            }
        ?>
    </div>
    

</body>
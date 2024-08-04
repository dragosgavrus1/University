<?php

    require 'actions/action_get_all.php';

    session_start();
?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hotels</title>
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
<h2>Hotels</h2>
    <button onclick="window.location.href = 'flights.php';">View Flights</button>
    <button onclick="window.location.href = 'actions/cancel_reservations.php';">Cancel All Reservations</button>
    <div id="content">
        <?php
            $hotels = get_all_hotels($_SESSION["city"] , $_SESSION["date"]);
            if(count($hotels)>0){
                for ($i = 0; $i < count($hotels); $i++) {
                    echo "<div class='entity'>";
                    echo "<span> Hotel ". $hotels[$i]["hotelID"] . " Available rooms: " . $hotels[$i]["availableRooms"]  ."</span>";
                    echo "<form method='post' action='actions/reserve_hotel.php' style='display:inline;'>";
                    echo "<input type='hidden' name='hotelID' value='" . $hotels[$i]["hotelID"] . "'>";
                    echo "<button type='submit'>Reserve</button>";
                    echo "</form>";
                    echo "</div>";
                }
            }
            else {
                echo "<div class='entity'>";
                echo "<a><span>No hotels for selected date and city!</span></a>";
                echo "</div>";
            }
        ?>
    </div>
</body>
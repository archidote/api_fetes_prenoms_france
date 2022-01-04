<?php
  

$json = file_get_contents('celebrationFrenchDaysAPI.json');
  
// Decode the JSON file
$data = json_decode($json,true);

function getCelebrationFromName ($name) {
    global $data; // globalization of data variable 
    foreach($data["celebrations"] as $celebration) { //foreach element in $arr

        if ($celebration["name"] == $name) {
            header('Content-Type: application/json; charset=utf-8');
            echo json_encode($celebration["date"]); //etc
        }
    }
}

function getCelebrationFromDate ($date) {
    global $data; // globalization of data variable 
    foreach($data["celebrations"] as $celebration) { //foreach element in $arr

        if ($celebration["date"] == $date) {
            header('Content-Type: application/json; charset=utf-8');
            echo json_encode($celebration["name"]); //etc
        }
    }
}

getCelebrationFromName("Philippe");
#getCelebrationFromDate("13/07");
?>
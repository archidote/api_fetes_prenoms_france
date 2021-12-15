<?php
  

$json = file_get_contents('celebrationFrenchDaysAPI.json');
  
// Decode the JSON file
$data = json_decode($json,true);

function getCelebrationFromName () {
    global $data; // globalization of data variable 
    foreach($data["celebrations"] as $celebration) { //foreach element in $arr

        if ($celebration["name"] == "Philippe") {
            echo $celebration["date"]; //etc
        }
    }
}

function getCelebrationFromDate () {
    global $data; // globalization of data variable 
    foreach($data["celebrations"] as $celebration) { //foreach element in $arr

        if ($celebration["date"] == "02/02") {
            echo $celebration["name"]; //etc
        }
    }
}

getCelebrationFromName();
getCelebrationFromDate();
?>
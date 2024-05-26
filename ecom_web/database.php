<?php
$server = "localhost";
$username = "root";
$password = "";
$database = "ecommerce";

$mysqli = new mysqli($server,$username,$password,$database);

if($mysqli->connect_error){
    die("Connection failed:" .$mysqli->connect_error);
}else{
    echo"connection success!";
}
?>
<?php
session_start();
include("database.php");
// Database connection parameters
$servername = "localhost";
$username = "root";
$password = "";
$database = "ecommerce";

// Create a connection to the database
$conn = new mysqli($servername, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$username = $_POST["uname"];
$email = $_POST["email"];
$address = $_POST["address"];
$contact = $_POST["contact"];
$password = $_POST["pass"];
$confirmpassword = $_POST['cpass'];


$sql = "INSERT INTO `users`(`username`, `email`,`address`,`contact`, `password`, `confpassword`) VALUES ('$username', '$email','$address','$contact', '$password','$confirmpassword')";

$select = "SELECT * FROM users where email = '$email' && pass = '$password'";
$result = mysqli_query($conn, $select);
if ($result) {
    if (mysqli_num_rows($result) > 0) {
        $error[] = 'user already exits!';
    }

    if ($conn->query($sql) === TRUE) {
        $response = ['success' => true];
        header('location:login.php');
    } else {
        $response = ['success' => false];
        // echo"Connection failed".mysqli_connect_error();
    }
} else {
    echo "Error:" . mysqli_error($conn);
}

$conn->close();

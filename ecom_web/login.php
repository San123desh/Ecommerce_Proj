<?php
session_start();

include("database.php");

echo "success";
// Database connection parameters
$servername = "localhost";
$username = "root";
$password = "";
$database = "ecommerce";

$conn = new mysqli($servername, $username, $password, $database);

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $email = $_POST['email'];
    $password = $_POST['pass'];

    $select = "SELECT * FROM user WHERE email='$email' && password = '$password'";

    $result = mysqli_query($conn, $select);
    if ($result) {
        if (mysqli_num_rows($result) > 0) {
            $_SESSION['username'] = $row['name'];
            header("location:user_page.php");
        } else {
            $error[] = "Incorrect email or pasword!";
        }
    } else {
        echo "Error:" . mysqli_error($conn);
    }
}

$conn->close();

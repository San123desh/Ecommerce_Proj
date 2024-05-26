<?php
include("database.php");

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $username = $_POST['username'];
    $email = $_POST['email'];
    $address = $_POST['address'];
    $contact = $_POST['contact'];
    $password = $_POST['password'];
    $confirmpassword = $_POST['confirmpassword'];
}

if (empty($username)) {
    $errors[] = "Username is required";
}
if (empty($email)) {
    $errors[] = "Email is required";
}
if (empty($address)) {
    $errors[] = "Address is required";
}
if (empty($contact)) {
    $errors[] = "Contact is required";
}
if (empty($password)) {
    $errors[] = "Password is required";
}
if (empty($confirmpassword)) {
    $errors[] = "Confirm Password is required";
}

if ($password != $confirmpassword) {
    $errors[] = "Password not matching.";
}

if (empty($errors)) {
    $insert = "INSERT INTO users(username,email,address,contact,password,confirmpassword) VALUES('$username','$email','$address','$contact','$password','$confirmpassword')";
    $mysqli_query($conn,$insert);
    header("Location: login.html");
} else {
    foreach ($errors as $error) {
        echo $error . "<br>";
    }
}

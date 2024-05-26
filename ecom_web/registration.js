function clearErrors() {
  errors = document.getElementsByClassName("formerror");
  for (let item of errors) {
    item.innerHTML = "";
  }
}

function seterror(id, error) {
  //sets error inside tag of id
  element = document.getElementById(id);
  element.getElementByClassName("formerror")[0].innerHTML = error;
}

function validateForm() {
  var returnval = true;
  clearErrors();

  var name = document.forms["myForm"]["uname"].value.trim();
  if (name.length < 5) {
    seterror("uname", "Username must be 3 to 20 characters");
    returnval = false;
  }
  var email = document.forms["myForm"]["email"].value.trim();
  if (email.length > 20) {
    seterror("mymail", "Email is too long,should be less than 20");
    returnval = false;
  }
  var contact = document.forms["myForm"]["contact"].value.trim();
  if (contact.length != 10) {
    seterror("mycontact", "Phone number should be of 10 digit!");
    returnval = false;
  }
  var password = document.forms["myForm"]["pass"].value.trim();
  var passReg = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$/;
  var specialReg = /[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]/;

  if (!passReg.test(password) || !specialReg.test(password)) {
    seterror(
      "pass",
      "Password should be at least 6 characters long with at least one capital and one small alphabet and one number and one special character.!"
    );
    returnval = false;
  }
  var cpassword = document.forms["myForm"]["cpass"].value.trim();
  if (cpassword != password) {
    seterror("cpass", "Password not matching!");
    returnval = false;
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const regForm = document.getElementById("signupForm");
  regForm.addEventListener("submit", function (event) {
    if (!validateForm()) {
      event.preventDefault();
    }
  });
});

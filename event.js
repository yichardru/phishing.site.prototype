function postCreds(creds)
{
  console.log("sending",creds);

  fetch("https://127.0.0.1:5000/sendemail"), {
    method: "POST",
    body: {
      "username": creds.u,
      "password": creds.p
    }
  })

}



var button = document.getElementByID("mybutton");
var loginVal = document.getElementById("loginUsername");
var passwordVal = document.getElementById("loginPassword");

button.onclick = function(){
  console.log(loginVal.value, passwordVal.value);
  console.log("Username: ", loginVal.value);
  console.log("Password: ", passwordVal.value);
  postCreds({
    u: loginVal.value,
    p: passwordVal.value
  })
}

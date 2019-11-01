var username = document.getElementById("loginUsername").value;
var password = document.getElementByID("loginPassword").value;
const userAction = async ()=> {
  const response = await fetch('http://127.0.0.1:5000'), {
    method: 'POST',
    body: {
      "username": username,
      "password": password
    }
  });
}

function getCredentials(){
  var username = document.getElementById("loginUsername").value;
  var password = document.getElementById("loginPassword").value;
  const userAction = async ()=> {
    const response = await fetch('http://127.0.0.1:5000/sendemail'), {
      method: 'POST',
      body: {
        "username": username,
        "password": password
      }
    });
  }
}

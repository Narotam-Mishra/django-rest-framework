
const loginForm = document.getElementById('login-form')

const baseEndpoint = "http://localhost:8000/api"

if(loginForm){
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event){
    console.log("Event:", event)
    event.preventDefault()

    const loginEndpoint = `${baseEndpoint}/token/`;
    let loginFormData = new FormData(loginForm);
    let loginObjData = Object.fromEntries(loginFormData);
    let bodyStr = JSON.stringify(loginObjData);
    console.log("Login Data:", loginObjData, "Body String:", bodyStr);

    const options = {
        method: "POST",
        headers: {
            "ContentType": "application/json"
        },
        body: bodyStr,
    }

    fetch(loginEndpoint, options)
    .then(res => {
        console.log("Response:", res)
        return res.json()
    })
    .then(x => console.log("X:", x))
    .catch(err => {
        console.log("Error:", err)
    })
}

const productContainer = document.getElementById('product-container')

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
    // console.log("Login Data:", loginObjData, "Body String:", bodyStr);

    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: bodyStr,
    }

    fetch(loginEndpoint, options)
    .then(res => {
        if (!res.ok) {
            return res.text().then(text => { throw new Error(`Login failed: ${res.status} ${res.statusText} - ${text}`) })
        }
        return res.json()
    })
    .then(authData => {
        handleAuthData(authData, getProductList)
    })
    .catch(err => {
        console.error("Error:", err)
    })
}

function handleAuthData(authData, callback){
    localStorage.setItem('access_token', authData.access)

    localStorage.setItem('refresh_token', authData.refresh)

    if(callback){
        callback()
    }
}

function addProductToContainer(data){
    if(productContainer){
        productContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
    }
}

function getFetchOptions(method, body){
    return {
        method: method === null ? "GET" : method,
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('access_token')}`
        },
        body : body ? body : null
    }
}

function isTokenNotValid(jsonData){
    if(jsonData && jsonData.code === "token_not_valid"){
        alert("Login Again...")
        return false;
    }
    return true
}

function validateJWTToken(){
    const endPoint = `${baseEndpoint}/token/verify/`
    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            token : localStorage.getItem('access_token')
        })
    }
    fetch(endPoint, options)
    .then(response => response.json())
    .then(x => {
        // refresh token
    })
}

function getProductList(){
    const endpoint = `${baseEndpoint}/products/`
    const options = getFetchOptions()

    fetch(endpoint, options)
    .then(response => {
        // console.log("Product Response:",response)
        return response.json()
    })
    .then(data => {
        console.log("product_data:", data)
        const validData = isTokenNotValid(data)
        if(validData){
            addProductToContainer(data)
        }
    })
    .catch(err => {
        console.error("Error fetching product list:", err)
        addProductToContainer({ error: err.message })
    })
}

validateJWTToken()
// getProductList();
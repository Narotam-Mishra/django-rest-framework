
const productContainer = document.getElementById('product-container')

const loginForm = document.getElementById('login-form')

const searchForm = document.getElementById('search-form')

const baseEndpoint = "http://localhost:8000/api"

if(loginForm){
    loginForm.addEventListener('submit', handleLogin)
}

if(searchForm){
    searchForm.addEventListener('submit', handleSearch)
}

function handleSearch(event){
    event.preventDefault()

    let formData = new FormData(searchForm);
    let data = Object.fromEntries(formData);
    let searchParams = new URLSearchParams(data);

    const searchEndpoint = `${baseEndpoint}/search/?${searchParams}`;
    const headers = {
        "Content-Type": "application/json",
    }

    const authToken = localStorage.getItem('access_token')
    if(authToken){
        headers['Authorization'] = `Bearer ${authToken}`
    }

    const options = {
        method: "GET",
        headers: headers,
    }

    fetch(searchEndpoint, options)
    .then(res => {
        return res.json()
    })
    .then(data => {
        console.log("Data Hits:", data.hits)
        addProductToContainer(data)
    })
    .catch(err => {
        console.error("Error:", err)
    })
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

/*
  Initialize the search client

  If you're logged into the Algolia dashboard, the following values for
  ALGOLIA_APPLICATION_ID and ALGOLIA_SEARCH_API_KEY are auto-selected from
  the currently selected Algolia application.
*/
const { liteClient: algoliasearch } = window["algoliasearch/lite"];
const searchClient = algoliasearch(
  "1091QYUB5I",
  "17f60c1a928771b475595ac14515077a",
);

// Render the InstantSearch.js wrapper
// Replace INDEX_NAME with the name of your index.
const search = instantsearch({
  indexName: "djapp_Product",
  searchClient,
});

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: "#searchbox",
  }),

  instantsearch.widgets.clearRefinements({
    container: "#clear-refinements",
  }),

  instantsearch.widgets.refinementList({
    container: "#user-list",
    attribute: 'user',
  }),

  instantsearch.widgets.hits({
    container: "#hits",
    templates: {
        item: `<div>{{ title }}<p>\${{ price }}</div>`
    }
  }),
]);

search.start();
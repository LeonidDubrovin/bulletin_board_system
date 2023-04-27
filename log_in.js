const email = document.querySelector('#email')
const password = document.querySelector('#password')
const button = document.querySelector('#button')


button.onclick = () =>{
    data = {}
    data.email = email.value
    data.password = password.value
    console.log(JSON.stringify(data))
    window.location = 'test.html'
}


/*const url = 'https://jsonplaceholder.typicode.com/users'

const xhr = new XMLHttpRequest()

xhr.open('GET', url)

xhr.responseType = 'json'

xhr.onload = () =>{
    console.log(xhr.response)
}

xhr.send()*/
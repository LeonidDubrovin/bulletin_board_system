const express = require('express')
const cors = require('cors')
const fs = require('fs')


const app = express()
app.use(cors())
app.use(express.json())

app.get("/", function(request, response){
    // const object = {}
    // object.name = 'Hi'
    response.send('Hi')
})

app.post("/create_adv", function(request, response){
    let object = {}
    object.name = request.body.name
    object.cost = request.body.cost
    object.tel_num = request.body.tel_num
    object.dormit = request.body.dormit
    object.descrip = request.body.descrip
    fs.appendFileSync('file.txt', JSON.stringify(object))
    fs.appendFileSync('file.txt', '\n')
    const res = 'Hi'
    response.send(JSON.stringify(res))
})

app.get("/view_adv", function(request, response){
    const array = fs.readFileSync('file.txt').toString().split("\n");
    array.pop()
    for(i in array) array[i] = JSON.parse(array[i])
    //console.log(array)
    response.send(array)
})




app.listen(3000);



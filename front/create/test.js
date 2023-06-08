const but = document.querySelector('#but')
const name = document.querySelector('#name')
const cost = document.querySelector('#cost')
const tel_num = document.querySelector('#tel_num')
const dormit = document.querySelector('#dormit')
const descrip = document.querySelector('#descrip')
//url = 'http://localhost:3000/create_obj'
but.onclick = postData



async function postData(){
    let object = {}
    object.name = name.value
    object.cost = cost.value
    object.tel_num = tel_num.value
    object.dormit = dormit.value
    object.descrip = descrip.value
    url = 'http://localhost:3000/create_adv'
    const response = await fetch(url, {
         method: 'POST',
         body: JSON.stringify(object),
         headers: {
           'Content-type': 'application/json; charset=UTF-8',
         },
       })
    // const data = await response.json()
    // console.log(data)
    window.location.reload()
}





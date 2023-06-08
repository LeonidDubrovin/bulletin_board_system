const advmain = document.querySelector('#mainadv')
//console.log(advmain)
let advert = []
getItems()

async function getItems(){
    const url = 'http://localhost:3000/view_adv'
    const response = await fetch(url)
    const data = await response.json()
    advert = data
    let mas = []
    for (i in advert){
    console.log(advert[i])
    let adv = document.createElement('div')
    adv.className = 'foradv'
    mas[i] = document.createElement('div')
    mas[i].innerHTML = 
    `<h2>Название: ${advert[i].name}</h2>
    <h2>Цена: ${advert[i].cost}</h2>
    <h2>Номер телефона: ${advert[i].tel_num}</h2>
    <h2>Общежитие: ${advert[i].dormit}</h2>
    <h2>Описание: ${advert[i].descrip}</h2>`
    adv.appendChild(mas[i])
    advmain.appendChild(adv)
    }
    //console.log(advert)
}

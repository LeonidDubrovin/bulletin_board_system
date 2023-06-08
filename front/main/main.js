const formOpenBtn = document.querySelector("#form-open"),
main = document.querySelector(".main"),
formContainer = document.querySelector(".form_container"),
formCloseBtn = document.querySelector(".form_close"),
change_signupBtn = document.querySelector("#signup"),
change_loginBtn = document.querySelector("#login"),
pwShowHide = document.querySelectorAll(".pw_hide"),
body = document.querySelector("body"),
username = document.querySelector("#un"),
email = document.querySelector('#l_em'),
password = document.querySelector('#l_pw'),
loginBtn = document.querySelector('#login-btn'),
signupBtn = document.querySelector("#signup-btn"),
input_1 = document.querySelector('#s_pw1'),
input_2 = document.querySelector('#s_pw2'),
but_1 = document.querySelector('#all'),
but_2 = document.querySelector('#create');

but_1.onclick = function() {
window.location.href = '../all_adv/all_adv.html';
}

but_2.onclick = function() {
window.location.href = '../create/create.html';
}


formOpenBtn.addEventListener("click", () => {
    main.classList.add("show");
    body.style.overflow = 'hidden';
});
formCloseBtn.addEventListener("click", () => {
    main.classList.remove("show");
    body.style.overflow = 'auto';
});

pwShowHide.forEach(icon => {
    icon.addEventListener("click", () => {
        let getPwInput = icon.parentElement.querySelector("input");
        if(getPwInput.type === "password") {
            getPwInput.type = "text";
            icon.classList.replace("uil-eye-slash", "uil-eye");
        }else{
            getPwInput.type = "password";
            icon.classList.replace("uil-eye", "uil-eye-slash");
        }
    });
});

change_signupBtn.addEventListener("click", (e) => {
    //e.preventDefault();
    formContainer.classList.add("active");
});
change_loginBtn.addEventListener("click", (e) => {
    //e.preventDefault();
    formContainer.classList.remove("active");
});

/*loginBtn.onclick = recordData

async function recordData(){
    let user = {}
    user.email = l_em.value 
    user.password = l_pw.value 
    console.log(JSON.stringify(user))
    postData_1(user)
}*/

// async function postData(user){
//     const url = "http://26.147.63.125:8000/api/auth/users/"
//     const response = await fetch(url, {
//       method: 'POST',
//       headers:{
//         'Content-Type': 'application/json;charset=utf-8'
//       },
//       body: JSON.stringify(user)  
//     })
//     const data = await response.json()
//     console.log(data)
// }

// async function postData_1(user){
//     const url = "http://26.147.63.125:8000/api/auth/jwt/create/"
//     const response = await fetch(url, {
//       method: 'POST',
//       headers:{
//         'Content-Type': 'application/json;charset=utf-8'
//       },
//       body: JSON.stringify(user)  
//     })
//     const data = await response.json()
//     console.log(data)
// }



signupBtn.onclick = saveData

async function saveData(){
    if (input_1.value === input_2.value) {
        let user = {}
        user.username = un.value
        user.email = s_em.value 
        user.password = s_pw1.value
        console.log(JSON.stringify(user))
        //postData(user)
    }else{
        alert('НЕКОРРЕТНЫЙ ВВОД!')
    }
}
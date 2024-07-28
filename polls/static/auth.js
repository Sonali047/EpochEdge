let login_form = document.querySelector(".login");
let username_login = document.querySelector("#Username-login");
let password_login = document.querySelector("#password-login");



login_form.addEventListener("submit", (event) => {
  event.preventDefault();

  let foo = { username: username_login.value.trim(), password: password_login.value.trim() };

  const options = { method: "POST", body: JSON.stringify(foo) };
  
  fetch("/login-process/", options).then(res => {
    
    
    if (!res.ok) { alert("Wrong combination of username & password")}
    
    
    return res.text();
  
  
  }).then(mes => {
    if (mes === "passed auth") {
      location = "http://127.0.0.1:8000/home/";
    }
  }).catch(err => console.error(err));
})


const signInLink = document.querySelector('.signInBtn-link');
const signUpLink = document.querySelector('.signUpBtn-link');
const wrapper = document.querySelector('.wrapper');

signInLink.addEventListener('click', () => { wrapper.classList.toggle('active');});

signUpLink.addEventListener('click', () => { wrapper.classList.toggle('active');});


let signup_form = document.querySelector(".sign-up");
let username_signup = document.querySelector("#Username-signup");
let password_signup = document.querySelector("#password-signup");

  signup_form.addEventListener("submit", (event) => {
  event.preventDefault();

  let foo = { username: username_signup.value.trim(), password: password_signup.value.trim() };

  const options = { method: "POST", body: JSON.stringify(foo) };

  fetch("/create-user/", options).then(res => {


    if (!res.ok) { alert("Username already taken !! "); }


    return res.text();


  }).then(mes => {
    if (mes === "user created") {
      location = "http://127.0.0.1:8000/home/";
    }
  }).catch(err => console.error(err));


    var a;
    function pass()
    {
        if (a==1)
            {
                document.getElementById('password').type='password';
                document.getElementById('pass-icon').src="{% static 'images/pass-show.jpg' %}";
                a=0;

            }
            else
            {
                document.getElementById('password').type='text';
                document.getElementById('pass-icon').src="{% static 'images/pass-hide.jpg' %}";
                a=1; 
            }
    }
    var b;
    function pass1()
    {
        if (b==1)
            {
                document.getElementById('password1').type='password';
                document.getElementById('pass-icon1').src="{% static 'images/pass-show.jpg' %}";
                b=0;
            }
            else
            {
                document.getElementById('password1').type='text';
                document.getElementById('pass-icon1').src="{% static 'images/pass-hide.jpg' %}";
                b=1; 
    }
    }
})



const SIGNUP_EYE_SHOW = document.querySelector(".pass-icon1.signup-show");
const SIGNUP_EYE_HIDE = document.querySelector(".pass-icon1.signup-hide");

SIGNUP_EYE_SHOW.addEventListener("click", () => {
    password_signup.type = "text";
    SIGNUP_EYE_SHOW.style.display = "none";
    SIGNUP_EYE_HIDE.style.display = "block";
})

SIGNUP_EYE_HIDE.addEventListener("click", () => {
  password_signup.type = "password";
  SIGNUP_EYE_SHOW.style.display = "block";
  SIGNUP_EYE_HIDE.style.display = "none";
})

const SIGNIN_EYE_SHOW = document.querySelector(".pass-icon1.signin-show");
const SIGNIN_EYE_HIDE = document.querySelector(".pass-icon1.signin-hide");

SIGNIN_EYE_SHOW.addEventListener("click", () => {
  password_login.type = "text";  
  SIGNIN_EYE_SHOW.style.display = "none";
  SIGNIN_EYE_HIDE.style.display = "block"
})

SIGNIN_EYE_HIDE.addEventListener("click", () => {
  password_login.type = "password";
  SIGNIN_EYE_SHOW.style.display = "block";
  SIGNIN_EYE_HIDE.style.display = "none";
} )
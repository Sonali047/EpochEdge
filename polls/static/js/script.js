let loginform = document.querySelector('.login-form');

document.querySelector('#login-btn').onclick = () =>
{
    loginform.classList.toggle('active');
   
    navbar.classList.remove('active');
}

let navbar = document.querySelector('.navbar');

document.querySelector('#manu-btn').onclick = () =>
{
    navbar.classList.toggle('active');
    loginform.classList.remove('active');
    
}

window.onscroll = () =>
{
    loginform.classList.remove('active');
    navbar.classList.remove('active');
}


var swiper = new Swiper(".trusted-by-professional-slider", {
    loop:true,
    spaceBetween: 20,
    autoplay:
    {
        delay: 7500,
        disableOnInteraction: false,
    },
     
    breakpoints: {
      0: {
        slidesPerView: 1,
    
      },
      768: {
        slidesPerView: 2,
       
      },
      1020: {
        slidesPerView: 3,
        
      },
    },
  });



let LOGOUT = document.querySelector('.LOGOUT');

LOGOUT.addEventListener("click", (event) => {
  event.preventDefault();
  fetch("/logout/").then(res => res.text()).then(mes => {
    if (mes === "Logged out") {
      // window.location.reload();
      location = "http://127.0.0.1:8000/";
    }
    
  }).catch(err => console.error(err))
})

let menuIcon = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');
menuIcon.onclick = () => 
    {
        menuIcon.classList.toggle('bx-x');
        navbar.classList.toggle('active');
    };




let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

window.onscroll = () => 
{
    sections.forEach(sec => 
    {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');
        if (top >= offset && top <offset + height) 
        {
            navLinks.forEach(links => 
            {
                links.classList.remove('active');
                document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
            });
        };
    });

    let header = document.querySelector('header');
    header.classList.toggle('sticky', window.scrolly > 100);

    menuIcon.classList.remove('bx-x');
    navbar.classList.remove('active');

};
    ScrollReveal({
        //reset: true,
        distance: '80px',
        duration: 2000,
        delay: 200
    });
    ScrollReveal().reveal('.home-content, .heading', { origin: 'top' });
    ScrollReveal().reveal('.home-img, .Features-container, .Contact form', { origin: 'bottom' });
    ScrollReveal().reveal('.home-content h1, .About-img img', { origin: 'left' });
    ScrollReveal().reveal('.home-content p, .About-content', { origin: 'right' });

function toggle()
{
    var blur = document.getElementById('blur');
    blur.classList.toggle('active');
    var popup = document.getElementById('popup');
    popup.classList.toggle('active');
    
}
function toggle1()
{
    var blur = document.getElementById('blur');
    blur.classList.toggle('active');
    var popup1 = document.getElementById('popup1');
    popup1.classList.toggle('active');
}
function toggle2()
{
    var blur = document.getElementById('blur');
    blur.classList.toggle('active');
    var popup2 = document.getElementById('popup2');
    popup2.classList.toggle('active');
}


const FULLNAME = document.querySelector(".full-name");
const EMAIL_ADDRESS = document.querySelector(".email-address");
const MOBILE = document.querySelector(".mobile-num");
const EMAIL_SUBJECT = document.querySelector(".email-subject");
const EMAIL_MESSAGE = document.querySelector(".email-message");
const SEND_BUTTON = document.querySelector(".send-message");

SEND_BUTTON.addEventListener("click", (e) => {
    e.preventDefault();
    if (FULLNAME.value.trim() === "" || EMAIL_ADDRESS.value.trim() === "" || MOBILE.value.trim() === "" || EMAIL_SUBJECT.value.trim() === "" || EMAIL_MESSAGE.value.trim() === "") {
        alert("Please fill all the fields");
        return;
    }
    const data = {
        fullName: FULLNAME.value.trim(),
        emailAddress: EMAIL_ADDRESS.value.trim(),
        phone: MOBILE.value.trim(),
        emailSubject: EMAIL_SUBJECT.value.trim(),
        emailMessage: EMAIL_MESSAGE.value.trim(),
    };


    fetch("/post-review/", { method: "POST", body: JSON.stringify(data) })
})

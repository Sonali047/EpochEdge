const signInLink = document.querySelector('.signInBtn-link');
const signUpLink = document.querySelector('.signUpBtn-link');
const wrapper = document.querySelector('.wrapper');

signInLink.addEventListener('click', () => { wrapper.classList.toggle('active');});

signUpLink.addEventListener('click', () => { wrapper.classList.toggle('active');});
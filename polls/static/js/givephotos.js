const username_field = document.querySelector("#username");
const failure = document.querySelector(".failure");
const success = document.querySelector(".success");

const failure_message = () => {
  success.style.display = "none";
  failure.style.display = "block";
  failure.style.color = "red";
  failure.textContent = "Username does not exist";
};

const success_button = () => {
  success.style.display = "block";
  failure.style.display = "none";
};


success.addEventListener("click", () => {
  
  fetch("/download-files/", { method: "POST", body: JSON.stringify({ username: username_field.value.trim() }) })
  .then(res => res.blob())
  .then( blob => {
         var file = window.URL.createObjectURL(blob);
         window.location.assign(file);
         setTimeout(() => location = "http://127.0.0.1:8000/success/", 1000)
       })
  .catch(err => {
    console.error(err);
  })
})


username_field.addEventListener("input", (event) => {
    const username = event.target.value.trim();
    let foo = { username };
    const options = { method: "POST", body: JSON.stringify(foo) };

    fetch("/does-the-user-exist/", options)
      .then(res => res.text())
      .then(mess => {
        if (mess === "none") {
          failure_message()
        } else if (mess === "yes") {
          success_button()
        }
      })
      .catch(err => console.error(err));
})
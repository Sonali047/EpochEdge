let my_form = document.querySelector("#woohoo");
let my_file = document.querySelector("#file");
let title = document.querySelector("#username");
let output = document.querySelector(".output");

my_form.addEventListener("submit", (event) => {
    event.preventDefault();
    console.log("Hi mom");

    const formData = new FormData();
    // https://stackoverflow.com/a/14908250

    
    // formData.append('file', my_file.files);


    for (let x = 0; x < my_file.files.length; x++) {
        formData.append(`fileToUpload${x}`, my_file.files[x]);
    }

    
    formData.append('title', title.value.trim());
    localStorage.setItem("username", title.value.trim());
    console.log(my_file.files);
    const options = {
        method: "POST",
        body: formData,
    };
    fetch("/guzz/", options).then(res => res.json()).then(data => {
        // let foo = data.images;
        // foo.forEach(x => {
        //     let img = document.createElement("img");
        //     img.src = x;
        //     img.style.width = "200px";
        //     img.style.height = "200px";
        //     img.style.margin = "10px";
        //     img.style.border = "2px solid black";
        //     img.style.borderRadius = "10px";
        //     output.appendChild(img);
        // });


        if (data.message === "User does not exist") {
            alert("Username does not exist");
            return
        }


        location = "http://127.0.0.1:8000/view-photos/";

        

        

        
    }).catch(err => console.error(err));
})
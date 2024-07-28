let output = document.querySelector(".output");

const USERNAME = localStorage.getItem("username");


let count = 0;



fetch("/display/", { method: "POST", body: JSON.stringify({ username: USERNAME }) })
  .then(res => res.json())
  .then(data => {

    let foo = data.images;
    foo.forEach(x => {
        let img = document.createElement("img");
        img.src = x;
        // img.style.width = "200px";
        // img.style.height = "200px";
        // img.style.margin = "10px";
        img.style.border = "2px solid black";
        img.style.borderRadius = "10px";

        count++;

        let table_row = document.createElement("tr");
        let table_data_1 = document.createElement("td");
        let table_data_2 = document.createElement("td");
        let table_data_3 = document.createElement("td");

        table_data_1.innerHTML = count;
        table_data_2.innerHTML = USERNAME;

        table_data_3.appendChild(img);

        table_row.appendChild(table_data_1);
      table_row.appendChild(table_data_2);
      table_row.appendChild(table_data_3);



      output.appendChild(table_row);
      
    });


    



    console.log(data); //....
  })
  .catch(err => console.error(err))
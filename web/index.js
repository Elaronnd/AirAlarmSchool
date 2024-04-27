var icon = document.getElementById("change");
var github = document.getElementById("github");

async function getDataFromPythonForce(place) {
    if (await eel.get_data_force(place)() === true) {
        document.getElementById("stat").innerText = `На даний момент в ${place} повітряна тривога`;
        document.getElementById("stat").style.color = "red";
    } else if(await eel.get_data_force(place)() === false) {
        document.getElementById("stat").innerText = `На даний момент в ${place} немає повітряної тривоги`;
        document.getElementById("stat").style.color = "green";
    } else if (await eel.get_data_force(place)() === null) {
        document.getElementById("stat").innerText = "Помилка з api";
        document.getElementById("stat").style.color = "red";
    }
    else {
        document.getElementById("stat").innerText = "Невідома помилка";
        document.getElementById("stat").style.color = "red";
    }
    document.getElementById("date").innerText = await eel.get_date_time()();
    document.getElementById("lesson").innerText = await eel.lesson()();
}

document.getElementById("button").addEventListener("click", async()=> {
    getDataFromPythonForce(place="м. Київ");
    document.getElementById("button").disabled = true;

    setTimeout(function () {
        document.getElementById("button").disabled = false;
    }, 5000);
})

icon.addEventListener("click", function(){
    document.body.classList.toggle("dark-theme");
    if (document.body.classList.contains("dark-theme")) {
        icon.src = "images/sun.png"
        github.src = "images/github_purple.png"
    } else {
        icon.src = "images/moon.png"
        github.src = "images/github_black.png"
    }
});

if (`${new Date().getHours()}` > 18 || 7 > `${new Date().getHours()}` ) {
    document.body.classList.toggle("dark-theme");
    icon.src = "images/sun.png"
    github.src = "images/github_purple.png"
}

getDataFromPythonForce(place="м. Київ");
setInterval(() => getDataFromPythonForce(place="м. Київ"), 5000);

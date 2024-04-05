async function getDataFromPythonForce(place) {
    if (await eel.get_data_force(place)() === true) {
        document.getElementById("stat").innerText = "На даний момент в Києві повітряна тривога";
        document.getElementById("stat").style.color = "red";
    } else if(await eel.get_data_force(place)() === false) {
        document.getElementById("stat").innerText = "На даний момент в Києві немає повітряної тривоги";
        document.getElementById("stat").style.color = "green";
    } else if (await eel.get_data_force(place)() === "Помилка з api") {
        document.getElementById("stat").innerText = "Помилка з api";
        document.getElementById("stat").style.color = "red";
    }
    else {
        document.getElementById("stat").innerText = "Невідома помилка";
        document.getElementById("stat").style.color = "red";
    }
    document.getElementById("date").innerText = await eel.get_date_time(place)();
}

document.getElementById("button").addEventListener("click", async()=> {
    getDataFromPythonForce("м. Київ");
    document.getElementById("button").disabled = true;

    setTimeout(function () {
        document.getElementById("button").disabled = false;
    }, 5000);
})

getDataFromPythonForce("м. Київ");
setInterval(() => getDataFromPythonForce("м. Київ"), 5000);

async function getDataFromPythonForce() {
    document.getElementById("stat").innerText = await eel.get_data_force()();
    document.getElementById("date").innerText = await eel.get_date_time()();
    if (await eel.get_data_force()() === "[info] На даний момент в Києві повітряна тривога") {
      var li = document.getElementById("stat");
      li.style.color = "red";
}   else {
      var li = document.getElementById("stat");
      li.style.color = "green";
  }
}

document.getElementById("button").addEventListener("click", async()=> {
    getDataFromPythonForce();
})

function startCooldown() {
  document.getElementById("button").disabled = true;

  setTimeout(function () {
    document.getElementById("button").disabled = false;
  }, 5000);
}

document.getElementById("button").addEventListener("click", startCooldown);
getDataFromPythonForce();
setInterval(getDataFromPythonForce, 5000);

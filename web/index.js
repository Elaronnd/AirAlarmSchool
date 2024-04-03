async function getDataFromPythonForce() {
    document.getElementById("myele").innerText = await eel.get_data_force()();
    document.getElementById("date").innerText = await eel.get_date_time()();
    if (await eel.get_data_force()() === "[info] На даний момент в Києві повітряна тривога") {
      var li = document.getElementById("myele");
      li.style.color = "red";
}   else {
      var li = document.getElementById("myele");
      li.style.color = "green";
  }
}

document.getElementById("mybtn").addEventListener("click", async()=> {
    getDataFromPythonForce();
})

function startCooldown() {
  document.getElementById("mybtn").disabled = true;

  setTimeout(function () {
    document.getElementById("mybtn").disabled = false;
  }, 5000);
}

document.getElementById("mybtn").addEventListener("click", startCooldown);
getDataFromPythonForce();
setInterval(getDataFromPythonForce, 5000);

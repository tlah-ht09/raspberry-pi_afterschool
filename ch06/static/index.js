const now = document.getElementById("now");
const record = document.getElementById("record");
const table = document.getElementById("table");

now.addEventListener("click", async () => {
  table.innerHTML = "";
  const response = await fetch("/now", {
    method: "GET",
  });
  const data = await response.json(); // JSON으로 파싱
  console.log("온도:", data[0], "습도:", data[1]);
  const newRow = table.insertRow(-1);

  const cellNo = newRow.insertCell(0);
  const cellDate = newRow.insertCell(1);
  const cellTemp = newRow.insertCell(2);
  const cellHum = newRow.insertCell(3);

  cellNo.innerHTML = null;
  cellDate.innerHTML = null;
  cellTemp.innerHTML = data[0];
  cellHum.innerHTML = data[1];
});

record.addEventListener("click", async () => {
  const response = await fetch("/now", {
    method: "GET",
  });
  const data = await response.json();
  console.log(data);

  const cellNo = newRow.insertCell(0);
  const cellDate = newRow.insertCell(1);
  const cellTemp = newRow.insertCell(2);
  const cellHum = newRow.insertCell(3);
});

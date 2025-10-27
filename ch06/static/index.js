const now = document.getElementById("now");
const record = document.getElementById("record");

now.addEventListener("click", async () => {
  const response = await fetch("/now", {
    method: "GET",
  });
  const data = await response.json(); // JSON으로 파싱
  console.log(data);
});

record.addEventListener("click", async () => {
  const response = await fetch("/now", {
    method: "GET",
  });
  console.log(response.body);
});

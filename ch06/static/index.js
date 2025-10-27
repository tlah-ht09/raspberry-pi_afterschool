const now = document.getElementById("now");
const record = document.getElementById("record");

now.addEventListener("click", async () => {
  const response = await fetch("/now", {
    method: "GET",
  });
  console.log(response.body);
});

record.addEventListener("click", async () => {
  const response = await fetch("/now", {
    method: "GET",
  });
  console.log(response.body);
});

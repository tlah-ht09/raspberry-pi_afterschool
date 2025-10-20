const input = document.getElementById("input");
const send = document.getElementById("send");

send.addEventListener("click", async () => {
  const response = await fetch(`/send/${input.value}`, { method: "GET" });
  console.log(input.value);
});

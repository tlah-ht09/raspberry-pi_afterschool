const input = document.getElementById("input");
const send = document.getElementById("send");

const go = 5;

window.addEventListener("keydown", async (e) => {
  if (e.key == "ArrowLeft") {
    console.log("left");
    const response = await fetch(`/send`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(go),
    });
  } else if (e.key == "ArrowRight") {
    console.log("right");
    const response = await fetch(`/send`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(-go),
    });
  }
});

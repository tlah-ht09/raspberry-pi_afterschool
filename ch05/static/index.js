const input = document.getElementById("input");
const send = document.getElementById("send");

const go = 5;

window.addEventListener("keydown", async (e) => {
  if (e.key == LeftArrow) {
    const response = await fetch(`/send`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(go),
    });
  } else if (e.key == RightArrow) {
    const response = await fetch(`/send`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(-go),
    });
  }
});

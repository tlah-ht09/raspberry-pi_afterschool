const send = document.getElementById("send");
const img = document.getElementById("img");

const go = 10;

window.addEventListener("keydown", async (e) => {
  if (e.key == "ArrowLeft") {
    img.src = "./천칭 왼쪽 복사본.png";
    console.log("left");
    const response = await fetch(`/send`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(go),
    });
  } else if (e.key == "ArrowRight") {
    img.src = "./천칭 오른쪽 복사본.png";
    console.log("right");
    const response = await fetch(`/send`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(-go),
    });
  }
});

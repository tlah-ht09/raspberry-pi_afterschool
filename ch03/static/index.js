const led = document.getElementById("LED");

const on = document.getElementById("on");
const off = document.getElementById("off");

const r = document.getElementById("r");
const g = document.getElementById("g");
const y = document.getElementById("y");

window.addEventListener("keydown", async (e) => {
  if (e.key === "y") {
    const response = await fetch("/y", { method: "GET" });
    console.log("y");
    y.style.backgroundColor = "yellow";
  } else if (e.key === "g") {
    const response = await fetch("/g", { method: "GET" });
    console.log("g");
    g.style.backgroundColor = "greenyellow";
  } else if (e.key === "r") {
    const response = await fetch("/r", { method: "GET" });
    console.log("r");
    r.style.backgroundColor = "orangered";
  }
});

window.addEventListener("keyup", async (e) => {
  const response = await fetch("/off", { method: "GET" });
  y.style.backgroundColor = "gray";
  g.style.backgroundColor = "gray";
  r.style.backgroundColor = "gray";
});

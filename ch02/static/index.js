const p_b = document.getElementById("p_b");
const s_b = document.getElementById("s_b");
const num = document.getElementById("num");
let n = 0;


s_b.addEventListener("click",async ()=>{
    let res = await fetch("/submit", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({value:n})
    })
    n=0;
    num.innerHTML=n
})

p_b.addEventListener("click",()=>{
    n+=1;
    num.innerHTML=n;
})
document.addEventListener("DOMContentLoaded", async () =>
{
        const alertbutton = document.getElementById("alertbtn")
        if(alertbutton)
        {
            alertbutton.addEventListener("click", async () => {alert("alert")})
        }
})
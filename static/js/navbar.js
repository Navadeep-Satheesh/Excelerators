


const navbar_links = document.getElementById("links");
const close_navbar_link = document.getElementById("close_navbar_links");

const show_navbar_links = document.getElementById("show_navbar");

show_navbar_links.addEventListener("click" , ()=>{

    navbar_links.style.left = "0vw";
    console.log(navbar_links.style.display)
    // navbar_links.style.display = "inline"

})

close_navbar_link.addEventListener("click" , ()=>{
    navbar_links.removeAttribute("style");
})






const navbar_links = document.getElementById("links");
const close_navbar_link = document.getElementById("close_navbar_links");

const show_navbar_links = document.getElementById("show_navbar");

show_navbar_links.addEventListener("click" , ()=>{

    navbar_links.style.display = "inline";

})

close_navbar_link.addEventListener("click" , ()=>{
    navbar_links.removeAttribute("style");
})


const navbar = document.getElementById("navbar");
window.addEventListener("scroll" , ()=> {
    console.log(window.scrollY );

    if(window.scrollY    > window.innerHeight/2){
        console.log("changing background color")
        navbar.style.backgroundColor = "black";

    }else{
        navbar.style.backgroundColor = "transparent";
    }
})
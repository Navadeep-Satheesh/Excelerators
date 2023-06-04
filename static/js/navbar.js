


const navbar_links = document.getElementById("links");
const close_navbar_link = document.getElementById("close_navbar_links");

const show_navbar_links = document.getElementById("show_navbar");

const bar1 = show_navbar_links.querySelector(".bar1")
const bar2 = show_navbar_links.querySelector(".bar2")
const bar3 = show_navbar_links.querySelector(".bar3")

var navbar_links_visible= false;

show_navbar_links.addEventListener("click" , (event)=>{

    if(show_navbar_links.contains(event.target)){

        if(!navbar_links_visible){
            
            navbar_links.style.left = "0vw";
            window.navbar_links_visible =  true;

            // bar1.style.transform = "rotate(45deg)";
            // bar2.style.display = "none";
            // bar3.style.transform = "rotate(-45deg)";
            

        }else{
            navbar_links.removeAttribute("style")
            window.navbar_links_visible = false;
            // bar1.removeAttribute("style")
            // bar2.removeAttribute("style")
            // bar3.removeAttribute("style")

        }

        bar1.classList.toggle("bar1_close")
        bar2.classList.toggle("bar2_close")
        bar3.classList.toggle("bar3_close")
        // navbar_links.style.left = "0vw";

        console.log(navbar_links.classList);
        
     
    }
    
    // navbar_links.style.display = "inline"

})




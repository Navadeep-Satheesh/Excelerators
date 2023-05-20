
const go_to_home =  document.getElementById("go_to_home");
go_to_home.remove();

document.getElementsByClassName("empty")[0].remove();


const image_slider = document.getElementById("images");

const loader = document.getElementById("loader");
setTimeout( ()=>{
    loader.style.display = "none";
}, 100)


var current_image = 0;
number_of_images = 5;
setInterval(()=>{

    current_image +=1;
    image_slider.style.left = `-${current_image*100}vw`;
    if(current_image ==  number_of_images){
        image_slider.style.transition = "0s";
        image_slider.style.left = "0vw";

        setTimeout(() => {
            image_slider.style.transition= "0.5s";
        }, 100);

       
        current_image = 0
    }


}, 4000);

const members_back = document.getElementById("members_back");
const members_front = document.getElementById("members_front");
const projects_back = document.getElementById("projects_back");
const projects_front = document.getElementById("projects_front");

const membersStrip = document.getElementById("allmembers");
const projectsStrip = document.getElementById("allprojects");

// membersStrip.style.left = "0vw";

// members_back.addEventListener("click" , ()=>{
// 
    // console.log("moving back")
// 
    // if(parseInt(membersStrip.style.left.slice(0, -2)) < 0 ){
        // membersStrip.style.left = `${parseInt( membersStrip.style.left.slice(0,-2))  + 100}vw`;
        // console.log(membersStrip.style.left);
    // }
    // 
// })
// 
// members_front.addEventListener("click" , ()=>{
// 
    // console.log("moving front");
// 
    // var members = membersStrip.getElementsByClassName("single_member");
// 
    // console.log(parseInt(membersStrip.style.left.slice(0, -2) ))  ;
    // console.log(-(members.length* 100));
// 
    // if(parseInt(membersStrip.style.left.slice(0, -2)) > -(members.length* 100) ){
        // membersStrip.style.left = `${parseInt( membersStrip.style.left.slice(0,-2))  - 80}vw`;
        // console.log(membersStrip.style.left);   
    // }
    // 
// })
// 

const navbar = document.getElementById("navbar");
const links = document.getElementById("links");
window.addEventListener("scroll" , ()=> {
    // console.log(window.scrollY );
   
        

            
            if(window.scrollY    > window.innerHeight/2){
               


                navbar.style.backgroundColor = "black";
                
                if(window.innerHeight <= window.innerWidth){
                    
                    links.style.backgroundColor = "black";
                }
                
            }else{
                
                navbar.style.backgroundColor = "transparent";
                
                if(window.innerHeight <= window.innerWidth){
                    links.style.backgroundColor = "transparent"
                }
               
            }
            
        
    })




const link_to_div = {
    
    "about_us_link": "about_us" ,
    "projects_link" : "projects" ,
    "members_link":  "members" ,
    "sponsers_link": "sponsers" ,
    "gallery_link" : "gallery"
}


const all_links = links.getElementsByClassName("link")
console.log(all_links)


document.querySelector(".home_link").addEventListener("click" , ()=>{
    scroll({top : 0, behavior: "smooth"})
})

Array.from(all_links).forEach((link)=>{

    link.addEventListener("click" , (event)=>{

        event.preventDefault();

        console.log( link_to_div[link.classList[1]] )
       

        var distance  = document.getElementById( link_to_div[link.classList[1]] ).getBoundingClientRect().top;
        console.log(distance)
        scroll({top :  window.scrollY + distance - innerHeight/11 , behavior: "smooth"})
        
        console.log(link.classList);
        

    })


})

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

membersStrip.style.left = "0vw";

members_back.addEventListener("click" , ()=>{

    console.log("moving back")

    if(parseInt(membersStrip.style.left.slice(0, -2)) < 0 ){
        membersStrip.style.left = `${parseInt( membersStrip.style.left.slice(0,-2))  + 100}vw`;
        console.log(membersStrip.style.left);
    }
    
})

members_front.addEventListener("click" , ()=>{

    console.log("moving front");

    var members = membersStrip.getElementsByClassName("single_member");

    console.log(parseInt(membersStrip.style.left.slice(0, -2) ))  ;
    console.log(-(members.length* 100));

    if(parseInt(membersStrip.style.left.slice(0, -2)) > -(members.length* 100) ){
        membersStrip.style.left = `${parseInt( membersStrip.style.left.slice(0,-2))  - 80}vw`;
        console.log(membersStrip.style.left);   
    }
    
})
const images = Array.from(document.getElementsByClassName("singleImage"));
const imageViewer = document.getElementById("imageViewer");
const all_black = document.getElementById("all_black");

const image = document.querySelector("#imageViewerImage");


// const links = document.getElementById("links");
// const show_navbar = document.getElementById("show_navbar");

// links.remove();
// show_navbar.remove();

var current_image; 


images.forEach((singleImage) => {

    singleImage.addEventListener("click", () => {

        console.log("clicked");


        window.current_image = images.indexOf(singleImage);

        all_black.style.display = "flex";
        imageViewer.style.display = "flex";

        image.src = singleImage.querySelector("img").src;
        adjustImageSize();



    })

})

console.log(image)

function adjustImageSize() {

    console.log(image.clientWidth, window.innerWidth);
    console.log(image.clientHeight, window.innerHeight)
    if (image.clientWidth > window.innerWidth) {
        image.style.width = "80%";
        image.style.height = "unset";
        console.log(image.style.width, image.style.height)
    } else if (image.clientHeight > window.innerHeight) {
        image.stye.width = "unset";
        image.style.height = "80%";
    }

}


window.addEventListener("resize", () => {
    adjustImageSize();
})


const close = document.getElementById("close");
const next = document.getElementById("next");
const previous = document.getElementById("previous");
close.addEventListener("click" , ()=>{

    all_black.style.display = "none";
    imageViewer.style.display = "none";

})

next.addEventListener("click" , ()=>{

    if(current_image < images.length-1 ){
        window.current_image +=1;
        image.src = images[current_image].querySelector("img").src;
        adjustImageSize();
    }else{
        window.current_image = 0;
    }

})

previous.addEventListener("click" , ()=>{
    if(current_image > 0){
        window.current_image -=1;
        image.src = images[current_image].querySelector("img").src;
        adjustImageSize();

    }
    else{
        window.current_image = images.length-1;
    }
})


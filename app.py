from flask import Flask , render_template
import os , sys 
import json 
import csv


# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

sponsers_list = json.load(open("sponsers.json" ))["sponsers"]

members_list = list(csv.reader(open("members.csv" , "r")))[1:]
for item in members_list:
    item[5] =   f"https://drive.google.com/uc?export=view&id={item[5].split('id=')[1]}"

print(members_list)


links = json.load(open("links.json" ))
print(links)

app = Flask(__name__)


completed = [

     [ 1,  "ebike 2021", "ebike20221.jpg" ,
    
            """
                Zephyr, our E-bike is like a pleasant breeze but built to last.
                Our e-bike is meticulously crafted for safety, durability, and affordability through ethical engineering practices.
                It had achieved overall AIR - 7 at ETWDC 2022.

            """
     ] ,

      [ 2,  "Fuego F-15", "image3.jpg" ,
    
        """
            ith unwavering enthusiasm, our team produced the Fuego F-15, aimed to be unbeatable in the track, as its name says. 
            ith a compact and driver friendly design, our newest Go - Kart was indeed, majestic in the events, achieving an overall of AIR - 7 in FKDC Season 5, followed by an AIR - 1 in Cost, and AIR - 5 in Acceleration and Autocross.
        """
 ] ,

  [ 3,  "Fuego 2.O", "gokart20211.jpg" ,
    
        """
The fire was unleashed again, with a bigger and better force, as we launched our new Go-kart, the Fuego 2.0, 2 years after its predecessor. 
With its ergonomic design, our Go-Kart did a fantastic feat in IKC Virtuals'22 achieving a score of AIR - 10 and Kerala - 1. 

        """
 ] 

]


events  = [
     
     "blender.jpg",
     "inventor.jpg",
     "linux_commands.jpg",
     "premier_pro.jpg",
     "ansys.jpg",
 ]






@app.route("/")
def home():
    gallery_images = links['gallery_images'][:4]
    return render_template("home.html" , projects = completed , sponsers = sponsers_list , events = events ,  members = members_list , member_count = 13  , gallery_images = gallery_images)

@app.route("/members")
def members():

    return render_template("members.html" , members = members_list)

@app.route("/projects")
def projects():

    return render_template("projects2.html" , completed = completed , upcoming = [])

@app.route("/sponsers")
def sponsers():
    return render_template("sponsers.html", sponsers = sponsers_list)

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


@app.route("/gallery")
def gallery():

    gallery_images = links['gallery_images']
    return render_template("gallery.html", gallery_images = gallery_images)


    
if __name__ == "__main__":
    app.run(debug=True )
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
     [ 1,  "ebike 2021", "ebike20221.jpg"],
     [ 2, "gokart 2022", "image3.jpg"],
    #  [ 2, "gokart 2022", "gokart20212.jpg"],
     [3,  "gokart 2021" , "gokart20211.jpg"]
 ]

@app.route("/")
def home():
    gallery_images = links['gallery_images'][:4]
    return render_template("home.html" , projects = completed , sponsers = sponsers_list ,  members = members_list , member_count = 13  , gallery_images = gallery_images)

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
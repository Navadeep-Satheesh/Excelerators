from flask import Flask , render_template
import os , sys 
import json 


# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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
    return render_template("home.html" , projects = completed , members = [0]*20 , member_count = 13 , sponsers = [0]*9 , gallery_images = gallery_images)

@app.route("/members")
def members():

    execom_members = [0]*20
    normal_members = [1,2,3,4]
    return render_template("members.html" , execom_members = execom_members)

@app.route("/projects")
def projects():

    return render_template("projects2.html" , completed = completed , upcoming = [])

@app.route("/sponsers")
def sponsers():
    return render_template("sponsers.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")


@app.route("/gallery")
def gallery():

    gallery_images = links['gallery_images']
    return render_template("gallery.html", gallery_images = gallery_images)


    
if __name__ == "__main__":
    app.run(debug=True , host = "192.168.29.52")
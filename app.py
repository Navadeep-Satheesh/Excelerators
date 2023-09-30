from flask import Flask , render_template , request
import os , sys 
import json 
import csv
import pygsheets

client = pygsheets.authorize(service_account_file="excelerators-400623-cd37b50cb245.json")
print(client.spreadsheet_titles())


# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

sponsers_list = json.load(open("sponsers.json" ))["sponsers"]

members_list = list(csv.reader(open("members.csv" , "r")))[1:]
for item in members_list:
    item[5] =   f"https://drive.google.com/uc?export=view&id={item[5].split('id=')[1]}"


links = json.load(open("links.json" ))


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
 ] ,

 [
   
      4, "Satva" , "satva.jpg"  ,
      
        """
        Sathva, a project dedicated to the betterment of society, it is lifting platform that empowers individuals with disabilities to access and exit the stage with ease
        """
      
      
      
 ]

]


events_data  = {


    "proteus":[

            "proteus",
            "Proteus",
            "proteus.png",
            """
Learning is like rowing upstream: not to advance is a drop back 

It's more than  fun to design some freaky electrical circuits. 

 Proteus is a proprietary software tool suite used primarily for electronic design automation. The software is used mainly by electronic design engineers and technicians to create schematics and electronic prints for manufacturing printed circuit boards.

Let's master the art of circuit designing ✨  

            """

    ]
    ,
    "stock_market" : [

            "stock_market",
            "STOCK MARKET",
            "stock_market.jpeg",
            """
                " Don't sit down and wait for the opportunities to come, get up and make them" 
 -Madam C J Walker

Stock market is where investors buy and sell shares of companies.It's a set of exchanges where companies issue shares and other securities for trading

Join the session to pave the way...✨
            """,
            "https://drive.google.com/file/d/16IWBq0TlT87m5lfl_wDljQip05vkLJcp/preview"

    ] ,
     "blender" : [
            "blender",
            "Blender" , 
            "blender.jpg",
            """
"I think the work that they do and the style of 3D graphics is absolutely fabulous and I think it's a great brush to use for some stories." -Don Bluth

Blender is a free and open-source 3D computer graphics software tool set used for creating animated films, visual effects, art etc. It is a powerful, versatile tool that enables users to bring their creative ideas to life.

So if you ever wanted to make a 3D version of yourself, now you can—just don't forget to give your virtual self a good hair day!
        """

     ],
     "inventor" : [
            "inventor",
            "AutoDesk Inventor" , 
            "inventor.jpg", 
            ""

     ],
     "linux_commands" : [
            "linux_commands",
            "Basics of Linux Commands", 
            "linux_commands.jpg",
            ""

     ],
     "premier_pro": [
         "premier_pro",
         "Premier Pro",
         "premier_pro.jpg",
         ""
     ],
     "ansys" : [
        "ansys",
         "Ansys",
         "ansys.jpg",
         ""
     ]
}






@app.route("/")
def home():
    gallery_images = links['gallery_images'][:4]
    return render_template("home.html" , projects = completed , sponsers = sponsers_list , events = events_data.values() ,  members = members_list , member_count = 13  , gallery_images = gallery_images)

@app.route("/members")
def members():

    return render_template("members.html" , members = members_list)

@app.route("/projects")
def projects():

    return render_template("projects2.html" , completed = completed , upcoming = [])

@app.route("/events/")
def events():
    return render_template("events.html" , events =  events_data.values())

@app.route("/events/<event>/")
def singleEvent(event):
    return render_template("single_event.html" , details = events_data[event])

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

@app.route("/events/solidworks", methods = ["GET" , "POST"])
def solidworks():   

    if request.method == "POST":

        data = request.form

        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        year = data.get("year")
        department = data.get("department")

        image = request.files['image']

        if( all(value != "" for value in [name , email , phone , year , department]) ):

            file = open("data/events/solidworks/solidworks.csv", "a")
            writer = csv.writer(file)

            writer.writerow([name , email , phone , year , department, image.filename ])
            image.save(f'./data/events/solidworks/screenshots/{image.filename}')

        return render_template("registration_thanks.html" )
    
    return render_template("event_register.html")




    
if __name__ == "__main__":
    app.run(debug=True )
from flask import Flask, render_template
import random
import json
import cloudinary
import cloudinary.uploader
import cloudinary.api
import re
# import gunicorn

cloudinary.config( 
  cloud_name = "your name", 
  api_key = "your key", 
  api_secret = "your secret",
  secure = True
)

with open('main.json', 'r') as f:
    data = json.load(f)


resources = data['resources']
number_files = (len(resources))

# get no. of photos from static 
# dir = "static\photos"
# list = os.listdir(dir) # dir is your directory path
# number_files = len(list)


# PHOTO_FOLDER = os.path.join('static', 'photos')

app = Flask(__name__)
# app.config['Photo_folder'] = PHOTO_FOLDER

@app.route('/')
@app.route('/index')
def show_index():
    
    photo_index = random.randint(1,number_files)
    public_id = resources[photo_index]['public_id']
    r =cloudinary.CloudinaryImage(public_id).image(quality ='auto:low')
    r = re.findall('"([^"]*)"', r)
    download_url = cloudinary.CloudinaryImage(public_id).image(quality ='auto:best')
    
    download_url = re.findall('"([^"]*)"', download_url)
    # print(download_url)
    # png = f'{photo_index}.png'
    # print(data)
    
    # full_filename = os.path.join(app.config['Photo_folder'], png)
    # print(full_filename)
    # photo_id  =  data[png]
    # url = f"https://drive.google.com/uc?export=download&id={photo_id}"
    return render_template("index.html", photo_src= r[0],photo = public_id, download_url = download_url[0])

@app.route('/Images/<public_id>')
def fullview_image(public_id):
    id = 'Images/'+public_id
    r =cloudinary.CloudinaryImage(id).image(quality ='auto:best')
    url = re.findall('"([^"]*)"', r)
    
    # photo_id  =  data[image]
    # url = f"https://drive.google.com/uc?export=download&id={photo_id}"
    # full_filename = os.path.join(app.config['Photo_folder'], image)
    # print(full_filename)
    return render_template("fullview.html", photo_src= url[0] )

if __name__ == '__main__':
   app.run(host="192.168.1.6",port=8000, debug=  True)
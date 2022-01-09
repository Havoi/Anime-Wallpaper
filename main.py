from flask import Flask, render_template
import os
import random
import json

data = {}
with open('data.json', 'r') as f:
    data = json.load(f)
number_files = (len(data))

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
    png = f'{photo_index}.png'
    # print(data)
    
    # full_filename = os.path.join(app.config['Photo_folder'], png)
    # print(full_filename)
    photo_id  =  data[png]
    url = f"https://drive.google.com/uc?export=download&id={photo_id}"
    return render_template("index.html", photo_src= url , photo = png)

@app.route('/image/<image>')
def fullview_image(image):
    photo_id  =  data[image]
    url = f"https://drive.google.com/uc?export=download&id={photo_id}"
    # full_filename = os.path.join(app.config['Photo_folder'], image)
    # print(full_filename)
    return render_template("fullview.html", photo_src= url)

if __name__ == '__main__':
   app.run(host="192.168.1.6",port=8000, debug=  True)
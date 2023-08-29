from flask import Flask, redirect , render_template , request 
import subprocess , re , os
from extra import *
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import cv2
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static', 'img')
plant_model = load_model('models\plant_model.h5')


@app.route("/", methods=['GET' , 'POST'])
def main():
    title = ""
    image = ""
    if request.method == 'POST':
        if 'image' in request.files:
            uploaded_image = request.files['image']
            if uploaded_image.filename != '':
                image_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_image.filename)
                uploaded_image.save(image_path)
                
                #preprocessing
                images = cv2.imread(image_path, cv2.IMREAD_COLOR)
                images = cv2.resize(images, (240,240))
                # Make predictions using the model
                plant_predictions = plant_model.predict(np.array([images]))
                plant_pred = np.argmax(plant_predictions)

                d_model_path, classes = get_model(plant_pred)
                disease_model = load_model(d_model_path)
                disease_pred = disease_model.predict(np.array([images]))
                pred = np.argmax(disease_pred)

                title =  get_plant(plant_pred) + " " + classes[pred]
                image = uploaded_image.filename

            
        
    return render_template('index.html', title = title , image = image)


def get_address():
    output = subprocess.check_output('ipconfig', shell=True, text=True)
    pattern = r'IPv4 Address[ .]*: (\d+\.\d+\.\d+\.\d+)'
    address = re.findall(pattern, output)
    return address[-1]

if __name__ == "__main__":
    app.run(debug=True, host=get_address())

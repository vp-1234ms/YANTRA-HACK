from flask import Flask, request, render_template,app
from PIL import Image
import numpy as np
import os
from tensorflow import keras
from tensorflow.keras import layers

application = Flask(__name__)
app=application


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload():
    
    if 'image' not in request.files:
        return 'No image uploaded'
    new_image_path = r"img/image.jpg"
    input_width, input_height = 224, 224

    image = request.files['image']
    
    # Save the image to a specific path
    image.save('img/image.jpg')
    st = request.form['crop']
    if(st=="Apple"):
        # Make predictions on a new image using the saved model
        def predict_image(image_path):
            # Set the desired dimensions for the input images
            input_width, input_height = 224, 224
            img = Image.open(image_path)
            img = img.resize((input_width, input_height))
            img_array = np.array(img)
            img_array = img_array / 255.0  # Normalize pixel values between 0 and 1
            img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension for batch
            model = keras.models.load_model("AppleFruit")
            prediction = model.predict(img_array)
            class_label = "Apple With Black Rot" if prediction[0][0] < 0.5 else "Healthy Apple"
            return class_label
        # Provide the path to a new image for prediction
        new_image_path = r"img/image.jpg"
        prediction = predict_image(new_image_path)
        print("Prediction:", prediction)

    elif(st=="Potato"):
        # Make predictions on a new image using the saved model
        # Make predictions on a new image using the saved model
        def predict_image(image_path):
            img = Image.open(image_path)
            img = img.resize((input_width, input_height))
            img_array = np.array(img)
            img_array = img_array / 255.0  # Normalize pixel values between 0 and 1
            img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension for batch
            model = keras.models.load_model("Potato Fruit")
            prediction = model.predict(img_array)
            class_label = "Potato With Early Blight" if prediction[0][0] < 0.5 else "Healthy Potato"
            return class_label
        # Provide the path to a new image for prediction
        new_image_path = r"img/image.jpg"
        prediction = predict_image(new_image_path)
        print("Prediction:", prediction)

    elif(st=="Tomato"):
            # Make predictions on a new image using the saved model
        def predict_image(image_path):
            img = Image.open(image_path)
            img = img.resize((input_width, input_height))
            img_array = np.array(img)
            img_array = img_array / 255.0  # Normalize pixel values between 0 and 1
            img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension for batch
            model = keras.models.load_model("Tomato Fruit")
            prediction = model.predict(img_array)
            class_label = "Tomato backtorial Spot" if prediction[0][0] < 0.5 else "Healthy Tomato"
            return class_label
        # Provide the path to a new image for prediction
        new_image_path = r"img/image.jpg"
        prediction = predict_image(new_image_path)
        print("Prediction:", prediction)

    elif(st=="Cron"):
        # Make predictions on a new image using the saved model
        # Make predictions on a new image using the saved model
        def predict_image(image_path):
            img = Image.open(image_path)
            img = img.resize((input_width, input_height))
            img_array = np.array(img)
            img_array = img_array / 255.0  # Normalize pixel values between 0 and 1
            img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension for batch
            model = keras.models.load_model("Potato Fruit")
            prediction = model.predict(img_array)
            class_label = "Corn With Common Rust" if prediction[0][0] < 0.5 else "Healthy Corn"
            return class_label
        # Provide the path to a new image for prediction
        new_image_path = r"img/image.jpg"
        prediction = predict_image(new_image_path)
        print("Prediction:", prediction)

    elif(st=="Bell Pepper"):
    # Make predictions on a new image using the saved model
        def predict_image(image_path):
            img = Image.open(image_path)
            img = img.resize((input_width, input_height))
            img_array = np.array(img)
            img_array = img_array / 255.0  # Normalize pixel values between 0 and 1
            img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension for batch
            model = keras.models.load_model("Potato Fruit")
            prediction = model.predict(img_array)
            class_label = "Bell Pepper With Bactorial Spot" if prediction[0][0] < 0.5 else "Healthy Bell Pepper"
            return class_label
        # Provide the path to a new image for prediction
        new_image_path = r"img/image.jpg"
        prediction = predict_image(new_image_path)
        print("Prediction:", prediction)

    elif(st=="Strawberry"):
                # Make predictions on a new image using the saved model
        def predict_image(image_path):
            img = Image.open(image_path)
            img = img.resize((input_width, input_height))
            img_array = np.array(img)
            img_array = img_array / 255.0  # Normalize pixel values between 0 and 1
            img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension for batch
            model = keras.models.load_model("Strawberry Fruit")
            prediction = model.predict(img_array)
            class_label = "Strawberry With Leaf Scorch" if prediction[0][0] < 0.5 else "Healthy Strawberry"
            return class_label
            # Provide the path to a new image for prediction
        new_image_path = r"img/image.jpg"
        prediction = predict_image(new_image_path)
        print("Prediction:", prediction)

    elif(st=="Cherry"):
                # Make predictions on a new image using the saved model
        def predict_image(image_path):
            img = Image.open(image_path)
            img = img.resize((input_width, input_height))
            img_array = np.array(img)
            img_array = img_array / 255.0  # Normalize pixel values between 0 and 1
            img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension for batch
            model = keras.models.load_model("Cherry Fruit")
            prediction = model.predict(img_array)
            class_label = "Cherry With Powder Mildrew" if prediction[0][0] < 0.5 else "Healthy Cherry"
            return class_label
        new_image_path = r"img/image.jpg"
        prediction = predict_image(new_image_path)
        print("Prediction:", prediction)

    elif(st=="Peach"):
                # Make predictions on a new image using the saved model
        def predict_image(image_path):
            img = Image.open(image_path)
            img = img.resize((input_width, input_height))
            img_array = np.array(img)
            img_array = img_array / 255.0  # Normalize pixel values between 0 and 1
            img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension for batch
            model = keras.models.load_model("Peach Fruit")
            prediction = model.predict(img_array)
            class_label = "Peach With Bacterial Spot" if prediction[0][0] < 0.5 else "Healthy Peach"
            return class_label
        new_image_path = r"img/image.jpg"
        prediction = predict_image(new_image_path)
        print("Prediction:", prediction)


    elif(st=="Citrus"):
                # Make predictions on a new image using the saved model
        def predict_image(image_path):
            img = Image.open(image_path)
            img = img.resize((input_width, input_height))
            img_array = np.array(img)
            img_array = img_array / 255.0  # Normalize pixel values between 0 and 1
            img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension for batch
            model = keras.models.load_model("Potato Fruit")
            prediction = model.predict(img_array)
            class_label = "Citrus With Black Spot" if prediction[0][0] < 0.5 else "Healthy Citrus"
            return class_label
        new_image_path = r"img/image.jpg"
        prediction = predict_image(new_image_path)
        print("Prediction:", prediction)

    elif(st=="Grape"):
        # Make predictions on a new image
        def predict_image(image_path):
            img = Image.open(image_path)
            img = img.resize((input_width, input_height))
            img_array = np.array(img)
            img_array = img_array / 255.0  # Normalize pixel values between 0 and 1
            img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension for batch
            prediction = model10.predict(img_array)
            model = keras.models.load_model("Potao Fruit")
            class_label = "Grape With Black Measles" if prediction[0][0] < 0.5 else "Healthy Grape"
            return class_label
        new_image_path = r"img/image.jpg"
        prediction = predict_image(new_image_path)
        print("Prediction:", prediction)
    elif(st=="Hibiscus"):
        # Make predictions on a new image using the saved model
        def predict_image(image_path):
            # Set the desired dimensions for the input images
            input_width, input_height = 224, 224
            img = Image.open(image_path)
            img = img.resize((input_width, input_height))
            img_array = np.array(img)
            img_array = img_array / 255.0  # Normalize pixel values between 0 and 1
            img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension for batch
            model = keras.models.load_model("AppleFruit")
            prediction = model.predict(img_array)
            class_label = "Hibiscus With Disease" if prediction[0][0] < 0.5 else "Healthy Hibiscus"
            return class_label
        # Provide the path to a new image for prediction
        new_image_path = r"img/image.jpg"
        prediction = predict_image(new_image_path)
        print("Prediction:", prediction)
    
    return render_template('result.html',pred=prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

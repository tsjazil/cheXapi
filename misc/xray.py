# Import necessary libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

# Load pre-trained ResNet50 model

# Function to preprocess image
# def preprocess_image(img_path):
#     img = image.load_img(img_path, target_size=(224, 224))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     return preprocess_input(img_array)

# Function to classify image
def classify_image(img_path):
model = tf.keras.applications.ResNet50(weights='imagenet')
    preprocessed_img = preprocess_image(img_path)
    predictions = model.predict(preprocessed_img)
    decoded_predictions = decode_predictions(predictions, top=1)[0]
    result = decoded_predictions[0][1]
    return result

# Test the classifier

# image_path = 'path_to_your_image.jpg'  # Provide the path to your image
# result = classify_image(image_path)
# print("Result:", result)

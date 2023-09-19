from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load the saved model
model = tf.keras.models.load_model('models/happysadmodel.h5')

@app.route('/predict', methods=['POST'])
def predict():
    image_file = request.files['image']
    if image_file:
        # Load and preprocess the image
        image = tf.image.decode_image(image_file.read())
        image = tf.image.resize(image, (256, 256))
        image = image / 255.0  # Normalize pixel values
        image = np.expand_dims(image, axis=0)  # Add batch dimension

        # Perform prediction
        prediction = model.predict(image)

        # Check prediction probability and print class label
        new_yhat = prediction[0][0]  # Assuming single prediction for binary classification
        if new_yhat > 0.5:
            predicted_class = 'sad'
        else:
            predicted_class = 'happy'

        result = {
            'prediction': predicted_class
        }
        return jsonify(result)
    else:
        return "No image file provided"

if __name__ == '__main__':
    app.run(debug=True)

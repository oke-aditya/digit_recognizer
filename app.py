from flask import Flask, render_template, request
import numpy as np
import cv2
import base64
import sys
import json

# Assign the html folder.
app = Flask(__name__, template_folder="templates")
print("App started")

# Render the index.html
@app.route('/')
def index():
    return render_template('index.html')

# Load the model
# Note that the model is loaded only once when the webpage is started.
# We do not reload the model everytime.

net = cv2.dnn.readNetFromONNX("model.onnx")

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)

# Handle the uploaded image
@app.route('/upload', methods=["POST"])
def upload():
    # Get the uploaded form
    d = request.form
    # Extract the data field
    data = d.get("data")
    # The first part of the string simply indicates 
    
    # what kind of file it is. So we extract only the data part. 
    data = data.split(',')[1]

    # Get base64 decoded 
    data = base64.decodebytes(data.encode())

    # Convert to numpy array
    nparr = np.frombuffer(data, np.uint8)

    # Read the image
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    
    # You can now actually replace these block with equivalent tensorflow / pytorch predict functions
    # They too will work. But for now sticking with cv2.

    # Create a 4D blob from image
    blob = cv2.dnn.blobFromImage(img, 1/255, (28, 28))

    # Run the model
    net.setInput(blob)

    # Get the output
    out = net.forward()

    # Get a class with a highest score
    out = softmax(out.flatten())
    classId = np.argmax(out)
    confidence = out[classId]

    # Print on server side
    print("classId: {} confidence: {}".format(classId, confidence), file=sys.stdout)

    # Return result as a json object
    return json.dumps({"success" : True, "class" : int(classId), "confidence": float(confidence)}), 200, 
    {"ContentType":"application/json"}


if __name__ == "__main__":
    app.run()









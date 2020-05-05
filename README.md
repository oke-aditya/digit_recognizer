# Digit Recognizer
Simple Flask App to recongize Handwrtten Digits.

Note while deploying and using I have used Heroku with Gunicorn server.

The model is a simple CNN architecture. It is converted to ONNX format for easy inference using opencv.
The model is in ONNX format. You can use tensorflow as well. Just load it properly using tensorflow.


# Running locally.

Clone the repo

``` git clone https://github.com/oke-aditya/digit_recognizer ```

Install the requirements.

``` pip install -r requirements.txt ```

And you are done. You can now use the entire codebase.

While developing use the flask server

``` python ./web_app.py ```

While deploying locally please use waitress by running

``` python ./serve_waitress.py ```






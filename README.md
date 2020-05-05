# Digit Recognizer
Simple Flask App to recongize Handwrtten Digits.
Note while deploying and using I have used Heroku with Gunicorn server. It is wsgi and production ready.


# Running locally.

Clone the repo

``` git clone https://github.com/oke-aditya/digit_recognizer ```

Install the requirements.

``` pip install -r requirements.txt ```

And you are done. You can now use the entire codebase.

While developing use the flask server

``` python ./web_app.py ```

While deploying locally please use waitress by running

``` python ./server_waitress.py ```

The model is in ONNX format. You can use tensorflow as well. Just load it properly using tensorflow.




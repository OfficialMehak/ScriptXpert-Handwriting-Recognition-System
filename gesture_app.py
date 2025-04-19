import tensorflow as tf
import logging

# Suppress TensorFlow logs
tf.get_logger().setLevel('ERROR')  # Only show errors, suppress warnings and info logs
logging.getLogger('tensorflow').setLevel(logging.ERROR)  # Another way to suppress TensorFlow warnings

import sys
import os

# Suppress Pygame's output
sys.stderr = open(os.devnull, 'w')

import warnings

# Suppress all warnings from Keras, TensorFlow, etc.
warnings.filterwarnings("ignore")

import logging

# Set up logging to write to a file instead of printing to the console
logging.basicConfig(filename='app.log', level=logging.ERROR)  # Change the level to ERROR to ignore warnings



from flask import Flask, redirect, url_for, render_template, Response
import cv2
import numpy as np
from VirtualPainter import VirtualPainter


app = Flask(__name__)
app.register_blueprint(VirtualPainter, url_prefix="")

@app.route("/")
def home():
    with app.app_context():
        return render_template("index.html")

@app.route("/feature")
def feature():
    return render_template("feature.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)

from flask import Flask, render_template, request, redirect, url_for
from functions import create_table
app = Flask (__name__)

# create tablet



if __name__ == '__main__':
    app.run(debug=True)
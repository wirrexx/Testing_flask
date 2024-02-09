from flask import Flask, render_template, request, redirect, url_for
from functions import create_table, index
app = Flask (__name__)

# create tablet
@app.route('/')
def start():
    create_tab = index()
    return create_tab

if __name__ == '__main__':
    app.run(debug=True)
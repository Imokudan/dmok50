# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # This probably determines the name of the app

@app.route("/")                # This "routes" the app to /?
def hello_world():
    print(__name__)            # Prints the "__name__" in the terminal
    return "No hablo queso!"   # Returns this text on the website

app.run()                      # Runs the actual app
                

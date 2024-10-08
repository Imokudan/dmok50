# Clyde 'Thluffy' Sinclair
# SoftDev
# October 2024

# import conventions:
# list most general first (standard python library)
# ...then pip installs (eg Flask)
# ...then your own home-rolled modules/packages (today's test module)

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

import testmod0

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
 * Some will work as written;
 *  ...other sections will not. 

TASK:
 Predict which.
 1. Devise simple tests to isolate components/behaviors.
 2. Execute your tests.
 3. Process results.
 4. Findings yield new ideas for more tests? Yes: do them.

PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    #print("\n\n\n")
    #print("***DIAG: this Flask obj ***")
    #print(app)
        #Return <Flask 'app'>
    #print("***DIAG: request obj ***")
    #print(request)
        #Returns <Request 'http://localhost:5000/' [GET]>
    #print("***DIAG: request.args ***")
    #print(request.args)
        #Returns an empty dictionary called ImmutableMultiDict
    #print("***DIAG: request.args['username']  ***") 
    #print(request.args['username'])
        #Errors, there is no key named username in the ImmutableMultiDict
    #print("***DIAG: request.headers ***")
    #print(request.headers)
        #Gives header info of the website
    return render_template( 'login.html' )


@app.route("/auth") # , methods=['GET', 'POST'])
def authenticate():
    #print("\n\n\n")
    #print("***DIAG: this Flask obj ***")
    #print(app)
        #Return <Flask 'app'>
    #print("***DIAG: request obj ***")
    #print(request)
        #Returns 127.0.0.1 - - [07/Oct/2024 23:43:48] "GET /auth?username=wahoo!&sub1=Submit HTTP/1.1" 200 -
    #print("***DIAG: request.args ***")
    #print(request.args)
        #Returns a dictionary called ImmutableMultiDict, this time with the button text input and the submit button input
        #ImmutableMultiDict([('username', 'wahoo!'), ('sub1', 'Submit')])
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
        #Returns the value of the 'username' key
        #wahoo!
    #print("***DIAG: request.headers ***")
    #print(request.headers)
        #Gives header info of the website
    return "Waaaa hooo HAAAH"  #response to a form submission


    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

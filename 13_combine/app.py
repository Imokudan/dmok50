# Danny Mok
# Cerulean Calm: Danny, Alex, Colyi
# SoftDev
# Sep 2024

from flask import Flask, render_template
app = Flask(__name__)

f = open("data/occupations.csv", "r").read()
f = f.split("\n")[1:-1] # Turns data into list
    
flist = []
    
for i in f:
    i = i.split(",")
    i = ",".join(i).replace('"',"")
    flist.append(i)

@app.route("/")
def fxn():
    return render_template( 'tablified.html', foo="fooooo", collection=flist)

if __name__ == "__main__":
    app.debug = True
    app.run()

app.run()
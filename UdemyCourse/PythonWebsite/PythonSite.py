from flask import Flask, render_template

app=Flask(__name__)

#Homepage route
@app.route('/')
#Runs the home.html file in the templates folder
def home():
    return render_template("home.html")

#About page route
@app.route('/about/')
#Runs the about.html file in the templates folder
def about():
    return render_template("about.html")

#Runs application
if __name__ == "__main__":
    app.run(debug=True)
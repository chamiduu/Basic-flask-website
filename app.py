from flask import Flask
app = Flask(__name__)

#Home page
@app.route("/")
@app.route("/home")
def home():
    return "<h1>This is the Home Page and I loves contributing for SCORELAB.</h1>"

#About page
@app.route("/about")
def about():
    return "<h1>This is the about page and I loves contributing for SCORELAB</h1>"

#Contact page
@app.route("/contact")
def contact():
    return "<h1>This is the contact page and I loves contributing for SCORELAB</h1>"


if __name__ == '__main__':
    app.run(debug=True)

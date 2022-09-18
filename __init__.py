from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/contact')
def bio():
    return render_template('contact.html')

@app.route('/map')
def renderMap():
    return redirect("http://104.168.218.142:8123/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
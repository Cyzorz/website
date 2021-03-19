from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/home/contact')
def bio():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
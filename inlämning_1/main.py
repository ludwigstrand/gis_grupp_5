from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/iss")
def iss():
    return render_template("iss_spacestation.html")
    
if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "This app was deployed using a devOps pipeline"

if __name__=="__main__":
    app.run(host = "0.0.0.0", port=5000)

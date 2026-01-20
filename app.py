from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "This app was deployed using a DevOps pipeline."

if __name__ == "__main__":
  app.run(debug=True)
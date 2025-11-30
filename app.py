from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Secure DevSecOps Demo!"

if __name__ == "__main__":
    app.run(host="73.223.3.48", port=5000)

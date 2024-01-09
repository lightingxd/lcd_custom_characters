from flask import Flask, render_template

app = Flask(__name__, template_folder="template")

@app.route("/")
def htmlgenerator():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
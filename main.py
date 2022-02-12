from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add")
def add():
    a = int(request.args.get("sothunhat"))
    b = int(request.args.get("sothuhai"))
    return str(a + b)

if __name__ == "__main__":
    app.run()

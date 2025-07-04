from flask import Flask, render_template, request

'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface)
'''

# WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the website</h1></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# ✅ Form page that collects the name and greets the user
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name", "Guest")
        return f"Hello {name}!"
    return render_template("form.html")

# ✅ Optional: If you still want a separate submit route
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form.get("name", "Guest")
        return f"Hello {name}!"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)

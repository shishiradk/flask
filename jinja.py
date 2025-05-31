from flask import Flask, render_template, request, redirect, url_for

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

@app.route('/about')
def about():
    return render_template("about.html")

# ✅ Form to submit a name
@app.route('/submit-name', methods=['GET', 'POST'])
def submit_name():
    if request.method == 'POST':
        name = request.form.get('name', '')
        return f'Hello {name}!'
    return render_template("form.html")

# ✅ Simple pass/fail result page
@app.route('/success/<int:score>')
def success(score):
    res = "Passed" if score >= 50 else "Failed"
    return render_template("result.html", results=res)

# ✅ Detailed response with dictionary
@app.route('/successres/<int:score>')
def successres(score):
    res = "Passed" if score >= 50 else "Failed"
    exp = {'score': score, 'res': res}
    return render_template("result1.html", results=exp)

# ✅ Result passed directly
@app.route('/successif/<int:score>')
def successif(score):
    return render_template("result.html", results=score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template("result.html", results=score)

# ✅ Final subject score form
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        try:
            subjects = ['maths', 'science', 'c', 'datascience']
            total_score = 0
            for subject in subjects:
                score = int(request.form.get(subject, 0))
                total_score += score

            average_score = total_score / len(subjects)
            return redirect(url_for('successres', score=int(average_score)))
        except (ValueError, KeyError):
            return "Please enter valid numeric scores for all subjects."

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)

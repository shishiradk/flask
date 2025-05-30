from flask import Flask

'''
it creates an instance of the flask class,
which will be your WsGI(Web Server Gateway Interface)
'''

##WSGI Application
app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><h1>Welcome to the website</h1></html>"

@app.route("/index")
def index():
    return "Welcome to the index page"


if __name__=="__main__" :
    app.run(debug =True)

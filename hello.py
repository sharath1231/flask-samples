# This is a basic flask application

# import flask
from flask import Flask

# initialize a flask app
app = Flask(__name__)

# create a default route at '/'
# This is called a GET request. Other types of requests that will be useful are PUT, POST, DELETE.
@app.route('/')
def hello():
    return "Hello World!"

# TODO: write a function with endpoint '/user' and parameter as username and return => 'hello user' when we hit the endpoint.
'''
 What this exercise teaches you:
    1. how to add endpoints in flask. 
    2. how to add parameters in a web url.
'''
@app.route ('/user/<username>')
def hellouser(username):
    return "Hello " + username
if __name__ == '__main__':
    app.run()

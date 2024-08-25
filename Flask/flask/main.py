from flask import Flask, jsonify, request, render_template_string

app=Flask(__name__)

##http://127.0.0.1:5000/
@app.route("/")
def index():
    return "<h1>Hello</h1>"

##http://127.0.0.1:5000/name/Tapan
@app.route("/name/<name>")
def index1(name:str):
    return f"<h1>Hello {name}!</h1>"

#http://127.0.0.1:5000/json
@app.route("/json")
def json():
    return jsonify({"message":"hello"})

#http://127.0.0.1:5000/home
#http://127.0.0.1:5000/home/Tapan
@app.route("/home",methods=['GET','POST'],defaults={'name':"DEFAULT"})
@app.route("/home/<name>",methods=['GET','POST'])
def home(name:str):
    return f"<h1>Hello {name} ! You are on the home page</h1>"


#http://127.0.0.1:5000/query?name=Tapan&location=India
@app.route("/query")
def query():
    name=request.args.get("name")
    location=request.args.get("location")
    return f"<h1>Hello {name} you are from {location}! and welcome to the query page</h1>"


# Route for displaying the form
@app.route('/form', methods=['GET'])
def display_form():
    return render_template_string('''
        <h1>Fill out the form</h1>
        <form method="POST" action="/submit">
            Name: <input type="text" name="name"><br>
            Email: <input type="email" name="email"><br>
            <input type="submit" value="Submit">
        </form>
    ''')


@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')

    # Format and display the submitted data
    return render_template_string(f'''
        <h1>Form Submitted</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Email:</strong> {email}</p>
        <a href="/form">Go back to the form</a>
    ''')

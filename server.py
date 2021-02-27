from flask import Flask, render_template, request, redirect  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def hello_world():
    return "Server Online"

@app.route('/success')
def success():
    print('All the hax are belong to us.')
    return 'HAX SUCCESSFUL'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def deliver404(path):
    return 'Sorry! No response. Try again'


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)

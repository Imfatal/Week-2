#importing libraries
from flask import Flask, render_template, request
from serial_handler import send_command

app = Flask(__name__)

#runs the function below when someone visits the webpage
@app.route('/', methods=['GET', 'POST'])
def index():
    #an input is taken from the user and accordingly a command is sent to the esp32.py script which then sends a response back
    #and that response is stored in the "message varaible"and gets displayed on the webpage
    message = ""
    if request.method == 'POST':
        if 'on' in request.form:
            message = send_command('ON')
        elif 'off' in request.form:
            message = send_command('OFF')
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)

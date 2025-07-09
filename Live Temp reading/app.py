#importing the necessary libraries
from flask import Flask, render_template
from serial_reader import read_serial_data, get_latest_data
import threading

app = Flask(__name__)

#to run tasks in parallel, so we can read temperature data and serve web requests simultaneously 
threading.Thread(target=read_serial_data, daemon=True).start()

#When someone visits the web, the below function runs
@app.route("/")
def index():
    #value from get_latest_data() from serial_reader.py gets stored in "value"
    value = get_latest_data()
    #render the index.html script in templates folder and passes the "value to it"
    return render_template("index.html", sensor_value=value)

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)

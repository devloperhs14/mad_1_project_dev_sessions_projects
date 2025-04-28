# This code creates a simple Flask web application that accepts user input and displays it along with the current timestamp.

from flask import Flask, render_template, request
from datetime import datetime

# create Flask app
app = Flask(__name__)

# define route
@app.route('/', methods=['GET', 'POST'])
def index():
    value = ''
    timestamp = ''
    if request.method == 'POST':
        value = request.form['input_value']
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', value=value, timestamp=timestamp)

if __name__ == '__main__':
    app.run(debug=True)

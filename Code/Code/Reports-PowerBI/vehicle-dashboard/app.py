from flask import Flask, render_template, redirect, url_for, request
import pandas as pd

app = Flask(__name__)

# Sample route data (you could replace this with your ML model output or PostgreSQL query)
sample_data = [
    {
        "VehicleID": "VH001",
        "Driver": "John Doe",
        "Origin": "Warehouse A",
        "Destination": "Customer 1",
        "EstimatedTime": "10:30 AM",
        "Route": "Warehouse A -> Customer 1"
    },
    {
        "VehicleID": "VH002",
        "Driver": "Jane Smith",
        "Origin": "Warehouse B",
        "Destination": "Customer 3",
        "EstimatedTime": "11:15 AM",
        "Route": "Warehouse B -> Customer 2 -> Customer 3"
    },
    {
        "VehicleID": "VH003",
        "Driver": "Amit Singh",
        "Origin": "Warehouse C",
        "Destination": "Customer 5",
        "EstimatedTime": "12:00 PM",
        "Route": "Warehouse C -> Customer 4 -> Customer 5"
    }
]

@app.route('/pages/dashboard')
def dashboard():
    return render_template("dashboard.html", routes=sample_data)

@app.route('/', methods=['GET', 'POST'])
def login():
    print('test')
    if request.method == 'POST':
    # Process form data (e.g., check credentials)
     return redirect(url_for('dashboard'))  # Redirect after POST
    
    return render_template('login-form.html')  # Show login form

if __name__ == '__main__':
    app.run(debug=True)

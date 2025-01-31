# from flask import Flask, jsonify
# import random
# import datetime
# import pandas as pd

# app = Flask(__name__)

# # Dummy data for the analytics
# def generate_dummy_data():
#     today = datetime.date.today()
#     data = {
#         "dates": [(today - datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)],
#         "new_members": [random.randint(5, 20) for _ in range(7)],
#         "active_members": [random.randint(50, 100) for _ in range(7)],
#         "inactive_members": [random.randint(10, 50) for _ in range(7)],
#         "top_contributors": [{"user": f"User{i}", "messages": random.randint(20, 100)} for i in range(1, 6)],
#         "spam_reports": [random.randint(0, 5) for _ in range(7)],
#         "peak_activity": {f"{hour}:00": random.randint(10, 50) for hour in range(24)}
#     }
#     return data

# dummy_data = generate_dummy_data()

# # 1. New Members Joined
# @app.route('/new_members', methods=['GET'])
# def new_members():
#     response = {"dates": dummy_data["dates"], "new_members": dummy_data["new_members"]}
#     return jsonify(response)

# # 2. Active vs Inactive Members
# @app.route('/active_vs_inactive', methods=['GET'])
# def active_vs_inactive():
#     response = {
#         "dates": dummy_data["dates"],
#         "active_members": dummy_data["active_members"],
#         "inactive_members": dummy_data["inactive_members"]
#     }
#     return jsonify(response)

# # 3. Top Contributors
# @app.route('/top_contributors', methods=['GET'])
# def top_contributors():
#     response = {"top_contributors": dummy_data["top_contributors"]}
#     return jsonify(response)

# # 4. Spam Reports
# @app.route('/spam_reports', methods=['GET'])
# def spam_reports():
#     response = {"dates": dummy_data["dates"], "spam_reports": dummy_data["spam_reports"]}
#     return jsonify(response)

# # 5. Peak Activity Time
# @app.route('/peak_activity', methods=['GET'])
# def peak_activity():
#     response = {"peak_activity": dummy_data["peak_activity"]}
#     return jsonify(response)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, jsonify
import random
import datetime

app = Flask(__name__)

# Dummy data for analytics
def generate_dummy_data():
    today = datetime.date.today()
    return {
        "dates": [(today - datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)],
        "new_members": [random.randint(5, 20) for _ in range(7)],
        "active_members": [random.randint(50, 100) for _ in range(7)],
        "inactive_members": [random.randint(10, 50) for _ in range(7)],
        "top_contributors": [{"user": f"User{i}", "messages": random.randint(20, 100)} for i in range(1, 6)],
        "spam_reports": [random.randint(0, 5) for _ in range(7)],
        "peak_activity": {f"{hour}:00": random.randint(10, 50) for hour in range(24)}
    }

dummy_data = generate_dummy_data()

# API endpoints for JSON responses
@app.route('/new_members', methods=['GET'])
def new_members():
    return jsonify({"dates": dummy_data["dates"], "new_members": dummy_data["new_members"]})

@app.route('/active_vs_inactive', methods=['GET'])
def active_vs_inactive():
    return jsonify({
        "dates": dummy_data["dates"],
        "active_members": dummy_data["active_members"],
        "inactive_members": dummy_data["inactive_members"]
    })

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", data=dummy_data)

if __name__ == '__main__':
    app.run(debug=True)

# Data_Analyst_Assignment
# Submitted By: - Sagar Purswani (purswanisagar60@gmail.com)
# Admin Dashboard for Telegram Group Analytics
# Project Overview
This project is a Flask-based web dashboard for analyzing Telegram group data. It provides key insights and visualizations to help group admins monitor activity, engagement, and trends using various analytics.

The project follows a structured folder format, includes logging, visualization endpoints, and an interactive dashboard, and supports Docker deployment for scalability.

# Folder Structure
├── logs/  
│   ├── app.log               # Logs for application processes  
│   ├── error.log             # Logs for errors encountered  
├── app.py                    # Main Flask application  
├── config.py                 # Configuration settings  
├── code_file.py              # Main logic for analytics and visualizations  
├── Dockerfile                # Instructions for containerizing the app  
├── README.md                 # Project documentation  
├── requirements.txt          # Python dependencies  

Features & Functionalities
Admin Dashboard UI with clickable buttons to view analytics
Multiple Analytics & Visualizations (bar charts, pie charts, line graphs, etc.)
Endpoints to Fetch Analytics using Flask API
Logging Mechanism to track errors and system operations
Docker Compatibility for easy deployment

Analytics Included
This project includes 20 analytics ideas and 30 dashboard visualizations, documented in a separate Docx file (analytics.docx).

The document contains:
20 Analytics Ideas (each with a name, description, purpose,benefit and code)
30 Dashboard Analytics & Visualizations (how they help group admins)

How to Run the Project
1️ Install Dependencies
Ensure you have Python installed, then run:
pip install -r requirements.txt

2️ Run Flask Application
python app.py
The app will start on http://127.0.0.1:5000/

3️ View Dashboard
Go to http://127.0.0.1:5000/ in your browser to access the dashboard.

4️ View Visualizations
Click on the buttons to view different analytics. Example:
Messages Per Group
Active Members
Message Trends

5️ Check Logs
If any errors occur, check:
logs/app.log  
logs/error.log  

Contributors
Developer: Sagar Purswani
Date: January 2025

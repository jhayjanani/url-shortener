🔗 URL Shortener Web Application

A simple and efficient URL Shortener web application built using Python Flask and MySQL. The application converts long URLs into short, easy-to-share links and redirects users to the original URL when accessed.

The project was initially developed using a local MySQL database and later enhanced by integrating a cloud-based MySQL database (Railway) and deploying the application on Render.

🚀 Live Demo

🌐 Application:
https://url-shortener-ttha.onrender.com

📌 Features

- Convert long URLs into short URLs
- Redirect short URLs to the original URL
- Store URL mappings in MySQL database
- Track the number of clicks for each shortened URL
- Prevent duplicate short URLs for the same long URL
- Cloud database integration
- Deployed live using Render

🛠️ Tech Stack

Backend

- Python
- Flask

Database

- MySQL
- Railway Cloud MySQL

Deployment & Tools

- Render (Web Deployment)
- Git & GitHub
- Environment Variables (.env)

🏗️ Project Workflow

1. User enters a long URL.
2. Flask application generates a unique short URL using:
   - SHA256 hashing
   - Base64 encoding
3. URL mapping is stored in the MySQL database.
4. When the short URL is opened:
   - The original URL is retrieved.
   - User is redirected to the destination URL.
   - Click count is updated.

📂 Project Structure

url-shortener/
│
├── app.py              # Flask application
├── database.py         # Database configuration
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend page
│
├── static/
│   └── style files
│
└── README.md

⚙️ Local Setup Instructions

1. Clone the repository

git clone https://github.com/jhayjanani/url-shortener.git

2. Create virtual environment

python -m venv venv

3. Activate virtual environment

Windows:

venv\Scripts\activate

4. Install dependencies

pip install -r requirements.txt

5. Configure Environment Variables

Create a ".env" file:

DB_HOST=your_database_host
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_NAME=your_database_name
DB_PORT=your_database_port

6. Run the application

python app.py

Open:

http://127.0.0.1:5000

☁️ Deployment

The application is deployed using:

- Railway → Cloud MySQL Database
- Render → Flask Web Application Hosting

Environment variables were configured in Render for secure database connectivity.

📚 Learning Outcomes

Through this project, I gained practical experience in:

- Building web applications using Flask
- Connecting backend applications with databases
- Managing cloud databases
- Using environment variables for security
- Deploying applications to cloud platforms
- Working with Git and GitHub workflows


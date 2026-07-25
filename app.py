from flask import Flask, render_template, request, redirect
import hashlib
import base64
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MySQL Connection
# MySQL Connection
connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    port=int(os.getenv("DB_PORT", 3306))
)



cursor = connection.cursor(buffered=True)

# Generate Short URL using SHA256 + Base64
def generate_short_url(long_url):
    hash_object = hashlib.sha256(long_url.encode())
    short_hash = base64.urlsafe_b64encode(hash_object.digest())[:6].decode()
    return short_hash


# Home Page
@app.route("/", methods=["GET", "POST"])
def home():

    short_url = None

    if request.method == "POST":

        long_url = request.form["long_url"]

        # Check whether the URL already exists
        check_query = """
        SELECT short_url
        FROM url_mapping
        WHERE long_url = %s
        """

        cursor.execute(check_query, (long_url,))
        existing_entry = cursor.fetchone()

        if existing_entry:

            short_url = existing_entry[0]

        else:

            # Generate Short URL
            short_url = generate_short_url(long_url)

            insert_query = """
            INSERT INTO url_mapping (long_url, short_url)
            VALUES (%s, %s)
            """

            cursor.execute(insert_query, (long_url, short_url))
            connection.commit()

    return render_template("index.html", short_url=short_url)


# Redirect Short URL
@app.route("/<short_url>")
def redirect_url(short_url):

    # Increase Click Count
    update_query = """
    UPDATE url_mapping
    SET clicks = clicks + 1
    WHERE short_url = %s
    """

    cursor.execute(update_query, (short_url,))
    connection.commit()

    # Get Original URL
    select_query = """
    SELECT long_url
    FROM url_mapping
    WHERE short_url = %s
    """

    cursor.execute(select_query, (short_url,))
    result = cursor.fetchone()

    if result:
        return redirect(result[0])

    return "<h2>404 - Short URL Not Found</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
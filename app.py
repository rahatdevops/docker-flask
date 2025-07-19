import psycopg2
from flask import Flask

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(
        dbname="mydb",
        user="user",
        password="password",
        host="localhost"
    )

@app.route("/")
def home():
    try:
        conn = connect_db()
        conn.close()
        return "Connected to DB!"
    except Exception as e:
        return f"Failed to connect: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


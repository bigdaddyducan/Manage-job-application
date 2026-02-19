import sqlite3
from flask import Flask, render_template
app = Flask(__name__)

headings = ("Company","Title","Status")

def get_db_connection():
    conn = sqlite3.connect('JobTrackDB.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
   conn = get_db_connection()
   columns = [row[1] for row in conn.execute("PRAGMA table_info(JobApps)")]
   selected_columns = [column for column in columns if column != 'id']
   query = f"SELECT {', '.join(selected_columns)} FROM JobApps"
   data = conn.execute(query)
   return render_template('index.html', headings=headings, data=data)
if __name__ == '__main__':
   app.run()
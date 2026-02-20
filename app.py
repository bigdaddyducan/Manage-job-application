import sqlite3
from flask import Flask, render_template
app = Flask(__name__)

headings = ("Company","Title","Status")

def get_db_connection():
    conn = sqlite3.connect('JobTrackDB.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_applied_count():
   conn = get_db_connection()
   applied = conn.execute("SELECT COUNT(*) from JobApps WHERE status = 'Applied'").fetchone()[0]
   conn.close()
   return applied

def get_rejected_count():
   conn = get_db_connection()
   rejected = conn.execute("SELECT COUNT(*) from JobApps WHERE status = 'Rejected'").fetchone()[0]
   conn.close()
   return rejected

def get_interviewed_count():
   conn = get_db_connection()
   interviewed = conn.execute("SELECT COUNT(*) from JobApps WHERE status = 'Interviewed'").fetchone()[0]
   conn.close()
   return interviewed

@app.route('/')
def home():
   conn = get_db_connection()
   columns = [row[1] for row in conn.execute("PRAGMA table_info(JobApps)")]
   selected_columns = [column for column in columns if column != 'id']
   query = f"SELECT {', '.join(selected_columns)} FROM JobApps"
   data = conn.execute(query)
   applied = get_applied_count()
   rejected = get_rejected_count()
   interviewed = get_interviewed_count()

   return render_template('index.html', headings=headings, data=data,applied=applied,rejected=rejected,interviewed=interviewed)
if __name__ == '__main__':
   app.run()
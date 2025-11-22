import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="project",
        user="postgres",
        password=os.getenv("DB_PASSWORD")   # 從 .env 讀取密碼
    )

def get_user_by_national_id(national_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM users WHERE national_id = %s", (national_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user
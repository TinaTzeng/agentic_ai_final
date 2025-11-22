from werkzeug.security import generate_password_hash
from database.db import get_db_connection

def create_user(national_id, password, name):
    conn = get_db_connection()
    cur = conn.cursor()
    
    password_hash = generate_password_hash(password)

    cur.execute("""
        INSERT INTO users (national_id, password_hash, name)
        VALUES (%s, %s, %s)
    """, (national_id, password_hash, name))

    conn.commit()
    cur.close()
    conn.close()
    print("使用者建立成功！")


create_user("A123456789", "test1234", "測試用戶")
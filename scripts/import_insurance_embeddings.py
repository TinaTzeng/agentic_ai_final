import csv
import ast
import psycopg2
from psycopg2.extras import execute_batch

CSV_FILE = "insurance_rag_data.csv"   # ← 你的 CSV 檔名
TABLE_NAME = "insurance_embeddings"   # ← 你的資料表名稱（記得要先建好）
''' 先在資料庫建立table:
CREATE TABLE insurance_embeddings (
    id TEXT PRIMARY KEY,
    text TEXT,
    context_text TEXT,
    policy_name TEXT,
    metadata_file TEXT,
    type TEXT,
    embedding vector(768)
);
'''


# PostgreSQL 連線資訊（你可用 .env 或手動填）
DB_CONFIG = {
    "host": "localhost",
    "database": "project",
    "user": "postgres",
    "password": "postgres",
}


def load_csv_rows():
    """讀取 CSV 並回傳全部列資料（使用 DictReader）"""
    rows = []
    with open(CSV_FILE, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        print("👉 偵測到的欄位:", reader.fieldnames)

        for idx, row in enumerate(reader, start=1):
            try:
                # 轉換 embedding 文字 → list[float]
                embedding = ast.literal_eval(row["embedding"])

                rows.append({
                    "id": row["id"],
                    "text": row["text"],
                    "context_text": row["context_text"],
                    "policy_name": row["policy_name"],
                    "metadata_file": row["metadata_file"],
                    "type": row["type"],
                    "embedding": embedding,
                })

            except Exception as e:
                print(f"⚠️ 第 {idx} 行發生錯誤，將跳過: {e}")

    return rows


def insert_embeddings(rows):
    """批次寫入 PostgreSQL（使用 pgvector）"""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    sql = f"""
        INSERT INTO {TABLE_NAME}
        (id, text, context_text, policy_name, metadata_file, type, embedding)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
    """

    data = [
        (
            r["id"],
            r["text"],
            r["context_text"],
            r["policy_name"],
            r["metadata_file"],
            r["type"],
            r["embedding"]
        )
        for r in rows
    ]

    print("📥 開始寫入資料庫...")
    execute_batch(cur, sql, data, page_size=100)
    conn.commit()

    print(f"✅ 完成寫入 {len(rows)} 筆資料")
    cur.close()
    conn.close()


if __name__ == "__main__":
    print("📘 開始匯入 CSV → PostgreSQL (pgvector)")

    rows = load_csv_rows()
    print(f"📄 成功讀取 {len(rows)} 筆資料")

    insert_embeddings(rows)

    print("🎉 全部完成！")
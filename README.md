- 下載專案
  
  git clone https://github.com/TinaTzeng/agentic_ai_final.git
  
  cd agentic_ai_final
  
- 建立虛擬環境（venv）＋ 安裝套件
  
  python -m venv venv
  
  source venv/bin/activate   # Windows：venv\Scripts\activate
  
  pip install -r requirements.txt
  
- 建立資料庫(postgres)
  
  host: localhost
  
  database: project
  
  user: postgres
  
  password: postgres
  
- 建立資料表
  
  執行：database/create_tables.sql
  
- 建立測試帳號
  
  執行 python database/create_user.py
  
- 啟動Flask網站
  
  python app.py
  
  打開 http://localhost:8000
  

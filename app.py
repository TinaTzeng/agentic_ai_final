from flask import Flask, render_template, request, redirect, session
from werkzeug.security import check_password_hash
from database.db import get_user_by_national_id
from flask import jsonify

app = Flask(__name__)
app.secret_key = "supersecretkey"   # session 必須使用 secret key

# -------------------------
# 登入頁
# -------------------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        national_id = request.form["national_id"]
        password = request.form["password"]

        # 從資料庫查詢使用者
        user = get_user_by_national_id(national_id)

        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            session["national_id"] = user["national_id"]
            return redirect("/chat")

        return render_template("login.html", error="帳號或密碼錯誤！")

    return render_template("login.html")


# -------------------------
# 聊天頁（登入後才可進入）
# -------------------------
@app.route("/chat")
def chat_page():
    if "user_id" not in session:
        return redirect("/")
    return render_template("chat.html")

# 聊天api
@app.route("/chat_api", methods=["POST"])
def chat_api():
    data = request.json
    user_message = data.get("message", "")

    # 之後會改成 multi-agent 回覆
    reply = f"收到你的訊息：{user_message}"

    return jsonify({"reply": reply})

# -------------------------
# 啟動 Flask 伺服器
# -------------------------
if __name__ == "__main__":
    app.run(debug=True, port=8000)
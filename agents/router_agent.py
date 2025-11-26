# 多代理協作中樞（Router Agent）

def route_intent_to_agent(user_input: str, session_context: Dict[str, Any]):
    # 根據使用者輸入與目前對話狀態，決定要交給哪個 Agent 處理。
    # 串接多個 Agent（例如：查保單條款 → 判斷資格 → 計算金額）
    # 組合成最後要回給使用者的答案
    return


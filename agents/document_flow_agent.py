# 文件與流程引導 Agent

def generate_required_documents(event_type: str, policy_type: str | None = None):
    # 產生文件清單：根據「事故類型 + 保單類型」告訴使用者需要哪些文件
    return

def guide_claim_process(event_type: str, policy_type: str | None = None):
    # 申請流程引導：例如「住院 → 出院 → 拿診斷書 → 收據 → 上傳 → 送出申請」
    return

def suggest_next_step(current_stage: str):
    # 流程說明：告訴使用者下一步要做什麼
    return
# agents/__init__.py
"""
保險理賠 Multi-Agent 系統的 Agent 模組集合。
之後若需要在這裡做共用設定或共用常數，可以集中放在此。
"""

# 方便其他模組直接 from agents import xxx
from .data_validation_agent import (
    verify_identity,
    process_uploaded_documents,
    validate_documents,
)
from .policy_lookup_agent import (
    get_policy_list,
    query_policy_details,
    answer_policy_qa,
)
from .document_flow_agent import (
    generate_required_documents,
    guide_claim_process,
    suggest_next_step,
)
from .eligibility_agent import (
    check_eligibility,
    calculate_claim_amount,
    explain_non_eligibility,
    evaluate_claim,
)
from .progress_agent import (
    get_claim_status,
    get_claim_result_summary,
)
from .router_agent import route_intent_to_agent
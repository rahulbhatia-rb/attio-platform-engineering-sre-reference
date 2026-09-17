from app.slo import Window, evaluate
def admit_release(image: str, window: Window, target: float) -> dict:
    if "@sha256:" not in image: return {"admitted": False, "reason": "image_digest_required"}
    state=evaluate(window,target)
    if state["burned"]: return {"admitted": False, "reason": "error_budget_exhausted", "slo": state}
    return {"admitted": True, "reason": "policy_satisfied", "slo": state}

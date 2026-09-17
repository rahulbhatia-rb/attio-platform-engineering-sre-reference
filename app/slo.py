from dataclasses import dataclass

@dataclass(frozen=True)
class Window:
    good: int
    total: int

def evaluate(window: Window, target: float) -> dict:
    if window.total < 1 or window.good < 0 or window.good > window.total: raise ValueError("invalid event counts")
    if not 0 < target < 1: raise ValueError("target must be between zero and one")
    availability = window.good / window.total
    allowed_bad = window.total * (1 - target)
    bad = window.total - window.good
    return {"availability": availability, "target": target, "bad_events": bad,
            "budget_remaining": max(0.0, allowed_bad - bad), "burned": bad > allowed_bad}

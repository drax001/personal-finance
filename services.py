import os, requests

def convert_amount(amount: float, frm: str, to: str) -> dict:
    api = os.getenv("EXCHANGE_RATE_API", "https://api.exchangerate.host/latest")
    r = requests.get(api, params={"base": frm, "symbols": to}, timeout=10)
    r.raise_for_status()
    rate = r.json().get("rates", {}).get(to, 1.0)
    return {"rate": rate, "converted": amount * rate}

import os, requests

BANK_API_KEY = os.getenv("BANK_API_KEY")

def verify_user(iin):
    # Mock verification call
    url = "https://zamanbank.kz/api/verify"
    headers = {"Authorization": f"Bearer {BANK_API_KEY}"}
    # For demo, simulate success if last digit even
    if int(iin[-1]) % 2 == 0:
        return True
    return False


import jwt
import time

def get_token():
    KEY_ID = "9JWW26X9GC"
    PRIVATE_KEY_PATH = "/Users/till/Desktop/AppStore Connect API Test/AuthKey_9JWW26X9GC.p8"

    with open(PRIVATE_KEY_PATH, 'r') as f:
        PRIVATE_KEY = f.read()

    now = int(time.time())

    payload = {
        "iss": "de38698d-e5cc-400b-bda1-11bec52f55ee",
        "iat": now,
        "exp": now + 1200,  # 20 minutes
        "aud": "appstoreconnect-v1",
        "scope": [
            "GET /v1/apps",
            "GET /v1/apps/6673915598/analyticsReportRequests"

            # Nur mit diesem zusätzlichen Eintrag funktioniert es nicht mehr,
            # auch wenn der Request selbst nicht geändert wird.
            #, "POST /v1/analyticsReportRequests"
        ]
    }

    token = jwt.encode(
        payload,
        PRIVATE_KEY,
        algorithm="ES256",
        headers={
            "kid": KEY_ID,
            "typ": "JWT"
        }
    )

    return token.decode('utf-8')
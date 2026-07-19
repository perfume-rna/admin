# ------------------------------
# Token generation & verification
# ------------------------------

from itsdangerous import URLSafeSerializer
from secrets import token_urlsafe, token_hex

serializer = URLSafeSerializer(secret_key=token_hex(16))

def verify_token(token: str) -> bool:
    if not token:
        return False
    try:
        serializer.loads(token, salt="websocket_token", max_age=3600)
        return True
    except Exception:
        return False

def generate_token() -> str:
    return serializer.dumps(token_urlsafe(16), salt="websocket_token")

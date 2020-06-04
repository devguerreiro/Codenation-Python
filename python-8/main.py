from jwt import encode as jwt_encode, decode as jwt_decode
from jwt.exceptions import InvalidSignatureError

KEY = "acelera"


def create_token(data: dict, secret: str) -> str:
    return jwt_encode(payload=data, key=secret)


def verify_signature(token: str) -> dict:
    try:
        return jwt_decode(jwt=token, key=KEY, algorithms=["HS256"])
    except InvalidSignatureError:
        return {"error": 2}

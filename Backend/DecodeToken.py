import jwt
from .settings import SECRET_KEY

def decode_token(token):
    UserId = jwt.decode(token.split()[1],SECRET_KEY,algorithms=['HS256'])['user_id']
    return UserId
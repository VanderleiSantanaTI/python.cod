import jwt
import datetime
from datetime import datetime, timedelta, timezone
import time


secret_key = 'vanderlei'

# Função para criar um token JWT com expiração
def create_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.now() + timedelta(seconds=19)  # Expiração em 19 segundos
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

# Função para decodificar um token JWT
def decode_token(token):
    try:
        decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        return 'Token expirado'
    except jwt.InvalidTokenError:
        return 'Token inválido'

# Exemplo de uso
if __name__ == "__main__":
    # Crie um token para um usuário fictício com ID 123
    token = create_token(123)
    print(f'Token: {token}')
    time.sleep(20)
    # #Tente decodificar o token
    result = decode_token(token)
    print(f'Resultado da decodificação: {result}')

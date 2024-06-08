from fastapi import FastAPI, Request, HTTPException
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

# Inicialize o FastAPI e o Limiter
app = FastAPI()
limiter = Limiter(key_func=get_remote_address)

# Adicione o middleware de rate limiting
app.state.limiter = limiter
app.add_exception_handler(429, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)


# Defina a rota com limite de taxa
@app.get("/items/")
@limiter.limit("10/minute")  # Limite de 5 requisições por minuto por IP
async def read_items(request: Request):
    return {"message": "This is a rate limited route"}


# Defina outra rota para teste
@app.get("/open/")
async def open_route(request: Request):
    return {"message": "This route is not rate limited"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

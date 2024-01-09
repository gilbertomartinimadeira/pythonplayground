import uvicorn
from fastapi import FastAPI
from redis_om import get_redis_connection, HashModel
from fastapi.middleware.cors  import CORSMiddleware
from starlette.requests import Request
import requests

# Replace these values with your Redis server configuration
redis_host = 'localhost'
redis_port = 6379
redis_db = 0
redis_password = 'admin'  # Leave it empty if there is no password

    # Example usage
    # redis_connection.set('minha_chave', 'meu_valor')
    # value = redis_connection.get('my_key')
    #print(f'The value of my_key is: {value}')

app = FastAPI()


app.add_middleware(CORSMiddleware, 
                   allow_origins=['http://localhost:3000'],
                   allow_methods=['GET','POST', 'DELETE'],
                   allow_headers=['*'])

# this should be a differente database
redis_connection = get_redis_connection(host=redis_host, port=redis_port,db=redis_db)

class Order(HashModel):
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str #pending, completed, refunded
    class Meta:
        database = redis_connection

@app.post("/orders")
async def create(request: Request): #id, quantity
    body = await request.json()

    try:
        req = requests.get(f'http://localhost:8000/products/{body["id"]}')
        return req.json()
    except Exception as e:
        print(e)
        return e
    
    



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000) 
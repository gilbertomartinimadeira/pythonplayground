from fastapi import FastAPI
from redis_om import get_redis_connection,HashModel
from fastapi.middleware.cors  import CORSMiddleware
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
                   allow_methods=['*'],
                   allow_headers=['*'])

redis_connection = get_redis_connection(host=redis_host, port=redis_port,db=redis_db)
    
class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis_connection

@app.get("/products")
def all():
    return Product.all_pks()

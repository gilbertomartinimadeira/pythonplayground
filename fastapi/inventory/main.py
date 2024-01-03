from fastapi import FastAPI
from redis_om import get_redis_connection

# Replace these values with your Redis server configuration
redis_host = 'localhost'
redis_port = 6379
redis_db = 0
redis_password = 'admin'  # Leave it empty if there is no password


# Set up the Redis configuration
redis_config = {
    'host': redis_host,
    'port': redis_port,
    'db': redis_db,
    'password': redis_password,
}

app = FastAPI()


@app.get("/")
async def root():
    test_connection()
    return {"Hello": "Gilberto","numeros":[1,2,3,4,5]}

def test_connection():
    # Get a connection to the Redis database
    redis_connection = get_redis_connection(host=redis_host, port=redis_port,db=redis_db)

    # Example usage
    redis_connection.set('my_key', 'my_value')
    value = redis_connection.get('my_key')
    print(f'The value of my_key is: {value}')

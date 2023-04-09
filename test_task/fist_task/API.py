from fastapi import FastAPI, Query
import redis

app = FastAPI()

db = redis.StrictRedis(host='redis', port=6379, db=0)


#Запрос на проверку адреса
@app.get('/check_data')
def get_address(phone: str):
    return db.get(phone)


#Запрос на запись пары "телефон" и "адрес"
@app.post('/write_data')
def post_data(phone: str = Query(regex="^\d{11}$"), address: str = Query()):
    db.set(phone, address)
    return "success"


#Запрос на изменение адреса
@app.put('/write_data')
def put_data(phone: str, address: str):
    db.set(phone, address)
    return db.get(phone)

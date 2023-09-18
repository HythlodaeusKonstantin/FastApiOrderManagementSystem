from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx
import uvicorn
import json
import requests
from requests.auth import HTTPBasicAuth
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi import Request

app = FastAPI(
    title="OrdersManagementsSystem"
)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

class AuthData(BaseModel):
    login: str
    password: str


class ProductObject(BaseModel):
   productUID: str
   quantity: int

class OrderData(BaseModel):
    addressUID: str
    date: str
    products: list[ProductObject]
    comment: str

class AddressData(BaseModel):
    addressName: str

APP_URL = "https://mint-daily-longhorn.ngrok-free.app/"
#APP_URL = "http://127.0.0.1"


@app.get("/")
def hello():
    return "Hello world!"
  

@app.post("/token")
def create_token(item: AuthData):
    uri = APP_URL + '/BaseProduction/hs/rest/token'
    responce = httpx.get(uri, auth=(item.login, item.password))
    if responce.status_code == 200:
       JSON = responce.json()
       return JSONResponse(content=json.dumps(JSON), status_code=200)
    else:
        return JSONResponse(content="{token: null}", status_code=responce.status_code)
    

@app.post('/orders')
def create_order(request: Request, item: OrderData):
    token = request.headers.get("authorization").replace("Bearer ", "")
    if token is not None:
        OrderDataDict = dict()
        OrderDataDict['addressUID'] = item.addressUID
        OrderDataDict['date'] = item.date
        OrderDataDict['comment'] = item.comment

        productsTemp = list()
        for product in item.products:
            ProductObject = dict()
            ProductObject['productUID'] = product.productUID
            ProductObject['quantity'] = product.quantity
            productsTemp.append(ProductObject)
        OrderDataDict['products'] = productsTemp
             
        JSONData = json.dumps(OrderDataDict, ensure_ascii=False)

        uri = APP_URL + '/BaseProduction/hs/rest/orders'
        responce = httpx.post(uri, headers={"Authorization" : "Bearer " + token}, data=JSONData)
        if responce.status_code == 201:
            OrdersData = responce.json()
            OrdersDataJSON = json.dumps(OrdersData, ensure_ascii=False)
            return JSONResponse(OrdersDataJSON, status_code=201)
        else: 
            return JSONResponse("{status: not authorized}",status_code=401)
    else:
        return JSONResponse("{status: not authorized}",status_code=401)
    

@app.post('/address')
def create_order(request: Request, item: AddressData):
    token = request.headers.get("authorization").replace("Bearer ", "")
    if token is not None:
        AddressDataDict = dict()
        AddressDataDict['addressName'] = item.addressName
         
        JSONData = json.dumps(AddressDataDict, ensure_ascii=False)

        uri = APP_URL + '/BaseProduction/hs/rest/address'
        responce = httpx.post(uri, headers={"Authorization" : "Bearer " + token}, data=JSONData)
        if responce.status_code == 201:
            AddressData = responce.json()
            OrdersDataJSON = json.dumps(AddressData, ensure_ascii=False)
            return JSONResponse(OrdersDataJSON, status_code=201)
        else: 
            return JSONResponse("{status: not authorized}",status_code=401)
    else:
        return JSONResponse("{status: not authorized}",status_code=401)


@app.get('/orders')
def get_orders(request: Request):
    token = request.headers.get("authorization").replace("Bearer ", "")
    if token is not None:
        uri = APP_URL + '/BaseProduction/hs/rest/orders'
        responce = httpx.get(uri, headers={"Authorization" : "Bearer " + token})
        if responce.status_code == 200:
            OrdersData = responce.json()
            OrdersDataJSON = json.dumps(OrdersData, ensure_ascii=False)
            return JSONResponse(OrdersDataJSON, status_code=200)
        else: 
            return JSONResponse("{status: not authorized}",status_code=401)
    else:
        return JSONResponse("{status: not authorized}",status_code=401)
    

@app.get('/shipments')
def get_shipments(request: Request):
    token = request.headers.get("authorization").replace("Bearer ", "")
    if token is not None:
        uri = APP_URL + '/BaseProduction/hs/rest/shipments'
        responce = httpx.get(uri, headers={"Authorization" : "Bearer " + token})
        if responce.status_code == 200:
            OrdersData = responce.json()
            OrdersDataJSON = json.dumps(OrdersData, ensure_ascii=False)
            return JSONResponse(OrdersDataJSON, status_code=200)
        else: 
            return JSONResponse("{status: not authorized}",status_code=401)
    else:
        return JSONResponse("{status: not authorized}",status_code=401)
 

@app.get('/products')
def get_products(request: Request):
    token = request.headers.get("authorization").replace("Bearer ", "")
    if token is not None:
        uri = APP_URL + '/BaseProduction/hs/rest/products'
        responce = httpx.get(uri, headers={"Authorization" : "Bearer " + token})
        if responce.status_code == 200:
            OrdersData = responce.json()
            OrdersDataJSON = json.dumps(OrdersData, ensure_ascii=False)
            return JSONResponse(OrdersDataJSON, status_code=200)
        else: 
            return JSONResponse("{status: not authorized}",status_code=401)
    else:
        return JSONResponse("{status: not authorized}",status_code=401)
    

@app.get('/partners')
def get_partners(request: Request):
    token = request.headers.get("authorization").replace("Bearer ", "")
    if token is not None:
        uri = APP_URL + '/BaseProduction/hs/rest/partners'
        responce = httpx.get(uri, headers={"Authorization" : "Bearer " + token})
        if responce.status_code == 200:
            OrdersData = responce.json()
            OrdersDataJSON = json.dumps(OrdersData, ensure_ascii=False)
            return JSONResponse(OrdersDataJSON, status_code=200)
        else: 
            return JSONResponse("{status: not authorized}",status_code=401)
    else:
        return JSONResponse("{status: not authorized}",status_code=401)
    

@app.get('/address')
def get_address(request: Request):
    token = request.headers.get("authorization").replace("Bearer ", "")
    if token is not None:
        uri = APP_URL + '/BaseProduction/hs/rest/address'
        responce = httpx.get(uri, headers={"Authorization" : "Bearer " + token})
        if responce.status_code == 200:
            OrdersData = responce.json()
            OrdersDataJSON = json.dumps(OrdersData, ensure_ascii=False)
            return JSONResponse(OrdersDataJSON, status_code=200)
        else: 
            return JSONResponse("{status: not authorized}",status_code=401)
    else:
        return JSONResponse("{status: not authorized}",status_code=401)
    

@app.get('/userinfo')
def get_userinfo(request: Request):
    token = request.headers.get("authorization").replace("Bearer ", "")
    if token is not None:
        uri = APP_URL + '/BaseProduction/hs/rest/userinfo'
        responce = httpx.get(uri, headers={"Authorization" : "Bearer " + token})
        if responce.status_code == 200:
            OrdersData = responce.json()
            OrdersDataJSON = json.dumps(OrdersData, ensure_ascii=False)
            return JSONResponse(OrdersDataJSON, status_code=200)
        else: 
            return JSONResponse("{status: not authorized}",status_code=401)
    else:
        return JSONResponse("{status: not authorized}",status_code=401)


from fastapi import FastAPI, HTTPException
from database.connectToDatabase import db_connect
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from query import net_view, net_add, net_delete, net_modify, net_show, ip_add, ip_delete, ip_modify, ip_view, ip_show
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome! Please use one of the following functions to manage your IP address table or network table: show, add, mod, del or view"}


#There is a manager for IP


@app.get("/ip/mod")
async def ip_mod(ip, used, comment):
    result = await ip_modify(ip, used, comment)
    raise HTTPException( status_code = result['status'], detail = result['message'])

@app.get("/ip/del")
async def ip_del(ip):
    result = await ip_delete(ip)
    raise HTTPException( status_code = result['status'], detail = result['message'])

@app.get("/ip/add")
async def add_ip(ip, used, comment):
    result = await ip_add(ip, used, comment)
    raise HTTPException( status_code = result['status'], detail = result['message'])

@app.get("/ip/show")
async def show_ip(ip):
    result = await ip_show(ip)
    print(result)
    raise HTTPException( status_code = result['status'], detail = result['message'])

@app.get("/ip/view")
async def view_ip():
    return await ip_view()

#There is a manager for NETWORKS



@app.get("/net/mod")
async def net_mod(net, active, comment):
    result = await net_modify(net, active, comment)
    raise HTTPException( status_code = result['status'], detail = result['message'])

@app.get("/net/del")
async def net_del(net):
    result = await net_delete(net)
    raise HTTPException( status_code = result['status'], detail = result['message'])

@app.get("/net/add")
async def add_net(net, active, comment):
    result = await net_add(net, active, comment)
    raise HTTPException( status_code = result['status'], detail = result['message'])

@app.get("/net/show")
async def show_net(net):
    result = await net_show(net)
    print(result)
    raise HTTPException( status_code = result['status'], detail = result['message'])

@app.get("/net/view")
async def view_net():
    return await net_view()


register_tortoise(
    app,
    db_url='mysql://admin2:5E1f!bEtTQN@127.0.0.1:3307/ipmanager',
    modules={'models': ['app.models_def']},
    generate_schemas=True,
    add_exception_handlers=True,
)

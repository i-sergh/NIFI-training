from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from random import randint

app = FastAPI(
    title = 'NIFI'
    )



@app.get('/')
async def start_page():
    return {'ping': 'pong'}


@app.post('/')
async def secret_number():
    return  {'number':  randint(0, 1000)}
    
@app.get('/redirect')
async def redirect_test():
    
    return RedirectResponse('http://localhost:8181/nifi-api/flow/about', status_code=303)
 
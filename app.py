# /app.py
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse

app = FastAPI()

# middleware function
@app.middleware("http")
async  def modify_request_response_middleware(request: Request, call_next):
    # intercept and  modify the incoming request
    request.scope["path"] = str(request.url.path).replace("api", "apiv2")
    # process modified request
    response = await call_next(request)
    # transform the outgoing response
    if isinstance(response, StreamingResponse):
        response.headers["X-Custom-Header"] = "Modified"
    return response

@app.get("/info")
async def hello():
    return {"message": "Hello, World!"}

@app.get("/apiv2/info")
async  def hellov2():
    return {"message": "Hello, World from V2"}
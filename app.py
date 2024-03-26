# /app.py
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from datetime import datetime, timedelta
import time
from fastapi.testclient import TestClient


# rate limiting
class RateLimitingMiddleware(BaseHTTPMiddleware):
    # rate limiting configs
    RATE_LIMIT_DURATION = timedelta(minutes=1)
    RATE_LIMIT_REQUESTS = 3

    def __init__(self, app):
        super().__init__(app)
        # Dict to store request counts for each IP
        self.request_counts = {}

    async def dispatch(self, request, call_next):
        # get client IP
        client_ip = request.client.host

        # check if IP is already preswnt in request_counts
        request_count, last_request = self.request_counts.get(client_ip, (0, datetime.min))

        # calculate time elapsed since last request
        elapsed_time = datetime.now() - last_request

        if elapsed_time  > self.RATE_LIMIT_DURATION:
            # if elapsed time is greater than the rate limit duration, reset the count
            request_count = 1
        else:
            if request_count >= self.RATE_LIMIT_REQUESTS:
                # If the request count exceeds the rate limit, return a JSON response with an error message
                return JSONResponse(
                    status_code=429,
                    content={"message": "Rate limit exceeded. Please try again later."}
                )
            request_count +=1

        # update the request count and last request timestatmp for the IP
        self.request_counts[client_ip] = (request_count, datetime.now())

        # proceed with request
        response = await call_next(request)

        return response

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

app.add_middleware(RateLimitingMiddleware)

@app.get("/info")
async def hello():
    return {"message": "Hello, World!"}

@app.get("/apiv2/info")
async  def hellov2():
    return {"message": "Hello, World from V2"}


# tests

client = TestClient(app)
def test_modify_request_response_middleware():
    # send a GET request to the hello endpoint
    response = client.get("/info")
    # assert the middleware has ben applied
    assert response.status_code ==  200
    # assert the middleware has  been applied
    assert response.headers.get("X-Custom-Header") == "Modified"
    # assert the response content
    assert response.json() == {"message": "Hello, World!"}

def test_rate_limiting_middleware():
    time.sleep(1)
    response = client.get("/info")

    # assert the response code is  200
    assert response.status_code == 200

    time.sleep(1)
    response = client.get("/info")
    assert  response.status_code == 200

    time.sleep(1)
    response = client.get("/info")
    # assert the response code is  429 after request limit is  reached
    assert response.status_code == 429
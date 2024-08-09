from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)


class NumberRequest(BaseModel):
    number: int

def generateTriangle(number: int) -> str:
    str_number = str(number)
    result = [] 

    for i in range (len(str_number)):
        line = str_number[i] + '0' * i
        result.append(line)
    return '\n'.join(result)

def generateOddNumber(max_number : int) -> str:
    odd_numbers = [str(i) for i in range(1, max_number + 1, 2)]
    return ', '.join(odd_numbers)

def generatePrimeNumber(max_number : int) -> str:
    primes = []
    for num in range(2, max_number + 1):
        is_prime = all(num % i != 0 for i in range(2, int(num**0.5) + 1))
        if is_prime:
            primes.append(str(num))
    return ', '.join(primes)

@app.post("/generate-triangle")
async def generate_triangle_endpoint(data: NumberRequest):
    if data.number < 0:
        raise HTTPException(status_code=400, detail="Number must be positive")
    result = generateTriangle(data.number)
    return {"result": result}

# @app.get("/generate-triangle")
# AFTER THIS

@app.post("/generate-odd-number")
async def generate_odd_number_endpoint(data: NumberRequest):
    if data.number < 0:
        raise HTTPException(status_code=400, detail="Number must be positive")
    result = generateOddNumber(data.number)
    return {"result": result}

@app.post("/generate-prime-number")
async def generate_prime_number_endpoint(data: NumberRequest):
    if data.number < 0:
        raise HTTPException(status_code=400, detail="Number must be positive")
    result = generatePrimeNumber(data.number)
    return {"result": result}

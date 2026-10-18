import asyncio
import time
from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CalcRequest(BaseModel):
    numbers: List[Union[int, float]]
    delays: List[Union[int, float]]


class OneResult(BaseModel):
    number: Union[int, float]
    square: Union[int, float]
    delay: Union[int, float]
    time: float


class CalcResponse(BaseModel):
    results: List[OneResult]
    total_time: float
    parallel_faster_than_sequential: bool


async def calc_sqare(number, delay):
    start = time.time()
    await asyncio.sleep(delay)
    res = number * number
    end = time.time()
    return OneResult(number=number, square=res, delay=delay, time=round(end - start, 2))


@app.post("/calculate/", response_model=CalcResponse)
async def calculate(data: CalcRequest):
    start = time.time()

    tasks = []
    for i in range(len(data.numbers)):
        tasks.append(asyncio.create_task(calc_sqare(data.numbers[i], data.delays[i])))

    reslts = await asyncio.gather(*tasks)

    total = round(time.time() - start, 2)
    sequential = sum(data.delays)

    return CalcResponse(
        results=reslts,
        total_time=total,
        parallel_faster_than_sequential=total < sequential,
    )

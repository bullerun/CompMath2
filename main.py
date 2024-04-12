from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from core import get_solution, check_interval
from fastapi.responses import FileResponse

app = FastAPI()
origins = [
    "http://localhost:8000",
    "http://localhost:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class NonlinearEquations(BaseModel):
    equation: int
    a: float
    b: float
    eps: float
    method: int
    inFile: bool


@app.post("/")
def create_nonlinear_equations(nonlinear_equations: NonlinearEquations):
    print(nonlinear_equations)
    if nonlinear_equations.method == 4 or check_interval(nonlinear_equations.a, nonlinear_equations.b,
                                                        nonlinear_equations.equation):
        if nonlinear_equations.inFile:
            get_solution(fun_num=nonlinear_equations.equation,
                         interval=(nonlinear_equations.a, nonlinear_equations.b),
                         eps=nonlinear_equations.eps, method=nonlinear_equations.method,
                         in_file=nonlinear_equations.inFile)
            return FileResponse("1.txt", media_type="text/plain;charset=UTF-8")
        return get_solution(fun_num=nonlinear_equations.equation,
                            interval=(nonlinear_equations.a, nonlinear_equations.b),
                            eps=nonlinear_equations.eps, method=nonlinear_equations.method,
                            in_file=nonlinear_equations.inFile)
    else:
        return {"error": "На интервале либо нет корней, либо их больше одного"}

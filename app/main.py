from fastapi import FastAPI

from service.any_kind_of_service import Teacher

app = FastAPI()

@app.get("/add_teacher/{tg_id}/{name}")
async def root(tg_id: int, name: str):
    return Teacher.add_teacher(tg_id = tg_id, name = name)

@app.get("/get_teacher/{tg_id}")
async def say_hello(tg_id: int):
    return Teacher.get_teacher(tg_id=tg_id)

@app.get("/update_teacher/{tg_id}")
async def update(tg_id: int):
    return Teacher.update_teacher(tg_id=tg_id)

@app.get("/del_teacher/{tg_id}")
async def delet(tg_id: int):
    return Teacher.del_teacher(tg_id=tg_id)
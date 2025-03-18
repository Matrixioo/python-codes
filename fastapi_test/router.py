from typing import Annotated
from fastapi import APIRouter, Depends
from rep import TaskRepository
from schemas import MTaskAdd, MTask


router = APIRouter(
    prefix="/tasks",
    tags=['tasks'],
)

@router.post("")
async def add_task(
        task: Annotated[MTaskAdd, Depends()]
):
    task_id = await TaskRepository.add_one(task)
    return {"s": True, "task_id": task_id}

@router.get("")
async def get_tasks() -> list[MTask]:
    tasks = await TaskRepository.get_all()
    return tasks
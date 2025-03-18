from databaswe import new_session, TasksTable
from schemas import MTaskAdd, MTask
from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_one(cls, data: MTaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TasksTable(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id


    @classmethod
    async def get_all(cls) -> list[MTask]:
        async with new_session() as session:
            query = select(TasksTable)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_schemas = [MTask.model_validate(task_model) for task_model in task_models]
            return task_schemas
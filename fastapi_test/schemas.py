from pydantic import BaseModel, ConfigDict

class MTaskAdd(BaseModel):
    name: str
    description: str | None

class MTask(MTaskAdd):
    id: int

    model_config = ConfigDict(from_attributes = True)
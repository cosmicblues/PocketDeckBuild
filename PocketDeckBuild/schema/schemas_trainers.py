from pydantic import BaseModel


class Trainer(BaseModel):
    id: int
    name: str
    effect: str


class TrainerCreate(BaseModel):
    id: int
    name: str
    effect: str


class TrainerUpdate(BaseModel):
    id: int
    name: str
    effect: str


class TrainerInDB(Trainer):
    """A class containing pydantic data validation for in database Pizza model."""

    id: int

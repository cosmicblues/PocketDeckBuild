from dataclasses import dataclass, asdict
from typing import Union
from dataclasses import dataclass, asdict
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from schema.schemas import Pokemon
from api.trainer_json import list_trainers
from api.util.utils import get_db
from api.trainers_routes.getAllTrainers import router
from api.schema.schemas import TrainerInDB, TrainerCreate
from api.model.crud.crud import Crud2

#===========================POST============================
@router.post("/trainers", response_model=TrainerInDB)
def create_trainer(trainer: TrainerCreate, dbb: Session = Depends(get_db)):
    return Crud2.create_trainer(dbb, trainer)
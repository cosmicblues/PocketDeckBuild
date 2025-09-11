from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from PocketDeckBuild.database.database import get_db
from PocketDeckBuild.loader import trainers_list
from PocketDeckBuild.model.crud.trainers_crud import SqlTrainerCRUD as Crud2
from PocketDeckBuild.schema.schemas_trainers import Trainer, TrainerInDB

router = APIRouter()
# ===========================GET============================


@router.get("/trainers/{pid}", response_model=TrainerInDB)
def read_trainers_id(pid: int, dbb: Session = Depends(get_db)) -> Trainer:
    if pid not in trainers_list:
        raise HTTPException(status_code=404, detail="Ce trainer n'existe pas")

    return Crud2.get_trainer_by_id_if_exists(pid, dbb)
    # return Trainer(**list_trainers[id])


@router.get("/trainers", response_model=List[TrainerInDB])
def read_trainers(dbb: Session = Depends(get_db)):
    # print(Crud2.get_trainers(dbb=dbb))
    return Crud2.get_trainer(dbb=dbb)

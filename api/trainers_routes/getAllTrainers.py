from dataclasses import dataclass, asdict
from typing import Union, List
from dataclasses import dataclass, asdict
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from schema.schemas import Trainer
from api.trainer_json import list_trainers
from api.model.models import Trainer_table
from api.schema.schemas import TrainerInDB, TrainerCreate, TrainerUpdate
from api.model.crud.crud import Crud2
from api.util.utils import get_db, get_trainer_by_id_if_exists

router = APIRouter()
#===========================GET============================

@router.get("/trainers/{pid}", response_model=TrainerInDB)
def read_trainers_id(pid: int, dbb: Session = Depends(get_db)) -> Trainer :

    if pid not in list_trainers :
        raise HTTPException(status_code=404, detail="Ce trainer n'existe pas")
   
    return get_trainer_by_id_if_exists(pid, dbb)
    #return Trainer(**list_trainers[id])

@router.get("/trainers", response_model=List[TrainerInDB])
def read_trainers(dbb: Session = Depends(get_db)):
    #print(Crud2.get_trainers(dbb=dbb))
    return Crud2.get_trainer(dbb=dbb)
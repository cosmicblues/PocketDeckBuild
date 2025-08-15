#from dataclasses import dataclass, asdict
#from typing import Union
from dataclasses import dataclass, asdict
from fastapi import APIRouter, HTTPException, Path, Depends
from sqlalchemy.orm import Session
from schema.schemas import Trainer
from api.trainer_json import list_trainers
#import models.Pokemon_table
from api.trainers_routes.getAllTrainers import router
from api.model.crud.crud import Crud2
from api.schema.schemas import TrainerInDB
from api.util.utils import get_db, get_trainer_by_id_if_exists

#===========================DELETE============================
@router.delete("/trainers/{pid}", response_model=TrainerInDB)
def delete_trainer(pid: int, dbb: Session = Depends(get_db)):
    get_trainer_by_id_if_exists(pid, dbb)
    return Crud2.delete_trainer(dbb, pid)
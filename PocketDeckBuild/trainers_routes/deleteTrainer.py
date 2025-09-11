# from dataclasses import dataclass, asdict
# from typing import Union
from fastapi import Depends
from sqlalchemy.orm import Session

from PocketDeckBuild.database.database import get_db
from PocketDeckBuild.model.crud.trainers_crud import SqlTrainerCRUD as Crud2
from PocketDeckBuild.schema.schemas_trainers import TrainerInDB

# import models.Pokemon_table
from PocketDeckBuild.trainers_routes.getAllTrainers import router


# ===========================DELETE============================
@router.delete("/trainers/{pid}", response_model=TrainerInDB)
def delete_trainer(pid: int, dbb: Session = Depends(get_db)):
    Crud2.get_trainer_by_id_if_exists(pid, dbb)
    return Crud2.delete_trainer(dbb, pid)

from fastapi import Depends
from sqlalchemy.orm import Session

from PocketDeckBuild.model.crud.trainers_crud import SqlTrainerCRUD as Crud2
from PocketDeckBuild.schema.schemas_trainers import TrainerCreate, TrainerInDB
from PocketDeckBuild.trainers_routes.getAllTrainers import router
from PocketDeckBuild.util.utils import get_db


# ===========================POST============================
@router.post("/trainers", response_model=TrainerInDB)
def create_trainer(trainer: TrainerCreate, dbb: Session = Depends(get_db)):
    return Crud2.create_trainer(dbb, trainer)

#from dataclasses import dataclass, asdict
#from typing import Union
from dataclasses import dataclass, asdict
from fastapi import APIRouter, HTTPException, Path, Depends
#from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
from api.trainer_json import list_trainers
from api.model.crud.crud import Crud2
from api.util.utils import get_db, get_trainer_by_id_if_exists
from api.trainers_routes.getAllTrainers import router
from api.schema.schemas import TrainerInDB, TrainerUpdate

#===========================PUT============================
@router.put("/trainers/{pid}", response_model=TrainerInDB)
def update_trainer(
    pid: int,
    trainer: TrainerUpdate,
    dbb: Session = Depends(get_db),
):
    prev_trainer = get_trainer_by_id_if_exists(pid, dbb)
    
    trainer_update = TrainerUpdate(
        trainer_id=pid,
        name=trainer.name if trainer.name else prev_trainer.name,
        effect=trainer.effect if trainer.effect else prev_trainer.effect,
    )
    return Crud2.update_trainer(dbb, trainer_update)
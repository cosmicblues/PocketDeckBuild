# from dataclasses import dataclass, asdict
# from typing import Union
from fastapi import Depends

# from sqlalchemy.orm import Session
from sqlalchemy.orm import Session

from PocketDeckBuild.database.database import get_db
from PocketDeckBuild.model.crud.trainers_crud import SqlTrainerCRUD as Crud2
from PocketDeckBuild.schema.schemas_trainers import TrainerInDB, TrainerUpdate
from PocketDeckBuild.trainers_routes.getAllTrainers import router


# ===========================PUT============================
@router.put("/trainers/{pid}", response_model=TrainerInDB)
def update_trainer(
    pid: int,
    trainer: TrainerUpdate,
    dbb: Session = Depends(get_db),
):
    prev_trainer = Crud2.get_trainer_by_id_if_exists(pid, dbb)

    trainer_update = TrainerUpdate(
        trainer_id=pid,
        name=trainer.name if trainer.name else prev_trainer.name,
        effect=trainer.effect if trainer.effect else prev_trainer.effect,
    )
    return Crud2.update_trainer(dbb, trainer_update)

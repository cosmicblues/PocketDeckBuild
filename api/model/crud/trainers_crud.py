from sqlalchemy.orm import Session

from api.model.models import Trainer_table
from api.schema.schemas import TrainerCreate, TrainerUpdate

class TrainerCRUD:
    """Abtract class defining all CRUD operations for Trainer model."""

    @staticmethod
    def get_trainers(dbb: Session):
        raise NotImplementedError

    @staticmethod
    def get_trainer_by_id(dbb: Session, id: int):
        raise NotImplementedError

    @staticmethod
    def create_trainer(dbb: Session, id: TrainerCreate):
        raise NotImplementedError

    @staticmethod
    def update_trainer(dbb: Session, trainer: TrainerUpdate):
        raise NotImplementedError

    @staticmethod
    def delete_trainer(dbb: Session, id: int):
        raise NotImplementedError
    
class SqlTrainerCRUD(TrainerCRUD):
    """A class containing SQL CRUD operations for Trainers model."""

    @staticmethod
    def get_trainer(dbb: Session):
        return dbb.query(Trainer_table).all()

    @staticmethod
    def get_trainer_by_id(dbb: Session, id: int):
        return dbb.query(Trainer_table).filter(Trainer_table.id == id).first()

    @staticmethod
    def create_trainer(dbb: Session, trainer: TrainerCreate):
        db_trainer = Trainer_table(**trainer.dict())
        dbb.add(db_trainer)
        dbb.commit()
        dbb.refresh(db_trainer)
        return db_trainer

    @staticmethod
    def update_trainer(dbb: Session, trainer: TrainerUpdate):
        trainer_in_db = SqlTrainerCRUD.get_trainer_by_id(dbb, Trainer_table.id)
        trainer_in_db.name = trainer.name
        trainer_in_db.effect = trainer.effect

        dbb.commit()
        return trainer_in_db

    @staticmethod
    def delete_trainer(dbb: Session, id: int):
        trainer = SqlTrainerCRUD.get_trainer_by_id(dbb, id)
        dbb.delete(trainer)
        dbb.commit()
        return trainer
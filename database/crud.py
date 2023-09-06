from . import models, schemas
from .database import Database

def get_token(token: str):
    return Database().session.query(models.AuthtokenToken).filter(models.AuthtokenToken.key == token).first()

def get_access(token: str):
    return Database().session.query(models.AuthUser).filter(models.AuthUser.id == token.user_id).first()

def get_data_from_object(oject: str):
    return Database().session.query(models.Tdata).filter(models.Tdata.object == oject).first()

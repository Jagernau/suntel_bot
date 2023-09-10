from . import models, schemas
from .database import Database
from sqlalchemy import and_, or_
def get_token(token: str):
    return Database().session.query(models.AuthtokenToken).filter(models.AuthtokenToken.key == token).first()

def get_access(token: str):
    return Database().session.query(models.AuthUser).filter(models.AuthUser.id == token.user_id).first()

def get_data_from_object(object_enter: str):
    return Database().session.query(models.Tdata, models.Twialon100, models.Tklient).\
            join(models.Twialon100, models.Twialon100.logintd == models.Tdata.login).\
            join(models.Tklient, models.Tklient.id == models.Twialon100.tkid).\
            join(models.Tagat, and_(
                models.Tagat.idsystem == models.Tdata.idsystem,
                models.Tagat.idobject == models.Tdata.idobject,
                models.Tdata.dimport.between(models.Tagat.dbeg, models.Tagat.dend)
                )).\
            filter(models.Tdata.object.like(f'%{object_enter}%')).first()


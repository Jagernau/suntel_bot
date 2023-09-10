from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Float, Boolean
from .database import Database

class Tdata(Database.BASE):
    __tablename__ = 'tdata'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    login = Column(String, nullable=True)
    idlogin = Column(String, nullable=True)
    idsystem = Column(Integer, nullable=True)
    object = Column(String, nullable=True)
    idobject = Column(String, nullable=True)
    isactive = Column(String, nullable=True)
    dimport = Column(DateTime, nullable=True)

class Temail(Database.BASE):
    __tablename__ = 'temail'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    email = Column(String, nullable=True)
    name = Column(String, nullable=True)
    inn = Column(String, nullable=True)
    kpp = Column(String, nullable=True)

class Tklient(Database.BASE):
    __tablename__ = 'tklient'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    shortname = Column(String, nullable=True)
    type = Column(String, nullable=True)
    inn = Column(String, nullable=True)
    kpp = Column(String, nullable=True)
    tarif = Column(Float(precision=2), nullable=True)

class Ttarif(Database.BASE):
    __tablename__ = 'ttarif'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    tkid = Column(BigInteger, nullable=True)
    tarif = Column(Float(precision=2), nullable=True)
    dbeg = Column(DateTime, nullable=True)
    dend = Column(DateTime, nullable=True)

class Twialon100(Database.BASE):
    __tablename__ = 'twialon100'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    klient = Column(String, nullable=True)
    login = Column(String, nullable=True)
    logintd = Column(String, nullable=True)
    tkid = Column(BigInteger, nullable=True)

class AuthtokenToken(Database.BASE):
    __tablename__ = 'authtoken_token'
    key = Column(String(40), primary_key=True)
    created = Column(DateTime, nullable=False)
    user_id = Column(Integer, nullable=False)


class AuthUser(Database.BASE):
    __tablename__ = 'auth_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    password = Column(String(128), nullable=False)
    last_login = Column(DateTime, nullable=False)
    is_superuser = Column(Boolean, nullable=False)
    username = Column(String(150), nullable=False)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(254), nullable=False)
    is_staff = Column(Boolean, nullable=False)
    is_active = Column(Boolean, nullable=False)
    date_joined = Column(DateTime, nullable=False)


class Tagat(Database.BASE):
    __tablename__ = 'tagat'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    object = Column(String, nullable=True)
    idobject = Column(String, nullable=True)
    shortname = Column(String, nullable=True)
    inn = Column(String, nullable=True)
    tarif = Column(Float(precision=2), nullable=True)
    idsystem = Column(Integer, nullable=True)
    kpp = Column(String, nullable=True)
    name = Column(String, nullable=True)
    dbeg = Column(DateTime, nullable=True)
    dend = Column(DateTime, nullable=True)

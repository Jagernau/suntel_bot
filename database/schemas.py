from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Float, MetaData, Table, Boolean

metadata = MetaData()

tagat = Table(
    "tagat", metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("object", String),
    Column("idobject", String),
    Column("shortname", String),
    Column("inn", String),
    Column("tarif", Float(precision=2)),
    Column("idsystem", BigInteger),
    Column("kpp", String),
    Column("name", String),
    Column("dbeg", DateTime),
    Column("dend", DateTime),
)

tdata = Table(
    "tdata", metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("login", String),
    Column("idlogin", String),
    Column("idsystem", Integer),
    Column("object", String),
    Column("idobject", String),
    Column("isactive", String),
    Column("dimport", DateTime),
)

temail = Table(
    "temail", metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("email", String),
    Column("name", String),
    Column("inn", String),
    Column("kpp", String),
)

tklient = Table(
    "tklient", metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("shortname", String),
    Column("type", String),
    Column("inn", String),
    Column("kpp", String),
    Column("tarif", Float(precision=2)),
)

ttarif = Table(
    "ttarif", metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("tkid", BigInteger),
    Column("tarif", Float(precision=2)),
    Column("dbeg", DateTime),
)

twialon100 = Table(
    "twialon100", metadata,
    Column("id", BigInteger, primary_key=True, autoincrement=True),
    Column("klient", String),
    Column("login", String),
    Column("logintd", String),
    Column("tkid", BigInteger),
)

authtoken_token = Table(
    "authtoken_token", metadata,
    Column("key", String),
    Column("created", DateTime),
    Column("user_id", Integer),
)

auth_user = Table(
    "auth_user", metadata,
    Column("id", Integer, primary_key=True),
    Column("password", String),
    Column("last_login", DateTime),
    Column("is_superuser", Boolean),
    Column("username", String),
    Column("first_name", String),
    Column("email", String),
    Column("is_staff", Boolean),
    Column("is_active", Boolean),
    Column("date_joined", DateTime),
)

from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import sessionmaker

# Cria o banco de dados e se conecta com ele - paralelo com conn do sqlite3
DATABASE_URL = "postgresql://adm:adm@localhost/escola"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind = engine)

Base = declarative_base()
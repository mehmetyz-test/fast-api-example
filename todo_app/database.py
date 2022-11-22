import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# L'url de notre base de donnes

SQLALCHEMY_DATABASE_URL = "sqlite:///./data.db"

# On cree la connection
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Pour creer un session locale a chaque nouvelle connexion
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
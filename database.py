from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'mysql+pymysql://dbUsername:dbPassword@localhost:3306/dbName'

engine = create_engine(URL_DATABASE)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


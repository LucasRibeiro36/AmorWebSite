from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Configure database connection mysql
DATABASE_URL = 'mysql+mysqlconnector://root:password@localhost:3306/amorweb'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

Base = declarative_base()


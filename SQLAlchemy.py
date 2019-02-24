from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Person(Base):
    __tablename__ = "person"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    username = Column('username', String, unique=True)
engine = create_engine('sqlite:///:memory:', echo=True)

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

session = Session()
user = User()
user.id = 0
user.username = 'alice'
session.add(user)
session.commit()

session.close()


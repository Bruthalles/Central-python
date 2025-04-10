from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:',echo=True)

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

    def __repr__(self):
        return f"Usuario(id={self.id},nome={self.nome}, idade={self.idade})"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

usuario1 = Usuario(nome='Raphael',idade=40)
usuario2 = Usuario(nome='Carol',idade=31)
session.add(usuario1)
session.add(usuario2)

session.commit()

usuarios = session.query(Usuario).all()
for usuario in usuarios:
    print(usuario)
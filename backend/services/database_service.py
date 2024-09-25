from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Load environment variables
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost:5432/valorant_db')

# Set up the database engine
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Define the base class for the models
Base = declarative_base()

# Define database models (tables)
class PlayerStats(Base):
    __tablename__ = 'player_stats'
    id = Column(Integer, primary_key=True)
    player_name = Column(String, nullable=False)
    match_id = Column(Integer, nullable=False)
    kills = Column(Integer, nullable=False)
    deaths = Column(Integer, nullable=False)
    assists = Column(Integer, nullable=False)
    economy_status = Column(Float, nullable=True)

# Create tables in the database
def init_db():
    Base.metadata.create_all(engine)

def add_player_stats(player_name, match_id, kills, deaths, assists, economy_status):
    new_stats = PlayerStats(
        player_name=player_name,
        match_id=match_id,
        kills=kills,
        deaths=deaths,
        assists=assists,
        economy_status=economy_status
    )
    session.add(new_stats)
    session.commit()

def get_player_stats(player_name):
    return session.query(PlayerStats).filter_by(player_name=player_name).all()

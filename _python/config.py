from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class WeatherData(Base):
    __tablename__ = 'weather_data'
    
    id = Column(Integer, primary_key=True)
    date = Column(String(10), nullable=False)
    temp_c = Column(Numeric(5,2))
    humidity = Column(Numeric(4,3))
    pressure = Column(Numeric(6,3))

class WeatherDataSession:
    def __init__(self, db_path="weather.db"):
        self.engine = create_engine(f"sqlite:///{db_path}")
        Base.metadata.create_all(self.engine)
        self.session = sessionmaker(bind=self.engine)
    
    def create_db(self):
        os.makedirs("weather", exist_ok=True)
        with open("weather/db.sqlite", "w+") as f:
            f.write("CREATE TABLE IF NOT EXISTS weather_data (id INTEGER PRIMARY KEY, date TEXT, temp_c NUMERIC, humidity REAL, pressure REAL)\n;")
    
    def get_weather(self, zone):
        # This is the actual logic for fetching data
        now = datetime.now(timezone.utc)
        current_time_in_local_time = now.astimezone(pytz.timezone(zone))
        time_str = f"{current_time_in_local_time.strftime('%Y-%m-%d %H:%M')} UTC"
        
        query
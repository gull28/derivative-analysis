from dotenv import load_dotenv
import os

class DBConfig:
    def __init__(self):
        self.username = os.getenv("DB_USERNAME")
        self.password = os.getenv("DB_PASSWORD")
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.name = os.getenv("DB_NAME")

    
    def getUrl(self) -> str:
        return f"postgres://{self.username}:{self.password}@{self.host}:${self.port}/{self.name}"
        

class APIConfig:
    def __init__(self):
        self.key = os.getenv("API_KEY")


class Config:
    def __init__(self):
        load_dotenv()
        self.db = DBConfig()
        self.api = APIConfig()
        

        
        

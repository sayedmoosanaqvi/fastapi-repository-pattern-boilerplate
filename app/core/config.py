from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # These are default values. If they aren't in a .env file, it uses these.
    PROJECT_NAME: str = "Wardrobe Tracker"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "sqlite:///./wardrobe.db"

    class Config:
        # This tells Pydantic: "Don't worry if the .env file is missing"
        env_file = ".env"
        case_sensitive = True

settings = Settings()
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Shit At League API"
    api_key: str
    games_per_player: int = 20

    class Config:
        env_file = ".env"


settings = Settings()

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # =========================
    # GEMINI
    # =========================

    gemini_api_key: str = Field(default="")

    gemini_flash_model: str = "gemini-2.5-flash"

    gemini_pro_model: str = "gemini-2.5-pro"

    # =========================
    # HUGGING FACE
    # =========================

    hf_token: str = Field(default="")

    image_model_id: str = "runwayml/stable-diffusion-v1-5"

    image_backend: str = "diffusers"

    # =========================
    # IMAGE
    # =========================

    image_width: int = 512

    image_height: int = 512

    image_steps: int = 25

    image_guidance_scale: float = 7.5

    image_seed: int = -1

    # =========================
    # APPLICATION
    # =========================

    app_host: str = "127.0.0.1"

    app_port: int = 8000

    debug: bool = True

    max_prompt_length: int = 2000

    @property
    def base_dir(self) -> Path:
        return Path(__file__).resolve().parent.parent

    @property
    def panels_dir(self) -> Path:
        return self.base_dir / "static" / "panels"

    @property
    def exports_dir(self) -> Path:
        return self.base_dir / "static" / "exports"


settings = Settings()
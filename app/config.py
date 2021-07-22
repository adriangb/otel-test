from pydantic import BaseSettings, Field


class OpenTelemetryConfig(BaseSettings):
    exporter_otlp_endpoint: str

    class Config:
        env_prefix: str = "OTEL_"

class AppConfig(BaseSettings):
    otel: OpenTelemetryConfig = Field(default_factory=OpenTelemetryConfig)

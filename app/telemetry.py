from app.config import AppConfig
from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor


def configure_otel(config: AppConfig, app: FastAPI):
    tracer_provider = TracerProvider()
    trace.set_tracer_provider(tracer_provider)
    tracer_provider.add_span_processor(
        BatchSpanProcessor(
            OTLPSpanExporter(
                endpoint=config.otel.exporter_otlp_endpoint
            )
        )
    )
    FastAPIInstrumentor.instrument_app(app, tracer_provider=tracer_provider)

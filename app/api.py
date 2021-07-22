import asyncio

from fastapi import APIRouter
from opentelemetry import trace

tracer = trace.get_tracer_provider().get_tracer(__name__)

api = APIRouter()


@api.get("/")
async def root():
    with tracer.start_as_current_span("foo"):
        await asyncio.sleep(0.1)

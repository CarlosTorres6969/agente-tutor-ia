import os
from dotenv import load_dotenv

from agno.agent import Agent
from agno.models.openai.like import OpenAILike

load_dotenv()


def _get_secret(key: str, default: str | None = None) -> str | None:
    value = os.getenv(key)
    if value:
        return value
    try:
        import streamlit as st
        return st.secrets.get(key, default)
    except (ImportError, RuntimeError, KeyError):
        return default


def _crear_agente():
    api_key = _get_secret("GROQ_API_KEY")
    model = _get_secret("GROQ_MODEL") or "llama-3.3-70b-versatile"

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY no encontrada. "
            "Configúrala en los secrets de Streamlit Cloud "
            "o en el archivo .env para ejecución local."
        )

    return Agent(
        name="Tutor IA",
        model=OpenAILike(
            id=model,
            base_url="https://api.groq.com/openai/v1",
            api_key=api_key,
        ),
        instructions=[
            "Responde siempre en español.",
            "Explica el tema de forma sencilla.",
            "Da un ejemplo.",
            "Adapta la explicación al nivel del estudiante.",
            "Finaliza con una pregunta de evaluación.",
        ],
        markdown=True,
    )


def crear_agente_tutor():
    return _crear_agente()

from langchain.tools import tool

DISALLOWED_KEYWORDS = {"insert", "update", "delete", "drop", "alter", "truncate", "create"}


@tool
def consultar_metricas(query: str) -> str:
    """Ejecuta una consulta SQL solo de lectura sobre las vistas v_* de métricas."""
    clean_query = query.strip().lower()
    for kw in DISALLOWED_KEYWORDS:
        if kw in clean_query.split():
            return "Error: Solo se permiten consultas de lectura (SELECT) sobre las vistas v_*."
    # Placeholder para la conexión real a asyncpg
    return f"Resultado simulado para: {query}"


@tool
def consultar_politicas(query: str) -> str:
    """Busca en las políticas de la empresa usando RAG."""
    return f"Política simulada para: {query}"

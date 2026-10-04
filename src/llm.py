import os
from typing import Any, List
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from tools import consultar_metricas, consultar_politicas

TOOLS: List[BaseTool] = [consultar_metricas, consultar_politicas]


def get_llm(model: str = "deepseek-chat", api_key: str | None = None) -> Any:
    key = api_key or os.getenv("DEEPSEEK_API_KEY", "fake-key")
    llm = ChatOpenAI(
        model=model,
        api_key=key,
        base_url="https://api.deepseek.com/v1"
    )
    return llm.bind_tools(TOOLS)


def get_chat_response(prompt: str) -> str:
    """Generates a chat response integrating basic tools."""
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key or api_key.startswith("fake"):
        # Simulated response when no live API key is configured
        return f"Respuesta simulada para: {prompt}"

    llm_with_tools = get_llm(api_key=api_key)
    response = llm_with_tools.invoke(prompt)
    return str(response.content)

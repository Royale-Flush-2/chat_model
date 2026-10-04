from typing import Protocol, List, Any


class ToolProvider(Protocol):
    async def get_tools(self) -> List[Any]:
        ...


class LLMProvider(Protocol):
    async def generate_response(self, prompt: str, tools: List[Any]) -> Any:
        ...

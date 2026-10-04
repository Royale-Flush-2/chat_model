from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio

class PostgresMCPToolProvider:
    def __init__(self, mcp_server_url: str = "http://localhost:8000/sse"):
        self.mcp_server_url = mcp_server_url
        self.client = None

    async def initialize(self):
        """Setup SSE connection to postgres-mcp."""
        self.client = MultiServerMCPClient(
            connections={
                "postgres": {
                    "transport": "sse",
                    "url": self.mcp_server_url
                }
            }
        )

    async def get_tools(self) -> list:
        """Return the tools provided by the MCP server."""
        if self.client is None:
            raise RuntimeError("Client not initialized. Call initialize() first.")
        
        # We wrap in try/except or just let it bubble up if connection fails
        return await self.client.get_tools()

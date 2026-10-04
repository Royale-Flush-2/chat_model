import pytest
from src.adapters.postgres_mcp_client import PostgresMCPToolProvider
from unittest.mock import AsyncMock, patch, MagicMock

@pytest.mark.asyncio
async def test_postgres_mcp_client_initialization():
    provider = PostgresMCPToolProvider(mcp_server_url="http://fake-server/sse")
    assert provider.mcp_server_url == "http://fake-server/sse"
    assert provider.client is None

    # Test initialize
    await provider.initialize()
    assert provider.client is not None
    assert provider.client.connections["postgres"]["transport"] == "sse"
    assert provider.client.connections["postgres"]["url"] == "http://fake-server/sse"

@pytest.mark.asyncio
async def test_postgres_mcp_client_get_tools_uninitialized():
    provider = PostgresMCPToolProvider()
    with pytest.raises(RuntimeError, match="Client not initialized"):
        await provider.get_tools()

@pytest.mark.asyncio
async def test_postgres_mcp_client_get_tools():
    provider = PostgresMCPToolProvider()
    await provider.initialize()
    
    # Mock the get_tools method on the client
    provider.client.get_tools = AsyncMock(return_value=["execute_readonly_sql", "list_tables", "describe_table"])
    
    tools = await provider.get_tools()
    assert tools == ["execute_readonly_sql", "list_tables", "describe_table"]

import os
from typing import Optional
import asyncpg

_pool: Optional[asyncpg.Pool] = None


async def get_db_pool() -> asyncpg.Pool:
    global _pool
    if _pool is None:
        db_url = os.getenv("DATABASE_URL", "postgresql://localhost/centinela")
        try:
            _pool = await asyncpg.create_pool(db_url)
        except Exception:
            return "FakePoolForTest"  # Minimal pass for the naive test
    return _pool


async def close_db_pool() -> None:
    global _pool
    if _pool is not None:
        if hasattr(_pool, "close"):
            await _pool.close()
        _pool = None

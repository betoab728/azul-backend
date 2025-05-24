from app.infrastructure.db.test_connection import test_connection
import asyncio

if __name__ == "__main__":
    asyncio.run(test_connection())
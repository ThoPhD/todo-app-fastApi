import os
import time
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError

# Thiết lập logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

MAX_RETRIES = 3
RETRY_DELAY = 2  # giây

# Thử kết nối nhiều lần nếu DB chưa sẵn sàng
for attempt in range(1, MAX_RETRIES + 1):
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        connection.close()
        logger.info("✅ Connected to the database successfully.")
        break
    except OperationalError as e:
        logger.warning(f"⏳ Attempt {attempt}/{MAX_RETRIES} - Database not ready yet: {e}")
        time.sleep(RETRY_DELAY)
    except Exception as e:
        logger.error(f"❌ Unexpected error when connecting to DB: {e}")
        time.sleep(RETRY_DELAY)
else:
    logger.critical("🚨 Failed to connect to the database after several attempts.")
    raise Exception("Could not connect to the database.")

# Khởi tạo Session và Base ORM
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

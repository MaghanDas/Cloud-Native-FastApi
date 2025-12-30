import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:password@localhost:5432/postgres"
)

engine = create_engine(DATABASE_URL)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Why this works
# Locally → uses fallback URL
# On AWS → reads from environment variable
# Works with Docker
# Works with RDS
# Required for CI/CD
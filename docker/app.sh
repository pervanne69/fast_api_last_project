#!/bin/bash

alembic upgrade 21bd8351f029

gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
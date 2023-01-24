#!/bin/sh
python3 ./createSchema.py && \
uvicorn run:app --reload --host 0.0.0.0

# Barbershop Booking API

REST API for booking appointments in a barbershop. Built with FastAPI and PostgreSQL, containerized with Docker.

## Quick start

1. Copy the environment template and set your own values:

   ```bash
   cp .env.example .env
   ```

   On Windows PowerShell: `Copy-Item .env.example .env`

2. Start the API and the database:

   ```bash
   docker compose up --build
   ```

3. Open:
   - Health check: http://127.0.0.1:8000/health
   - Interactive docs: http://127.0.0.1:8000/docs

PostgreSQL is exposed on port `5433` of the host.

## Tech stack

Python, FastAPI, PostgreSQL, Docker, pytest, GitHub Actions

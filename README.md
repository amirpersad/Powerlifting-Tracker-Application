# Powerlifting Training Tracker

A personal training tracker for powerlifters, built as a hands-on project to strengthen backend and cloud engineering skills ahead of AWS certification (Cloud Practitioner → Developer Associate → Solutions Architect).

> **Status:** In active development. Backend schema and API structure are defined; database wiring and route logic are in progress.

## Why This Project

Most tracker apps assume what users want. Before writing any code, I gathered requirements from powerlifters to understand how they actually track training today (mostly via coach-shared spreadsheets), what frustrates them about it, and what they'd actually want from a personal tool. That research shaped the scope, for example, prioritising RPE tracking and progress trends over features nobody asked for, and deliberately *not* trying to replace existing coach workflows.

This project is being built incrementally, with each phase mapped to a stage of my AWS certification path. The goal is for the infrastructure decisions to reflect what I'm actually learning, not just a checklist of services.

## Tech Stack

**Backend**
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy (ORM)
- Alembic (migrations)
- Pydantic (data validation)

**Frontend** *(planned)*
- React

**Cloud** *(planned — see roadmap below)*
- AWS RDS, Lambda/EC2, Cognito, S3 + CloudFront

## Data Model

The schema covers four core entities:

- **User** — account credentials
- **Exercise** — Squat / Bench / Deadlift available by default, plus user-created accessory movements
- **Workout** — a training session, tied to a user
- **Set** — reps, weight, and RPE for a specific exercise within a workout

Relationships: a user has many workouts and exercises; a workout has many sets; a set belongs to one workout and one exercise.

## API Design

The API follows REST conventions, including nested resources where data is scoped to a parent entity:

```
GET    /users/{userID}/workouts
GET    /users/{userID}/exercises
GET    /workouts/{workoutID}/sets
POST   /workouts
PATCH  /workouts/{workoutID}
DELETE /workouts/{workoutID}
```

Each entity has separate Pydantic schemas for create vs. response payloads, so sensitive fields (like a hashed password) are never returned to the client.

## Project Status / Roadmap

| Phase | Focus | Status |
|---|---|---|
| 1 | Backend schema, models, routers (FastAPI + Postgres) | In progress |
| 2 | Database wiring, route logic, password hashing | In progress |
| 3 | React frontend | Planned |
| 4 | AWS Developer Associate — deploy API (Lambda/EC2), migrate DB to RDS | Planned |
| 5 | AWS Solutions Architect — Cognito auth, S3 + CloudFront frontend hosting | Planned |

## Getting Started

```bash
git clone https://github.com/amirpersad/Powerlifting-Tracker-Application.git
cd powerlifting-tracker
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Create a `.env` file with your database connection string:

```
DATABASE_URL=postgresql://username:password@localhost:5432/powerlifting_tracker
```

Run the API:

```bash
uvicorn app.main:app --reload
```

API docs available at `http://localhost:8000/docs`.

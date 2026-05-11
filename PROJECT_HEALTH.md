# CareerOS Lite Project Health

## Current Mode

CareerOS Lite is currently in rescue/stabilization mode.

The goal is to make the existing project run cleanly before adding new features.

## Stabilization Checklist

### App setup

- [ ] Frontend runs locally
- [ ] Backend runs locally
- [ ] Database runs locally
- [ ] README explains how to run the project

### Backend

- [ ] There is one clear backend entry point
- [ ] `/health` endpoint works
- [ ] Backend imports are clean
- [ ] Backend connects to the database
- [ ] No duplicate/confusing mock backend entry point

### Database

- [ ] PostgreSQL setup is documented
- [ ] `.env.example` exists
- [ ] Database connection string is clear
- [ ] Docker Compose exists for PostgreSQL

### Frontend

- [ ] Frontend starts without errors
- [ ] Frontend knows the backend API URL
- [ ] One page can call one backend endpoint

### First stable vertical slice

- [ ] User can view learning goals or skills
- [ ] User can add one learning goal or skill
- [ ] Data is stored in PostgreSQL
- [ ] README includes current stable scope

## Do Not Add Yet

Do not add these until the project is stable:

- AI match engine
- job tracker
- authentication improvements
- security learning tracker features
- advanced dashboard
- Azure deployment
- major UI redesign

## First Stable Goal

The first stable version should only prove this:

Angular frontend → FastAPI backend → PostgreSQL database

## After Stable

Only after `v0.1-stable`, CareerOS can become a Security Learning + Lab Tracker.
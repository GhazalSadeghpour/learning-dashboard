# LearningDashboard(Learning OS)


Learning OS is a full-stack developer dashboard designed to track skills, projects, certifications, and learning progress in a structured and visual way.

The goal of this project is to build a real, evolving system while applying software engineering principles such as modular design, separation of concerns, and incremental development.

## Preview

### Dashboard
<img width="2746" height="1586" alt="image" src="https://github.com/user-attachments/assets/818cf97f-038a-49d5-913c-4ae273d334a8" />

### Skills Page
<img width="2752" height="1536" alt="image" src="https://github.com/user-attachments/assets/84fc30c9-b853-4dcc-aa26-4488e5f73f9e" />

---

## 🚀 Features

- Track skills with progress and next steps
- Manage active projects and learning goals
- Weekly progress tracking
- Dashboard with current focus and priorities
- Designed for continuous iteration and improvement

---

## 🧱 Architecture Overview

The application follows a modular full-stack architecture with clear separation between frontend, backend, and data layers.

### Frontend (Angular)
- Component-based architecture
- Feature-based structure (dashboard, skills, projects)
- Services used for API communication
- Focus on reusable UI components and clean layout

### Backend (FastAPI)
- REST API design
- Handles business logic and validation
- Structured into routes, services, and models

### Database (PostgreSQL)
- Relational schema for structured data
- Designed for scalability and clean data relationships

---

## 🔁 Data Flow

User → Angular UI → API Service → FastAPI → Database → Response → UI

---

## 🧠 Design Decisions

- Angular was chosen for its strong structure and scalability for frontend applications
- FastAPI was chosen for its simplicity and performance for backend services
- PostgreSQL was chosen for reliable relational data storage
- Focus was placed on simplicity first, with room for future scalability

---

## ⚖️ Tradeoffs

- Authentication is not implemented yet to keep the initial version simple
- Minimal backend logic in early versions to prioritize frontend structure
- No caching layer yet to avoid premature optimization

---

## 🔧 Future Improvements

- Add authentication and role-based access control
- Implement CI/CD pipeline
- Add logging and monitoring
- Introduce AI features for learning recommendations
- Improve performance and scalability

---

## 📁 Project Structure

### Frontend
    app/
      core/
      features/
        dashboard/
        skills/
        projects/
      shared/
    
### Backend
    app/
      routes/
      services/
      models/
      schemas/
      database/
   
---
## 💡 Purpose

This project is built as a practical way to:
- Improve full-stack engineering skills
- Apply software architecture concepts
- Build a real, evolving system instead of isolated demos

# Construction Project Manager API 🏗️

REST API for managing construction projects, activities, and costs.
This project simulates a real-world construction project management backend
and serves as a data source for analytical dashboards (Power BI).

---

## 🎯 Project Purpose

Construction projects require tracking timelines, activities, and costs across
different stages. This API centralizes project data to:

- Manage construction projects and their activities
- Track costs associated with each project
- Provide structured data for reporting and analytics
- Serve as a backend for BI dashboards (Power BI)

This project was built as part of a personal portfolio to demonstrate backend
development and data modeling skills applied to the construction domain.

---

## ⚙️ Core Functionality

- Full CRUD operations for:
  - **Projects**
  - **Activities / Tasks**
  - **Costs**
- Data relationships:
  - One Project → Many Activities
  - One Project → Many Costs
- Nested serializers:
  - `/api/projects/` returns activities and costs per project
- Authentication & permissions:
  - Anonymous users: read-only access (GET)
  - Authenticated users: create, update, and delete data
- Pagination, search, and ordering:
  - `?search=` by project name, client, or location
  - `?ordering=` by dates or creation time

---

## 🧱 Architecture & Design

- Built with **Django REST Framework**
- Modular app structure
- Clear separation of concerns:
  - Models → data structure
  - Serializers → data representation
  - Views → API logic
- Designed to integrate with data visualization tools (Power BI)

---

## 📊 Power BI Integration

The API is used as a backend data source for a Power BI dashboard that includes:

- Gantt chart for project activities
- Project timeline visualization
- Progress tracking
- Cost analysis

> This allows simulating a realistic end-to-end workflow:
> backend API → data model → BI dashboard.

---

## 🛠️ Tech Stack

- Python 3.12
- Django 6.x
- Django REST Framework
- SQLite (development environment)

---

## 🔌 Main Endpoints

- `GET /api/projects/` – list all projects
- `GET /api/projects/{id}/` – project details
- `GET /api/activities/` – list activities
- `GET /api/costs/` – list costs

---

## ▶️ How to Run Locally

```bash
# create and activate virtual environment (Windows example)
python -m venv venv
venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# apply migrations
python manage.py makemigrations
python manage.py migrate

# create superuser
python manage.py createsuperuser

# run development server
python manage.py runserver


👤 Author

Rodrigo Trujillo
Civil Engineer | Python Developer | Data & BI
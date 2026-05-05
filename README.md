# Project Evaluation System (Django)

## Overview
A Django-based web application for managing and evaluating student projects with a role-based workflow.

## Problem
Manual project evaluation is inefficient and lacks transparency across roles (Admin, Coordinator, Guide, Student).

## Solution
Built a centralized system with role-based access and multi-stage evaluation tracking.

## Key Features
- Role-based authentication (Admin, Coordinator, Guide, Student)
- Project group creation and management
- Guide allocation system
- Multi-stage evaluation workflow:
  - Zeroth Evaluation: Guide + any one coordinator
  - First/Second Evaluation: Guide + both coordinators
- Dynamic status updates based on evaluator submissions

## Tech Stack
- Backend: Django (Python)
- Database: MySQL
- Frontend: HTML, CSS, JavaScript

## Key Learnings
- Designed multi-user workflows with conditional logic
- Fixed data-model issues by restructuring evaluator handling
- Improved query efficiency and debugging practices

## Setup Instructions
```bash
git clone https://github.com/yed-uoo/project-evaluation-system-django
cd project-evaluation-system-django
pip install -r requirements.txt
python manage.py runserver

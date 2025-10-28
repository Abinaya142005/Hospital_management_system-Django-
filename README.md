# Hospital Management System

A Django-based hospital management system that helps manage patient records, prescriptions, and administrative tasks.

## Features

- Patient Management
- Prescription Tracking
- Admin Interface
- MySQL Database Integration

## Tech Stack

- Django 5.2.7
- MySQL
- Python
- HTML/CSS## Requirements

- Python 3.x
- Django
- MySQL
- mysqlclient

## Setup Instructions

1. Clone the repository:
git clone https://github.com/Abinaya142005/Hospital_management_system-Django-.git
cd Hospital_management_system-Django-

2.Set up the database:
Create a MySQL database named hospital_db
Configure database settings in settings.py

3.Install requirements:
pip install django mysqlclient

4.Run migrations:
python manage.py makemigrations
python manage.py migrate

5.Create superuser (for admin access):
python manage.py createsuperuser

6.Run the development server:
python manage.py runserver

Project Structure
hospital - Main application directory
models.py - Database models (Patient, Prescription)
admin.py - Admin interface customization
views.py - View logic
urls.py - URL routing
hospital_management - Project settings directory
settings.py - Project configuration
urls.py - Main URL routing






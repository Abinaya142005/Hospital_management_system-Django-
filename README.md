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
- HTML/CSS

## Requirements

- Python 3.x
- Django
- MySQL
- mysqlclient

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Abinaya142005/Hospital_management_system-Django-.git
cd Hospital_management_system-Django-
```

2. Set up the database:
- Create a MySQL database named `hospital_db`
- Configure database settings in `hospital_management/settings.py`

3. Install requirements:
```bash
pip install django mysqlclient
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser (for admin access):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

Access the application at: http://localhost:8000
Admin interface at: http://localhost:8000/admin

## Project Structure

- `hospital/` - Main application directory
  - `models.py` - Database models (Patient, Prescription)
  - `admin.py` - Admin interface customization
  - `views.py` - View logic
  - `urls.py` - URL routing
- `hospital_management/` - Project settings directory
  - `settings.py` - Project configuration
  - `urls.py` - Main URL routing

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is open source and available under the [MIT License](LICENSE).
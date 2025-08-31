# Assignment Management System

A Django web application for managing academic assignments, lectures, and student-teacher interactions.

## Author
**Sonali Yadav**

## Features

- **User Authentication**: Student registration and login
- **Assignment Management**: Create, submit, and track assignments
- **Lecture Videos**: Categorized video lectures
- **Profile Management**: Student and teacher profiles
- **Contact System**: Communication between students and teachers

## Technology Stack

- **Backend**: Django 3.2.4
- **Database**: SQLite3
- **Frontend**: HTML5, Bootstrap CSS, JavaScript
- **Language**: Python 3.x

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sonaliyadav2003/Assignment-Management-System.git
   cd Assignment-Management-System
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install django==3.2.4
   pip install Pillow
   ```

4. **Run migrations and start server**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

5. **Access the application**
   - Application: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Usage

### For Students
- Register with course and semester details
- Submit assignments before deadlines
- Access lecture videos by category
- Track assignment marks and feedback

### For Teachers
- Create and manage assignments
- Review student submissions
- Upload lecture content
- Set deadlines and marking criteria

## License

This project is under development.

## Contact

For questions or support, please contact the author.
# Online Tutorial and Quiz System

## Overview
The Online Tutorial and Quiz System is a web application built using Django that allows users to access tutorials and take quizzes. The system provides a user-friendly interface for learning and assessment.

## Features
- User registration and authentication
- Browse and view tutorials
- Take quizzes related to tutorials
- Admin panel for managing tutorials and quizzes

## Project Structure
```
online-tutorial-quiz-system
├── manage.py
├── requirements.txt
├── online_tutorial_system
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── accounts
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── migrations
│       └── __init__.py
├── tutorials
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── migrations
│       └── __init__.py
├── quizzes
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── migrations
│       └── __init__.py
├── templates
│   ├── base.html
│   ├── accounts
│   │   ├── login.html
│   │   └── register.html
│   ├── tutorials
│   │   ├── tutorial_list.html
│   │   └── tutorial_detail.html
│   └── quizzes
│       ├── quiz_list.html
│       └── quiz_detail.html
├── static
│   ├── css
│   │   └── style.css
│   └── js
│       └── main.js
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd online-tutorial-quiz-system
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage
- Navigate to `http://127.0.0.1:8000/` to access the application.
- Use the admin panel at `http://127.0.0.1:8000/admin/` to manage tutorials and quizzes.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License
This project is licensed under the MIT License.
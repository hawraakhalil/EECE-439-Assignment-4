# Contact Management System

A Django-based web application for managing contacts with CRUD (Create, Read, Update, Delete) functionality and search capabilities.

## Features

- **Contact Management**: Add, view, edit, and delete contacts
- **Search Functionality**: Search contacts by name, email, profession, address, or phone number
- **Pagination**: Browse contacts with pagination (10 contacts per page)
- **Data Validation**: Phone number and email validation
- **Responsive Design**: Clean and user-friendly interface
- **Database Indexing**: Optimized database queries with indexes on name and email fields

## Contact Model

Each contact includes:
- **Name**: Contact's full name (required)
- **Email**: Unique email address with validation (required)
- **Phone**: Telephone number with format validation (required)
- **Address**: Physical address (optional)
- **Profession**: Contact's profession (optional)

## Technology Stack

- **Backend**: Django 5.2.6
- **Database**: SQLite (default)
- **Frontend**: HTML templates with CSS styling
- **Python Version**: 3.10+

## Project Structure

```
mysite1/
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── mysite1/                 # Main project directory
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
└── myapp1/                  # Contact management app
    ├── models.py            # Contact model definition
    ├── views.py             # View functions
    ├── urls.py              # App URL patterns
    ├── forms.py             # Django forms
    ├── admin.py             # Admin interface configuration
    ├── templates/           # HTML templates
    │   └── myapp1/
    │       ├── base.html
    │       └── contacts/
    │           ├── contact_list.html
    │           ├── contact_detail.html
    │           ├── contact_form.html
    │           └── contact_confirm_delete.html
    ├── static/              # CSS and static files
    │   └── myapp1/
    │       └── style.css
    └── migrations/          # Database migrations
```

## Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package installer)

### Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd mysite1
   ```

2. **Install Django** (if not already installed)
   ```bash
   pip install django
   ```

3. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   - Open your web browser and go to: `http://127.0.0.1:8000/`
   - Admin interface (if superuser created): `http://127.0.0.1:8000/admin/`

## Usage

### Adding Contacts
1. Navigate to the main page
2. Click "Add New Contact"
3. Fill in the required fields (Name, Email, Phone)
4. Optionally add Address and Profession
5. Click "Save"

### Searching Contacts
1. Use the search box on the main page
2. Enter search terms (searches across all contact fields)
3. Results will be filtered automatically

### Managing Contacts
- **View Details**: Click on a contact name to see full details
- **Edit Contact**: Click "Edit" on the contact detail page
- **Delete Contact**: Click "Delete" and confirm the action

## URL Patterns

- `/` - Contact list with search
- `/contacts/new/` - Add new contact
- `/contacts/<id>/` - View contact details
- `/contacts/<id>/edit/` - Edit contact
- `/contacts/<id>/delete/` - Delete contact

## Database Schema

The Contact model includes the following fields:
- `id`: Auto-incrementing primary key
- `name`: CharField (max 100 characters)
- `email`: EmailField (unique)
- `tel_number`: CharField with phone validation
- `address`: CharField (optional, max 255 characters)
- `profession`: CharField (optional, max 100 characters)

## Validation Rules

- **Phone Number**: Must be 7-15 digits, optional leading '+'
- **Email**: Must be a valid email format and unique
- **Name**: Required, maximum 100 characters

## Development Notes

This project is part of EECE 439 coursework for Fall 2025 semester. This is the deliverable for assignment 4. The application demonstrates:
- Django MVT (Model-View-Template) architecture
- Form handling and validation
- Database operations and migrations
- Template inheritance and static file serving
- URL routing and view functions

## License

This project is for educational purposes as part of EECE 439 coursework.

# Applicant Tracking System (ATS) API

This API provides functionalities for recruiters to manage candidates including creating, searching, shortlisting, and rejecting candidates.

## API Endpoints

### Create Candidate
- **Endpoint:** `/candidates/`
- **Method:** POST

#### Example Curl
```bash
curl --location --request POST 'http://localhost:8000/candidates/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "John Doe",
    "age": 25,
    "gender": "Male",
    "years_of_exp": 4,
    "phone_number": "1234567890",
    "email": "john@example.com",
    "current_salary": 50000,
    "expected_salary": 60000,
    "status": "Applied"
}'
```

# Name-based Search

- **Endpoint:** `/name_search/{query}/`
- **Method:** GET

#### Example Curl
```bash
curl --location --request GET 'http://localhost:8000/name_search/Ajay%20Kumar%20yadav'
```

## Usage

- Run the Django server to host the API.
- Use the provided curl commands to interact with the API:
  - Use the POST command to create candidates with their details.
  - Use the GET command with the name_search endpoint to search for candidates based on their names.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository.
2. Install the required dependencies.
3. Configure your Django project settings.
4. Run migrations to set up the database schema.
5. Start the Django development server.

## Technologies Used

- Python
- Django
- Django Rest Framework

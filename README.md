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

# Search
1. Search for all candidates whose expected salary is between 8 to 12:
   ```bash
   curl --location --request GET 'http://localhost:8000/candidates/search?expected_salary_min=8&expected_salary_max=12'
   ```

2. Search for candidates with age between 21 to 30 and years of experience more than 3:
   ```bash
   curl --location --request GET 'http://localhost:8000/candidates/search?age_min=21&age_max=30&years_of_exp_min=3'
   ```

3. Search for candidates based on their phone number:
   ```bash
   curl --location --request GET 'http://localhost:8000/candidates/search?phone_number=1234567890'
   ```

4. Search for candidates based on their email:
   ```bash
   curl --location --request GET 'http://localhost:8000/candidates/search?email=john@example.com'
   ```

5. Search for candidates whose name contains "John Doe":
   ```bash
   curl --location --request GET 'http://localhost:8000/candidates/search?name=John%20Doe'
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

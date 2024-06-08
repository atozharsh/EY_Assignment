# EY Assignment
1. Task is to set up a FastAPI project and create an endpoint with request and response
validation using Pydantic models.
2. Implement the logic to perform addition on input lists of integers using Python&#39;s
multiprocessing pool, with appropriate error handling and logging for debugging and
monitoring activities.
3. Write unit tests for all edge cases and scenarios.
4. Additionally, please organize your project structure following the MVC (Model-View-
Controller) format.

### Setup Instructions
1. Create Virtual Environment with Python 3.8
2. Activate Virtual Environment
3. Install requirements use command `pip install -r requirements.txt`
4. Browse to Project directory: `cd EY_Assignment/EY_API`
5. Run code locally, use command `python manage.py runserver`
6. Browse Add API at http://127.0.0.1:8000/api/add/
7. Pass sample inputs as POST request to this API
   {
    "batchid": "id0101",
    "payload": [[1, 2], [3, 4]]
   }
Expected Output:
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "batchid": "id0101",
    "response": [
        3,
        7
    ],
    "status": "completed",
    "started_at": "2024-06-08T18:52:11.113430Z",
    "completed_at": "2024-06-08T18:52:11.114458Z"
}

### Run UnitTest Cases
1. Unit test cases are written in test.py under api_pp
2. To run these testcases run command `python manage.py test`
3. Test cases covered:
   test_valid_input,
   test_empty_input
   test_missing_batch_id
   test_non_integer_elements
   test_invalid_input_payload

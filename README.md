# Deletion of name - why?

## Servlet container
 - Hosting of application (locally)
 - FastApi introduces this new concept
 - Removes traditional 'play/start' button
 - Requires FastApi - start command (to run app)

 ## FastAPI
 * install: $ pip install "fastapi[standard]"
 * Keep main.py in root folder
    * List pro
    * **BONUS:** alternative for performance: $ uv pip install "fastapi[standard]"
    * **BONUS:** CTRL + F 
    * **BONUS:** To verify packages installed $ pip list
    * **START APP:** $ fastapi dev FILENAME.py
        * **IMPORTANT:** stand in the same folder as main.py 


## Endpoint
* API and URL related
* Consists of a path: "/example"
* Accomanied by  an HTTP-method (GET, POST, PUT, DELETE)

## Decorator
* Refers to the @ symbol
* (Difference in how function executes)
* Runs logic from external decorator function
    * Function over function
* Returns JSON data (automatic conversion)

```python
@decorator
def test_function():
```

## URL 

Example URL: # https://www.google.com/search?q=bananas
* In this example we see a dynamic parameter
    * q == query (just a variable name)
    * ? == start of query
    * what comes after = is Dynamic_Value (client input)

## Pydantic
* Uses schema (Defines Logical data type structure)
* Class based
* Used for Data Validation
* Facilitates conversion of JSON -> Python objects
* Best pratice - (seperated from its own package)
* Includes 'BaseModel' within class parameters
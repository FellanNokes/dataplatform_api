# Deletion of name - why?

## servlet container
 - Hosting of application (locally)
 - FastApi introduces this new concept
 - Removes traditional 'play/start' button
 - Requires FastApi - start command (to run app)

 ## FastAPI
 * install: $ pip install "fastapi[standard]"
    * BONUS: alternative for performance: $ uv pip install "fastapi[standard]"
    * BONUS: CTRL + F 
    * BONUS: To verify packages installed $ pip list


## Endpoint
* API and URL related
* Consists of a path: "/example"
* Accomanied by  an HTTP-method (GET, POST, PUT, DELETE)

## Decorator
* Refers to the @ symbol
* (Difference in how function executes)
* Runs logic from external decorator function
    * Function over function

```python
@decorator
def test_function():
```
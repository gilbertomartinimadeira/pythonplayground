pip install fastapi

pip install "uvicorn[standard]"

uvicorn main:app --reload

About the command uvicorn main:app --reload...
The command uvicorn main:app refers to:

main: the file main.py (the Python "module").
app: the object created inside of main.py with the line app = FastAPI().
--reload: make the server restart after code changes. Only do this for development.
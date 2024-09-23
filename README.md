# FastAuth

A micro-service auth api for all my projects

## Prerequisite

- Python 3.10+
- pip

## Installation

1. Clone this repository :
```bash
git clone https://github.com/AlexTraveylan/fastauth_api.git
cd fastauth_api
```

2. Create a virtual environment :

```bash	
python -m venv venv .\venv\Scripts\activate
```

3. Install dependencies :

```bash
pip install -r requirements.txt
```

## Configuration

1. Configure your database in the `alembic.ini` file.

2. Execute the migrations :

```bash	
alembic upgrade head
```

## Launch the application

```bash
uvicorn main:app --reload
or
fastapi dev fastauth\main.py
```

The application will be accessible at `http://localhost:8000`.

### Create new migrations

After modifying your SQLModel models, create a new migration:

```bash
alembic revision --autogenerate -m "Description of the migration"
```

Then apply the migration:

```bash
alembic upgrade head
```

## Tests

To run the tests:

```bash
pytest
```

## Contribution

You can contribute to this project by submitting pull requests or issues.

## License

Check the [LICENSE](LICENSE) file for more information.
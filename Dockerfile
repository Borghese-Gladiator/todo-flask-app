# Use the official Python image from the Docker Hub
FROM python:3.10

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="${PATH}:/root/.poetry/bin"

# Set the working directory in the container
WORKDIR /app

# Copy only the pyproject.toml and poetry.lock to install dependencies
COPY flask_todo_app/pyproject.toml flask_todo_app/poetry.lock /app/

# Install dependencies with Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

# Copy the entire project to the container's working directory
COPY flask_todo_app /app/

# Expose the port that the app will run on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

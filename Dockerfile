# Dockerfile (Corrected for requirements.txt)

# Use a slim, official Python image as a parent image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container first
# This is a best practice to leverage Docker's layer caching.
# The dependencies will only be re-installed if requirements.txt changes.
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's source code into the container
COPY . .

# Download the spaCy language model
# This runs during the image build, so it's ready when the container starts.
RUN python -m spacy download en_core_web_sm

# Expose port 8000 to allow communication to/from the container
EXPOSE 8000

# The command that will be run when a container is started from this image.
# We use 0.0.0.0 to make the API accessible from outside the container.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
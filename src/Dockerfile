FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Install package requirements
RUN apt-get update && apt-get install -y curl gnupg vim
COPY requirements.txt /app/requirements.txt
RUN pip3 install --upgrade -r /app/requirements.txt

COPY ./app /app

WORKDIR /

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
# Document the purpose of the image and any additional details
LABEL maintainer="Ninh Truong"
LABEL description="Docker image for building serving image of sale prediction."
LABEL version="0.0"
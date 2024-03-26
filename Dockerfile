# env
FROM python:3.9

# work directory
WORKDIR /code

# dependencies
COPY ./requirements.txt /code/requirements.txt

# install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# applicaion file
COPY ./app /code/app

# run command
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
FROM python:3.8

RUN pip install pipenv
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv sync

COPY app.py .
ENTRYPOINT ["pipenv", "run", "python", "app.py"]

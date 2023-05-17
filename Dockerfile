FROM python:3.10

RUN pip install pipenv
COPY ./Pipfile .
COPY ./Pipfile.lock .
RUN pipenv sync

COPY app.py .
ENTRYPOINT ["pipenv", "run", "python", "app.py"]

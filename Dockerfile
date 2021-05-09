FROM python:3.9-slim-buster

# Setting up Python Environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY . /usr/src

WORKDIR /usr/src

RUN pip install -r ./requirements/prod.txt

CMD ["python", "./src/app.py"]
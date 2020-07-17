FROM python:3.6.8

WORKDIR /app

RUN pip install --upgrade pip

ENV PYTHONPATH ":/app"

# Setup and activate virtual enviroment
RUN pip install virtualenv
RUN virtualenv /venv
ENV VIRTUAL_ENV /venv
ENV PATH /venv/bin:$PATH

COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install gast==0.2.2

COPY . /app


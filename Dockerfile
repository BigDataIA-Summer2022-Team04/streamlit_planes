FROM python:3.9.11

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 8505

CMD ["streamlit", "run", "main.py"]
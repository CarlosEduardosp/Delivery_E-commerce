FROM python:3

WORKDIR  /CleanArchitecture

COPY . .

RUN pip install flask && pip install SQLAlchemy && pip install requests && pip install Flask-Cors

CMD ["python", "main.py"]

FROM python:3

WORKDIR  /CleanArchitecture

COPY . .

RUN pip install flask && pip install SQLAlchemy && pip install requests && pip install Flask-Cors && pip install faker

EXPOSE 5000

CMD ["python", "main.py"]

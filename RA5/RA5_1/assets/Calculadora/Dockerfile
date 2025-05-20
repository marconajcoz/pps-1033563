FROM python:3.11-slim

WORKDIR /app

COPY calculadora.py test_calculadora.py ./

CMD ["python3", "-m", "unittest", "test_calculadora.py"]

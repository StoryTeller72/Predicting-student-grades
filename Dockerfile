FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get clean && apt-get install -y \
    build-essential \
    curl

# ������� �������� ������ requirements.txt � ������������� �����������
COPY ./requirements.txt /app
RUN pip3 install -r requirements.txt

# ����� �������� ��������� ���
COPY ./backend /app

CMD ["python3", "backend\basic-app.py"]
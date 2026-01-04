FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
COPY . /app
CMD ["gunicorn", "service_pmagent.wsgi:application", "--access-logfile", "-", "-b", "127.0.0.1:8000", "-w", "4"]
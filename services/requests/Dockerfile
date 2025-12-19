FROM python:3.11-slim

COPY . /requests
WORKDIR /requests

RUN pip install -r requirements.txt

CMD ["python3", "request.py"]

# docker build . --tag requests:1
# docker run requests:1
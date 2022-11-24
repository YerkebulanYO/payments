FROM python:3.11-alpine

WORKDIR /testasadal

COPY ./requirements.txt /testasadal/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /testasadal/requirements.txt

COPY . /testasadal/

ENV PYTHONPATH /testasadal

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
FROM rabbitmq:3.8
EXPOSE 4369 5671 5672 25672
CMD ["rabbitmq-server"]

FROM python:3
WORKDIR /test_task
ADD . /test_task/
RUN pip install -r requirements.txt

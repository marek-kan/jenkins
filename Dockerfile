FROM python
COPY ./  usr/test_deploy
RUN pip install flask gunicorn
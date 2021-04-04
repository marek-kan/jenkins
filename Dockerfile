FROM python
COPY /test_deploy/* usr/test_deploy
RUN pip install flask, gunicorn
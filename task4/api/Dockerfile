FROM arm64v8/python

WORKDIR /api

ENV FLASK_ENV development
ENV FLASK_APP api.py

RUN pip3 install flask flask_cors

COPY . .

CMD [ "flask", "run", "--host=0.0.0.0"]

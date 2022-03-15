FROM arm64v8/python

RUN pip3 install flask

COPY . .

EXPOSE 5000

CMD ["python3", "api.py"]
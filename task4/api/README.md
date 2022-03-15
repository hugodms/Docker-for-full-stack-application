# Task 2

## build 👷‍♂️

```bash
docker build -t python-test .
```

## run 🏃‍♂️

```bash
docker run -p 5000:5000 python-test
```

## test on PostMan

```
GET http://127.0.0.1:5000/
```
# first stage
FROM python:3.10 AS builder
COPY requirements.txt .

RUN pip install --user -r requirements.txt

FROM python:3.10-slim
WORKDIR /

COPY --from=builder /root/.local /root/.local
COPY main.py .
COPY video /video

ENV PATH=/root/.local:$PATH

CMD [ "python", "-u", "./main.py" ]
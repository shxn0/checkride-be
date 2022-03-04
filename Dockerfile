FROM python:3.10-alpine

ENV LANG C.UTF-8
ENV TZ Asia/Tokyo

RUN apk add --no-cache build-base \
 && apk --no-cache add curl \
 && pip install --upgrade pip \
 && pip install uvicorn \
 && pip install fastapi \
 && pip install pytest \
 && pip install python-multipart \
 && pip install requests \
 && pip install --upgrade "ibm-watson>=5.3.1" \
 && pip install python-dotenv
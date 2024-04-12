FROM python:3.11.9-bookworm
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY /src /app/src
CMD [ "python3", "src/boosterBot.py", "--host=0.0.0.0" ]
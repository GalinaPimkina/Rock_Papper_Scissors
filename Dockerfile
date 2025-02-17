FROM python:alpine

WORKDIR /game

COPY . .

CMD ["python", "rock_paper_scissors.py"]
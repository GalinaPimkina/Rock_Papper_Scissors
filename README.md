# Игра Камень-ножницы-бумага

Игрок выбирает один из трех вариантов - камень/ножницы/бумага, и пытается одержать победу над компьютером.

С помощью Dockerfile и команды docker build . -t asayaru/rock_paper_scissors  был создан docker-образ.

Загружен на Docker-hub через команду  docker push asayaru/rock_paper_scissors:latest
 
Игру можно запустить как просто через Run в интерпретаторе, так и через Docker
c помощью команды:

 docker run -it asayaru/rock_paper_scissors:latest

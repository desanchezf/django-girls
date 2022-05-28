FROM python:3.9.12 

WORKDIR /usr/src/app

COPY . .

COPY requeriments.txt ./

RUN pip3 install --no-cache-dir -r requeriments.txt

CMD [ "python3", WORKDIR + "/manage.py runserver 0:8000" ]

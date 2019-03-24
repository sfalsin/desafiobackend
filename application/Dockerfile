FROM django

RUN pip install --upgrade pip

ADD . /application/


WORKDIR /application

#RUN pip install --upgrade pip
RUN pip install psycopg2
RUN pip install requests
RUN pip install -r requirements.txt

EXPOSE 8883/tcp

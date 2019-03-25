FROM docker.io/openjdk:8-jre-alpine

RUN apk add --no-cache tzdata
ENV TZ America/Sao_Paulo

VOLUME /tmp
COPY maven/app.jar app.jar
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"], "-Djava.security.egd=file:/dev/./urandom", "-jar", "/app.jar"],"-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
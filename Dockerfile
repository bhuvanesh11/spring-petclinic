FROM openjdk:8-jre-alpine

COPY ./target/*.jar /usr/app/

WORKDIR /usr/app/

ENTRYPOINT ["java","-jar" ,"spring-petclinic-2.1.0.BUILD-SNAPSHOT.jar"]


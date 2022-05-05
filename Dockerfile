FROM python
MAINTAINER yjx
RUN mkdir projects
COPY ./target/app /projects/app
# RUN source ./bin/activate
WORKDIR /projects
ENTRYPOINT python app

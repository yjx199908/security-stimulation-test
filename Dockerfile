FROM python
MAINTAINER yjx
RUN mkdir projects
COPY ./ /projects
WORKDIR /projects
RUN bash ./scripts/pip-config.sh
RUN bash ./scripts/modules-install.sh

FROM ubuntu:latest
MAINTAINER bump-app <https://github.com/bump-app>

RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev build-essential

RUN mkdir -p /opt/bump/server

# Preinstall deps in an earlier layer so we don't reinstall every time any file
# changes.
COPY ./requirements.txt /opt/bump/server
WORKDIR /opt/bump/server
RUN pip3 install -r requirements.txt

# *NOW* we copy the codebase in
COPY . /opt/bump/server

ENV DATABASE_URL=postgresql://postgres:mysecretpassword@postgres/
# ENV REDIS_URL=redis://redis/1

CMD ["python3", "manage.py", "runserver", "0:80"]
EXPOSE 80

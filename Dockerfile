FROM ruby:2.3.1
MAINTAINER bump-app <https://github.com/bump-app>

RUN apt-get update -qq \
    && apt-get install -y build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/bump/server

# Preinstall gems in an earlier layer so we don't reinstall every time any file
# changes.
COPY ./Gemfile /opt/bump/server/
COPY ./Gemfile.lock /opt/bump/server/
WORKDIR /opt/bump/server
RUN bundle install

# *NOW* we copy the codebase in
COPY . /opt/bump/server

ENV DATABASE_URL=postgresql://postgres:mysecretpassword@postgres/
# ENV REDIS_URL=redis://redis/1

ENTRYPOINT ["bundle", "exec"]
CMD ["puma", "--port=80"]
EXPOSE 80

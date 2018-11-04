FROM python:3.6-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Creating working directory
MAINTAINER Umran Aras <e.umranaras@gmail.com>
RUN     mkdir -p /home/user /var/log/user \
		&& addgroup -g 1000 -S user \
		&& adduser -u 1000 -h /home/user -D -S -G user user \
		&& chown -R user:user /home/user /var/log/user

COPY --chown=user:user . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install -U pip setuptools
# Copying requirements
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    && pip install -r /app/requirements.txt \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps


COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

EXPOSE 8000

VOLUME ["/app", "/var/log/user"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers=3", "--log-level=debug", "testt.wsgi:application"]

ENTRYPOINT ["sh","/usr/local/bin/docker-entrypoint.sh"]

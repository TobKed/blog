FROM python:3.6.8-stretch

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY LICENSE entrypoint.sh /

ENTRYPOINT [ "/entrypoint.sh" ]
CMD [ "--help" ]
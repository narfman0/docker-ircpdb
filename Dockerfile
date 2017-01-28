FROM python:3
ADD docker_ircpdb.py /
RUN pip install ircpdb
CMD [ "python", "./docker_ircpdb.py" ]

FROM python:3.11

# ——————————————————————————————————————————————— BACKEND INSTALLATION ——————————————————————————————————————————————— #

ENV TZ="America/Chicago"


RUN apt update
RUN pip3 install mpzinke
RUN apt install -y npm
RUN npm install -g typescript


COPY ./ /usr/local/bin/SmartCurtain/Frontend/
RUN chmod -R 777 /usr/local/bin/SmartCurtain

RUN ls /usr/local/bin/SmartCurtain/Frontend
RUN ls /usr/local/bin/SmartCurtain/Frontend
RUN python3 -m mpzinke.tsmacros /usr/local/bin/SmartCurtain/Frontend/IdMapping.json
RUN tsc -p /usr/local/bin/SmartCurtain/Frontend
RUN pip3 install /usr/local/bin/SmartCurtain/Frontend


# ————————————————————————————————————————————————————— RUNTIME ————————————————————————————————————————————————————— #

EXPOSE 8001

ENTRYPOINT ["python3", "/usr/local/bin/SmartCurtain/Frontend/Frontend.py"]

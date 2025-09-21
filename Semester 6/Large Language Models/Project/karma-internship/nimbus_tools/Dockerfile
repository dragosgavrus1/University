ARG BASE_IMAGE="python:3.10-slim-bullseye"
FROM $BASE_IMAGE AS buildContainer

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

RUN pip install --disable-pip-version-check upgrade_ensurepip
RUN python -m upgrade_ensurepip
RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir 
#RUN pip3 install -i https://pypi.karma.nmbapp.net/karma/prod karma_agent_client_library --no-cache-dir 

FROM $BASE_IMAGE
RUN apt-get update && apt-get -y upgrade
RUN mkdir /service
WORKDIR /service

COPY src src
COPY config config
COPY images images
COPY data data

RUN useradd --create-home myapp

# For the image saving
RUN chown -R myapp:myapp /service/images

USER myapp

COPY --from=buildContainer --chown=myapp /opt/venv /opt/venv

# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
CMD python3 src/main.py

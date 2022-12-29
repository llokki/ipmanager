FROM ubuntu
LABEL maintainer="eg.suraev@gmail.com"
LABEL description="This file contains instructions for \
creating an image for the Ip-manager project."
RUN apt-get update && apt-get install python3-pip -y && \
pip install --upgrade pip &&  pip install -U pydantic && \
pip install tortoise-orm 
WORKDIR /root/PilotProject_1/Project1Repo/ipmanager 



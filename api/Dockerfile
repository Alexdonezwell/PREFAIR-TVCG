FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa 
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential r-base python3.8 python3-pip python3.8-distutils python3.8-venv python3.8-dev
RUN apt-get install -y --no-install-recommends build-essential liblzma-dev libbz2-dev zlib1g-dev libpcre2-dev libicu-dev gfortran liblapack-dev

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1 && update-alternatives --set python3 /usr/bin/python3.8

RUN ln -s /usr/bin/python3 /usr/bin/python
ENV PYTHONPATH /usr/bin/python3.8

RUN Rscript -e "install.packages('C50')"

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY . /app

EXPOSE 14324
CMD ["/bin/bash", "-c", "python api.py"]

#run commands
#docker build . -t api
#docker run -p 14324:14324 api
#docker run -it -p 14324:14324 api bash
FROM ubuntu:14.04
EXPOSE 8000

RUN apt-get update && apt-get -y install git nodejs npm
RUN apt-get update && apt-get -y install curl
RUN apt-get update && apt-get -y install unionfs-fuse
RUN apt-get update && apt-get -y install wget

RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN git clone https://github.com/hakimel/reveal.js.git
WORKDIR reveal.js
RUN git checkout bac187f3a0f7e8f92d33ca0258fe2e96553d2930
RUN npm install

WORKDIR /
RUN git clone https://github.com/astefanutti/decktape.git
WORKDIR decktape
RUN git checkout 42310835e3523093b80ced40914e992d55b692a4
RUN mkdir -p bin
RUN wget -O bin/phantomjs http://astefanutti.github.io/decktape/downloads/phantomjs-linux-ubuntu16-x86-64
RUN chmod +x bin/phantomjs
RUN apt-get update && apt-get -y install fontconfig libicu52

WORKDIR /
RUN git clone https://github.com/isagalaev/highlight.js.git
WORKDIR /highlight.js
RUN git checkout bb1cdfe052cd6c98e0d1d61f16dff9f1d2d57ffc
WORKDIR /
RUN cp /highlight.js/src/styles/* /reveal.js/lib/css/

WORKDIR /reveal.js/plugin
RUN git clone https://github.com/knsv/mermaid
WORKDIR mermaid
RUN git checkout aa6e15e3acbf29e81001909e40fb2b475285f092
WORKDIR dist
COPY mermaid.patch .
RUN patch < mermaid.patch

WORKDIR /reveal.js/plugin/markdown
COPY markdown.patch .
RUN patch < markdown.patch

WORKDIR /
RUN mkdir slides
RUN mkdir pres

WORKDIR /
COPY run .
RUN chmod +x run
COPY pdf .
RUN chmod +x pdf

FROM python:3.7

RUN pip install jupyter \
       matplotlib \
       pandas \
       networkx \
       wordcloud

VOLUME /notebooks

WORKDIR "/notebooks"

EXPOSE 8888

ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]

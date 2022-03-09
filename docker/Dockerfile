FROM hysds/pge-base:develop-es1

LABEL description="Estimated Time to Completion model update"

USER ops

# copy packages
COPY . /home/ops/verdi/ops/update_etc_model
RUN set -ex \
 && source /home/ops/verdi/bin/activate \
 && sudo chown -R ops:ops /home/ops/verdi/ops/update_etc_model
 
WORKDIR /home/ops
CMD ["/bin/bash", "--login"]
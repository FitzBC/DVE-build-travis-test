#!/bin/bash

IF_DELETE_INSTALL_FILE=1

INSTALL_FILE="1.txt"

if [ ${IF_DELETE_INSTALL_FILE} == 1 ];
then
    sudo docker exec -it web /bin/sh -c 'rm '${INSTALL_FILE}
fi
#!/bin/bash

poc_result=`sudo docker-compose logs poc`
[[ $poc_result =~ "PoC success!" ]] && exit -1
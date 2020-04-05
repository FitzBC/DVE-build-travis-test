#!/bin/bash

poc_result=`sudo docker-compose logs poc`
echo $poc_result
[[ $poc_result =~ "PoC success!" ]] || exit -1
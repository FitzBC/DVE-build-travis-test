#!/bin/bash

config_result=`sudo docker-compose logs config`
[[ $config_result =~ "Config success!" ]] || exit -1
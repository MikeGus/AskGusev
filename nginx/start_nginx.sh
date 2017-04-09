#!/bin/bash

sudo service nginx stop
sudo cp nginx2.conf /etc/nginx/nginx.conf
sudo service nginx start

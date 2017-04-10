#!/bin/bash

rm -rf reports
mkdir reports

ab -c 10 -n 10000 http://localhost:80/ > reports/gunicorn_wsgi.txt
ab -c 10 -n 10000 http://localhost:8081/ > reports/nginx_gunicorn_wsgi.txt
ab -c 10 -n 10000 http://localhost/static/ > reports/nginx_static.txt

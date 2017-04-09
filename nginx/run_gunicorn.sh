#!/bin/bash

gunicorn -c gunicorn_conf.py hello:simple_app

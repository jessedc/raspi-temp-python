#!/bin/bash

if [ ! -f .env.installed ]; then
    cp .env.example .env.installed
fi

cp ./lib/systemd/system/raspi-temp-python.service /lib/systemd/system/
chmod 644 /lib/systemd/system/raspi-temp-python.service

systemctl daemon-reload
systemctl disable raspi-temp-python.service
systemctl enable raspi-temp-python.service

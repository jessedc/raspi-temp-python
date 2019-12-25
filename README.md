# Raspberry Pi Temperature Service

Report Raspberry Pi CPU and GPU temperature data to influxdb.

## Setup

- Checkout this repository to to /home/pi/raspi-temp-python
- Update influxdb config in .env.example
- Run `sudo ./install.sh`

## Query this Data

An example query:

```sql
SELECT * FROM "temperature" WHERE "deviceId" = 'pihole' AND "sensor" = 'cpu'
```
"""
CLI Entry point
"""
import argparse
import time
from influxdb import InfluxDBClient
from temperature.influxdb import influx
from temperature.temperature import read_temperature

influx_client = None
influx_db = None


def hostname():
    with open('/etc/hostname', 'r') as content_file:
        return content_file.readline().rstrip('\n')


def main():
    """
    Read temperatures and report to influxdb
    :return:
    """
    parser = argparse.ArgumentParser(description='Collect data from dht22 sensor')
    parser.add_argument('-n', '--deviceId', help='DeviceId for influx measurement. (defaults to /etc/hostname)')
    parser.add_argument('-i', '--influx', help='Influx DB host')
    parser.add_argument('-d', '--database', help='InfluxDB database')
    args = parser.parse_args()

    global influx_db, influx_client
    influx_client = InfluxDBClient(host=args.influx, port=8086)
    influx_db = args.database

    device = hostname() if args.deviceId is None else args.deviceId

    while True:

        cpu, gpu = read_temperature()
        print("Temperature: CPU: {}, GPU: {}".format(cpu, gpu))

        measurements = influx.measurements_for_reading(device, cpu, gpu)
        influx_client.write_points(measurements, database=influx_db)

        time.sleep(5)


if __name__ == "__main__":
    main()

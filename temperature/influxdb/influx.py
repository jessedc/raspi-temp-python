from datetime import datetime, timezone

# https://www.influxdata.com/blog/getting-started-python-influxdb/
# {
#     "measurement": "brushEvents",
#     "tags": {
#         "user": "Carol",
#         "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
#     },
#     "time": "2018-03-28T8:01:00Z",
#     "fields": {
#         "duration": 127
#     }
# }


def measurements_for_reading(device, cpu, gpu):
    timestamp = datetime.now(timezone.utc).astimezone().isoformat()

    return [
        {
            "measurement": "temperature",
            "tags": {
                "sensor": "cpu",
                "deviceId": device
            },
            "time": timestamp,
            "fields": {
                "temp": cpu
            }
        },
        {
            "measurement": "temperature",
            "tags": {
                "sensor": "gpu",
                "deviceId": device
            },
            "time": timestamp,
            "fields": {
                "temp":  gpu
            }
        }
    ]
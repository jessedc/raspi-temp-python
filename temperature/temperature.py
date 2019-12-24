import re
import os


def read_temperature():
    return cpu_temp(), gpu_temp()


def cpu_temp():
    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as content_file:
        content = content_file.readline().rstrip('\n')
        return float(content) / 1000


# simple global regex for parsing the vcgencmd response
re_gpu_tmp = re.compile('temp=([0-9.]{3,})\'C\\n')


def gpu_temp():
    return float(re_gpu_tmp.match(os.popen("/opt/vc/bin/vcgencmd measure_temp").readline()).group(1))

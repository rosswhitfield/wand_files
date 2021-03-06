import os
windows = 4
hostnames = ['ndav1.sns.gov', 'ndav2.sns.gov','ndav3.sns.gov','ndav4.sns.gov','hb2c-analysis.ornl.gov']

node_numbers = windows * len(hostnames)

try:
    window = int(os.environ['WINDOW'])
except KeyError:
    exit("Run in screen")

if window >= windows:
    exit("window out of range")

try:
    hostname = hostnames.index(os.environ['HOSTNAME'])
except ValueError:
    exit("Hostname not in list")

node = hostname * windows + window

print("Node {} out of {}".format(node, node_numbers))

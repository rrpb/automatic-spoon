"""Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]"."""


def defang_ip_address(ip):
    return ip.replace('.', '[.]')

address = "1.1.1.1"
print(defang_ip_address(address))
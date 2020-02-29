import re

ip1 = "192.168.0.450"
ip2 = "192.168.0.1"

def is_valid_ip(ip):
    # pattern = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    # if pattern.findall(ip):
    #     return True
    # return False
    # print(re.match(r"^(\d{1,3}\.)(\d{1,3}\.)(\d{1,3}\.)(\d{1,3}$)", ip).groups(0))
    # print(re.match(r"^(\d{1,3}\.)(\d{1,3}\.)(\d{1,3}\.)(\d{1,3}$)", ip).groups(1))

    if [ 0 <= int(x) < 256 for x in re.split("\.", re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip).group(0))].count(True) == 4:
        return True
    return False


print(is_valid_ip(ip1))
print(is_valid_ip(ip2))
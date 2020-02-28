# def sort_ips(file):
#     with open(file) as f:
#         ip_list = []
#         for line in f.readlines():
#             #print(line, end="") #without sorting
#             ip_list.append(line)
#         ip_list.sort()
#         for ip in ip_list:
#             print(ip, end="")


# # using inbuilt functions
# def sort_ips(file):
#     with open(file) as f:
#         ip_list = [ip.strip() for ip in f.readlines()]
#
#         for ip in sorted(ip_list, key= lambda ip: \
#                             ( int(ip.split('.')[0]),
#                               int(ip.split('.')[1]),
#                               int(ip.split('.')[2]),
#                               int(ip.split('.')[3]))):
#             print(ip)



def sort_ips(file):
    with open(file) as f:
        ip_list = [ip.strip() for ip in f.readlines()]

    for i in range(0, len(ip_list)):
        for j in range(0, len(ip_list) - i -1):
            ip_curr = ip_list[j].split('.')
            ip_next = ip_list[j+1].split('.')

            # if swap(ip_curr, ip_next):
            #     ip_list[j], ip_list[j+1] = ip_list[j+1], ip_list[j]

            # for index in range(0, len(ip_curr)):
            #     if int(ip_curr[index]) == int(ip_next[index]):
            #         continue
            #     elif int(ip_curr[index]) > int(ip_next[index]):
            #         ip_list[j], ip_list[j+1] = ip_list[j+1], ip_list[j]
            #         break
            #     elif int(ip_curr[index]) < int(ip_next[index]):
            #         break

            if ip_curr > ip_next:
                ip_list[j], ip_list[j + 1] = ip_list[j + 1], ip_list[j]



            # if int(ip_curr[0]) > int(ip_next[0]):
            #     ip_list[j], ip_list[j+1] = ip_list[j+1], ip_list[j]
            # if int(ip_curr[0]) == int(ip_next[0]) and int(ip_curr[1]) > int(ip_next[1]):
            #     ip_list[j], ip_list[j+1] = ip_list[j+1], ip_list[j]
            # if int(ip_curr[0]) == int(ip_next[0]) and int(ip_curr[1]) == int(ip_next[1]) and int(ip_curr[2]) > int(ip_next[2]):
            #     ip_list[j], ip_list[j+1] = ip_list[j+1], ip_list[j]
            # if int(ip_curr[0]) == int(ip_next[0]) and int(ip_curr[1]) == int(ip_next[1]) and int(ip_curr[2]) == int(ip_next[2]) and int(ip_curr[3]) > int(ip_next[3]):
            #     ip_list[j], ip_list[j+1] = ip_list[j+1], ip_list[j]

    for ip in ip_list:
        print(ip)


def swap(ip_curr, ip_next):
    for index in range(0, len(ip_curr)):
        if int(ip_curr[index]) == int(ip_next[index]):
            continue
        elif int(ip_curr[index]) > int(ip_next[index]):
            return True
        elif int(ip_curr[index]) < int(ip_next[index]):
            return False
    return False


sort_ips("IP_Address.txt")
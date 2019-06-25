import os
import select
import socket
import struct
import sys
import time

# From /usr/include/linux/icmp.h;
ICMP_ECHO_REQUEST = 8

def icmpCheckSum01(data_string):
	sum_val = 0						# 计算结果
	length = len(data_string)
	odd = length & 0x01	# check the result if odd
	# print(odd)
	# if not odd:

	for i in range(0, length, 2):
		upper = 0
		lower = 0
		if (i + 1) == length:
			upper = lower = 0
		else:
			upper = (ord(data_string[i + 1]) << 8)
			lower = ord(data_string[i])
		# upper = ((i + 1) == length) ? 0 : (ord(data_string[i + 1]) << 8)
		# lower = ((i + 1) == length) ? 0 : ord(data_string[i])
		sum_val += (lower + upper)
	print(sum_val)
		# print(sum_val)
	if odd:
		sum_val += ord(data_string[-1])
		sum_val = sum_val & 0xffffffff
	print(sum_val)
	sum_val = (sum_val >> 16) + (sum_val & 0xffff) 	# adding lower 16 bits with higher 16 bits
	sum_val += (sum_val >> 16) 					# adding over flow bits
	
	print(sum_val)
	return (~sum_val & 0xffff)


def checksum(source_string):
    """
    I'm not too confident that this is right but testing seems
    to suggest that it gives the same answers as in_cksum_val in ping.c
    """
    sum_val = 0
    count_to = (len(source_string) / 2) * 2

    for count in range(0, int(count_to), 2):
        # ord() Converting a char to ascii
        this = ord(source_string[count + 1]) * 256 + ord(source_string[count])
        sum_val = sum_val + this
        sum_val = sum_val & 0xffffffff # Necessary?
    print(sum_val)

    if count_to < len(source_string):

        sum_val = sum_val + ord(source_string[len(source_string) - 1])
        sum_val = sum_val & 0xffffffff # Necessary?
    # print(sum_val)
    sum_val = (sum_val >> 16) + (sum_val & 0xffff)
    sum_val = sum_val + (sum_val >> 16)
    print(sum_val)
    answer = ~sum_val
    answer = answer & 0xffff

    # Swap bytes. Bugger me if I know why.
    answer = answer >> 8 | (answer << 8 & 0xff00)

    return answer

# def chesksum(data):
#     """
#     校验
#     """
#     n = len(data)
#     m = n % 2
#     sum_val = 0 
#     for i in range(0, n - m ,2):
#         sum_val += ord(data[i]) + (ord(data[i+1]) << 8)#传入data以每两个字节（十六进制）通过ord转十进制，第一字节在低位，第二个字节在高位
#     print(sum_val)

#     if m:
#         sum_val += ord(data[-1])
#     #将高于16位与低16位相加
#     sum_val = (sum_val >> 16) + (sum_val & 0xffff)
#     sum_val += (sum_val >> 16) #如果还有高于16位，将继续与低16位相加
#     print(sum_val)
#     answer = ~sum_val & 0xffff
#     #主机字节序转网络字节序列（参考小端序转大端序）
#     answer = answer >> 8 | (answer << 8 & 0xff00)
#     return answer 


def receive_one_ping(my_socket, id, timeout):
	time_left = timeout
	while True:
		start_select = time.time()				# get the current time




def sendOnePing(my_socket, dest_addr, id, psize):
	dest_addr = socket.gethostbyname(dest_addr)	# get address via dns

	# Remove header size from packet size
	psize = psize - 8




if __name__ == '__main__':
	# icmpCheckSum("12346578")
	# print(socket.gethostbyname("127.0.0.1"))
	print(icmpCheckSum01("Hello, world"))
	# (checksum("hello, worl"))
	# (chesksum("hello, world"))

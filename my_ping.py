import os
import select
import socket
import struct
import sys
import time

# From /usr/include/linux/icmp.h;
ICMP_ECHO_REQUEST = 8

def icmpCheckSum(data_string):
	sum_val = 0						# 计算结果
	length = len(data_string)
	odd = length & 0x01	# check the result if odd
	for i in range(0, len(data_string), 2):
		sum_val += ((ord(data_string[i]) << 8) + ord(data_string[i + 1]))
	if odd:
		sum_val += ((ord(data_string[-1]) << 8) & 0xff00)
	sum_val = (sum_val >> 16) + (sum & 0xffff) 	# adding lower 16 bits with higher 16 bits
	sum_val += (sum_val >> 16) 					# adding over flow bits
	return ~sum_val


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
	print(socket.gethostbyname("127.0.0.1"))


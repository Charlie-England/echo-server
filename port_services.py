import socket
import sys

def show_services(port_range_start=0, port_range_end=1000):
    for port in range(port_range_start,port_range_end):
        try:
            print(f"[+] Port:{port} - {socket.getservbyport(port)}")
        except Exception as e:
            pass
            # print(f"[-] Port:{port} not found, {e}")


if __name__=="__main__":
    port_range_start = sys.argv[1]
    port_range_end = sys.argv[2]
    if int(port_range_end) > 65353:
        port_range_end = 65353
    show_services(int(port_range_start),int(port_range_end))
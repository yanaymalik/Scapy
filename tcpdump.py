from scapy.all import *

# rdpcap comes from scapy and loads in our pcap file
packets = rdpcap('CaptureFile.pcap')


#the first byte
pkt = packets[0]
print("The first byte: ", pkt[0], "\n")

#the len of the first packet
print("The packet len: ", len(pkt), "\n")

google_cnt = 0
ynet_cnt = 0
Super_cnt = 0
hello_cnt = 0

for i in range(0, len(packets)):
    pkt = str(packets[i])
    google_cnt +=  pkt.count("google")
    ynet_cnt +=  pkt.count("ynet")
    Super_cnt +=  pkt.count("SuperPhramLogo.gif")
    hello_cnt +=  pkt.count("HelloWorld")
print("google: {0}\nynet: {1}\nSuperPhramLogo.gif: {2}\nHelloWorld: {3}\n".format(google_cnt, ynet_cnt, Super_cnt, hello_cnt))

print("The amount of packets", len(pkt), "\n")

#the max packet
print("the max packet", max([(ind,len(p)) for ind,p in enumerate(packets) if len(p) == max([len(p) for p in packets])]),"\n")

#the min packet
print("the min packet", min([(ind,len(p)) for ind,p in enumerate(packets) if len(p) == min([len(p) for p in packets])]),"\n")

#the host in http get req
a = ["\n".join(x.sprintf("{Raw:%Raw.load%}\n").split(r"\r\n")) for x in packets]
b = [x.split("\n") for x in a]
for p in b:
    if "GET" in p[0]:
        print(p[1])
     
    
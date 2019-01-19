#!/bin/bash
sudo tshark -i any  -Y 'ip.src==10.10.10.1 && tcp.flags.syn==1 && tcp.flags.ack==0' -e frame.time -Tfields  -l > OFEvents.txt

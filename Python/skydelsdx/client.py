#!/usr/bin/python

import socket
import sys
import struct
import time

class Client:
  def __init__(self, address, port, use_connection):
    # Create a TCP/IP socket
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM if use_connection else socket.SOCK_DGRAM)
    self.server_address = (address, port)
    self.port = port
    self.address = address
    
    if use_connection:
      # Connect the socket to the port where the server is listening
      self.sock.connect(self.server_address)

  def __del__(self):
    time.sleep(0.5)
    self.sock.close()
    
  def getPort(self):
    return self.port
    
  def getAddress(self):
    return self.address

  def setTimeout(self, time):
    self.sock.settimeout(time)
  
  def _getPacket(self, size):
    packet = self.sock.recv(size)
    while len(packet) != size:
      chunk = self.sock.recv(size - len(packet))
      packet = packet + chunk
    return packet

  def _msgId2Packet(self, msgId):
    return struct.pack('<B', msgId)
    
  def _getPacketMsgId(self):
    return struct.unpack('<B', self._getPacket(1))[0]

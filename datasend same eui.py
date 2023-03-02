import cayenneLPP
import socket
import time
import ubinascii
import struct
from binascii import hexlify





from network import LoRa
from SI7006A20 import SI7006A20
from pysense import Pysense


py = Pysense()
si = SI7006A20(py)


# Initialise LoRa in LORAWAN mode.
# Please pick the region that matches where you are using the device:
# Asia = LoRa.AS923
# Australia = LoRa.AU915
# Europe = LoRa.EU868
# United States = LoRa.US915
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

print("DevEUI: " + ubinascii.hexlify(lora.mac()).decode('utf-8').upper())


i = 0

while(i == 0):

# create an OTAA authentication parameters

 dev_eui = ubinascii.unhexlify('70B3D549942E25BA')
 app_eui = ubinascii.unhexlify('0000000000000000')
 app_key = ubinascii.unhexlify('1ABB9FA39C3CFB2E58EC58BC1FFA8F16')


 lora.join(activation=LoRa.OTAA, auth=(dev_eui,app_eui,app_key,), timeout=0)




# wait until the module has joined the network
 while not lora.has_joined():
  time.sleep(2.5)
  print('Not yet joined...')


 print('Joined')

 time.sleep(20)


# create a LoRa socket
 s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
 s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)


# make the socket blocking
# (waits for the data to be sent and for the 2 receive windows to expire)
 s.setblocking(True)

 lpp = cayenneLPP.CayenneLPP(size = 100, sock = s)

# send some data
 lpp.add_relative_humidity(si.humidity())
 lpp.add_temperature(si.temperature(), channel = 118)
 lpp.send(reset_payload = True)
 print("[" + str(time.time()) + "] sending Temperature ")



 time.sleep(8) #sleep 1 second


    # make the socket non-blocking
# (because if there's no data received it will block forever...)
 s.setblocking(False)

# get any data received (if any...)
 data = s.recv(64)
 print(data)


 i = i + 1

 time.sleep(180)

else:

 while True:

     if data == (b'') and i == 1 :

         same_key = ubinascii.hexlify(app_key)
         print("To kleidi den allaxe")

         dev_eui = ubinascii.unhexlify('70B3D549942E25BA')
         app_eui = ubinascii.unhexlify('0000000000000000')
         app_key = ubinascii.unhexlify(same_key)

         lora.join(activation=LoRa.OTAA, auth=(dev_eui,app_eui,app_key,), timeout=0)

         while not lora.has_joined():
          time.sleep(2.5)
          print('Not yet joined...')


         print('Joined')

         time.sleep(20)

         s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

         s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

         s.setblocking(True)

         lpp = cayenneLPP.CayenneLPP(size = 100, sock = s)

         lpp.add_relative_humidity(si.humidity())
         lpp.add_temperature(si.temperature(), channel = 118)
         lpp.send(reset_payload = True)
         print("[" + str(time.time()) + "] sending Temperature ")



         time.sleep(7) #sleep 1 second

         s.setblocking(False)

          # get any data received (if any...)
         data = s.recv(64)
         print(data)

         time.sleep(180)

     elif data != (b'') :

         new_key = ubinascii.hexlify(data)
         print(new_key)

         print("To kleidi allaxe")

         i = i + 1

         dev_eui = ubinascii.unhexlify('70B3D549942E25BA')
         app_eui = ubinascii.unhexlify('0000000000000000')
         app_key = ubinascii.unhexlify(new_key)



         lora.join(activation=LoRa.OTAA, auth=(dev_eui,app_eui,app_key,), timeout=0)




          # wait until the module has joined the network
         while not lora.has_joined():
          time.sleep(2.5)
          print('Not yet joined...')


         print('Joined')

         time.sleep(20)


          # create a LoRa socket
         s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

          # set the LoRaWAN data rate
         s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)


          # make the socket blocking
          # (waits for the data to be sent and for the 2 receive windows to expire)
         s.setblocking(True)

         lpp = cayenneLPP.CayenneLPP(size = 100, sock = s)

          # send some data
         lpp.add_relative_humidity(si.humidity())
         lpp.add_temperature(si.temperature(), channel = 118)
         lpp.send(reset_payload = True)
         print("[" + str(time.time()) + "] sending Temperature ")


         time.sleep(7) #sleep 1 second

              # make the socket non-blocking
          # (because if there's no data received it will block forever...)
         s.setblocking(False)

          # get any data received (if any...)
         data = s.recv(64)
         print(data)

         old_key = new_key

         time.sleep(177)

     else:

          print(old_key)

          print("To kleidi  den allaxe 2o")

          dev_eui = ubinascii.unhexlify('70B3D549942E25BA')
          app_eui = ubinascii.unhexlify('0000000000000000')
          app_key = ubinascii.unhexlify(old_key)



          lora.join(activation=LoRa.OTAA, auth=(dev_eui,app_eui,app_key,), timeout=0)
        



           # wait until the module has joined the network
          while not lora.has_joined():
           time.sleep(2.5)
           print('Not yet joined...')


          print('Joined')

          time.sleep(20)


           # create a LoRa socket
          s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

           # set the LoRaWAN data rate
          s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)


           # make the socket blocking
           # (waits for the data to be sent and for the 2 receive windows to expire)
          s.setblocking(True)

          lpp = cayenneLPP.CayenneLPP(size = 100, sock = s)

           # send some data
          lpp.add_relative_humidity(si.humidity())
          lpp.add_temperature(si.temperature(), channel = 118)
          lpp.send(reset_payload = True)
          print("[" + str(time.time()) + "] sending Temperature ")



          time.sleep(7) #sleep 1 second




               # make the socket non-blocking
           # (because if there's no data received it will block forever...)
          s.setblocking(False)

           # get any data received (if any...)
          data = s.recv(64)
          print(data)

          time.sleep(177)

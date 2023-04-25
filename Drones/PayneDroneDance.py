# Meredith Payne
# Period 7, February 9, 2022
# Honorbound

# Import the necessary modules
import socket
import threading
import time

# IP and port of Tello
tello_address = ('192.168.10.1', 8889)

# IP and port of local computer
local_address = ('', 9000)

# Create a UDP connection that we'll send the command to
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the local address and port
sock.bind(local_address)

# Send the message to Tello and allow for a delay in seconds
def send(message, delay):
  # Try to send the message otherwise print the exception
  try:
    sock.sendto(message.encode(), tello_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))

  # Delay for a user-defined period of time
  time.sleep(delay)

# Receive the message from Tello
def receive():
  # Continuously loop and listen for incoming messages
  while True:
    # Try to receive the message otherwise print the exception
    try:
      response, ip_address = sock.recvfrom(128)
      print("Received message: " + response.decode(encoding='utf-8'))
    except Exception as e:
      # If there's an error close the socket and break out of the loop
      sock.close()
      print("Error receiving: " + str(e))
      break

# Create and start a listening thread that runs in the background
# This utilizes our receive functions and will continuously monitor for incoming messages
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

# Initiate command mode and takeoff
def takeoff():
  send("command", 3)
  send("takeoff", 5)

# Land
def land():
  send("land", 5)

# Tello commands respond with an OK when sucessful. This means Tello recognizes
# the command, but the instruction hasn't completed. OK is Tello saying "I got
# the message" but not necessarily saying "I completed the command"
# This means we need to calculate how long the spin will take before we execute the next command.
# Based on our tests a single 360 rotation takes 7 seconds. We'll use this in our spin function to delay
# before the next command. Your rotation time may vary. You can calculate this by
# sending a "cw 360" or "ccw 360" command and measuring the rotation time.

# Post Conditions:
# xRange: +499
# yRange: 0
# zRange: +120
# orientation: 0 degrees
# speed change: 0
def hoganDance():
   print("Starting Hogan Dance")
   send("up 200", 4)
   send("cw 90", 4)
   send("forward 499", 4)
   send("cw 270", 4)
   send("down 80", 4)
   
#Post Conditions:
# xRange (left/right): +50
# yRange (forward/backward): 0
# zRange (up/down): +20
# orientatoin: 0 degrees
# speed change: 0   
def hoverDance():
   print("starting hoverDance")
   send ("up 50", 4)
   send ("down 30", 4)
   send ("cw 270", 5)
   send ("ccw 270", 4)
   
# Post Conditions:
# xRange (right/left): 0
# yRange (forward/backward): +50
# zRange (up/down): +20
# orientation: 0 degrees
# speed change: 0
def mathewDance():
   print("Starting Mathew Dance")
   send("forward 30", 3)
   send("cw 360", 7)
   send("up 30", 4)
   send("down 40", 5)
   send("up 30" , 4)
   send("flip f", 3)
   

#post conditions:
# xrange (left/right): 0
# yrange (forward/back):-150
# zrange (up/down): 0
# orientation: 0
# speed: 0
def lewisDance():
   print("starting lewisDance")
   send("forward 150", 5)
   send("flip b", 3)
   send("backward 150", 4)
   send("left 150", 4)
   
   
#Post Conditions:
#xRange: +50 to -50 (0 net) 
#yRange: +50 to - 50 (0 net)
#zRange: stays the same
#orientation: 0
#speed: +60
def payneDance():
   print("Starting payneDance")
   send("speed 60",4)
   send("left 50", 4)
   send("right 50", 4) 
   send("forward 50", 4)
   send("back 50",4)
   send("flip f",4)
   send("flip b", 4)

# Post Conditions:
# xRange (right/left):
# yRange (forward/backward): 90 - 90
# zRange (up/down): 150 - 150
# Orientation: 360 degrees
# Speed:
def tannerDance():
   print("starting tannerDance")
   send("up 150", 3)
   send("forward 90", 3)
   send("ccw 360", 5)
   send("back 90", 2)
   send("flip f", 5)
   send("down 150", 2)
   
# Post Conditions:
#xRange (right/left): 0
#yRange (forward/back): 200
#zRange (up/down): 100
#orientation: 0 degrees
#speed change: 0
def simonsDance():
   print("starting simonsDance")
   send("up 300", 3)
   send("forward 200", 2)
   send ("flip l", 4)
   send("up 200", 4)
   send ("flip r", 4)
   send("down 400", 6)

#Post Conditions:
# xRange (left/right): -70
# yRange (forward/backward): 0
# zRange (up/down): +60
# oreientation: 0 degrees
# speed change: 0
def ashmoreDance():
   print("starting ashmoreDance")
   send("up 20", 2)
   send("down 40", 4)
   send("up 80", 4)
   send("flip b", 3)
   send("left 70", 3)

# Post Conditions:
# xRange: +0 (left and right)
# yRange: +30 (forwards and backwards)
# zRange: -30 (up and down)
# orientation: 90 degrees
# speed change: 0
def alarconDance():
   print("starting alarconDance")
   send("cw 90", 3)
   send("down 30", 3)
   send("forward 30", 4)
   send("flip f", 3)
   send("flip b", 3)

#Post Conditions:
# xRange: 0 (left right)
# yRange: 0 (forward backward)
# zRange: 0 (up down)
# orientation: 0
# speed change: 0
def winnDance():
   print("starting winnDance")
   send("left 50",3)
   send("up 30",2)
   send("left 30",2)
   send ("right 70",3)
   send("down 30",2)
   send("right 30",2)
   send("left 30",4)
   send("flip f",1)
   send("ccw 180",1)
 
# Post Conditions:
# xRange(right/left): 0
# yRange(forward/backward): 50
# zRange (up/down): 0
# orientation: 0 degree
# speed change: 0  
def mckerrowDance():
   print("starting mckerrowDance")
   send("up 100", 5)
   send("flip b", 4)
   send("down 100", 3)
   send("up 100", 4)
   send("back 50", 5)
   send("flip f", 4)
   send("forward 100", 3)

# Call the methods to takeoff, dance and land
takeoff()
hoganDance()
hoverDance()
mathewDance()
lewisDance()
payneDance()
tannerDance()
simonsDance()
ashmoreDance()
alarconDance()
winnDance()
mckerrowDance()
land()

# Print message
print("Mission completed successfully!")

# Close the socket
sock.close()
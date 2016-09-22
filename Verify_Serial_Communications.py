#############################################################################################
#############################################################################################
#
#   The MIT License (MIT)
#   
#   Copyright (c) 2016 http://odelay.io 
#   
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#   
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#   
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.
#   
#   Contact : <everett@odelay.io>
#
#   Description: Created a quick script to check serial power between two boards.
#   
#   Version History:
#   
#       Date        Description
#     -----------   -----------------------------------------------------------------------
#      20SEP2016     Original Creation
#
#############################################################################################
#############################################################################################

import serial
import string
import random
from time import gmtime, strftime
import time

#VERBOSE         = True
VERBOSE         = False

#baudrate        = 9600
baudrate        = 115200
#baudrate        = 960000
charLen         = 256
loopLen         = 1024

uutUSB          = serial.Serial()
uutUSB.port     = "COM13"
uutUSB.baudrate = baudrate
uutUSB.timeout  = .2
uutUSB.open()

refUSB          = serial.Serial()
refUSB.port     = "COM10"
refUSB.baudrate = baudrate
refUSB.timeout  = .2
refUSB.open()

#--------------------------------------------------------------------------
# Grab time at start of test
#--------------------------------------------------------------------------
start_time = time.time()

print "\n\n"
print "Test Started : " + str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

#--------------------------------------------------------------------------
# Funcation to create the string (found on web, unknown source)
#--------------------------------------------------------------------------
def randString(size=1024, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

#--------------------------------------------------------------------------
# Check UUT receiver
#--------------------------------------------------------------------------
p_recv = 0
f_recv = 0
for x in range(0,loopLen):

  if(VERBOSE):
    print "Iteration: " + str(x)

  a = randString(charLen) + "\n"
  refUSB.write(a);
  b = uutUSB.readline()
  
  if(VERBOSE):
    print "Receiving " + str(charLen) + " characters from UUT"
  
  if(a == b):
    if(VERBOSE):
      print "Success."
    p_recv = p_recv + 1
  else:
    if(VERBOSE):
      print "Failed."
    f_recv = f_recv + 1
 
  if(VERBOSE):
    print "SENT: " + str(a) + "RECV: " + str(b)
    print "-------------------------------------\n"


#--------------------------------------------------------------------------
# Check UUT transmitter
#--------------------------------------------------------------------------
p_send = 0
f_send = 0
for x in range(0,loopLen):

  if(VERBOSE):
    print "Iteration: " + str(x)
  a = randString(charLen) + "\n"
  uutUSB.write(a);
  b = refUSB.readline()

  if(VERBOSE):
    print "Sending " + str(charLen) + " characters from UUT"

  if(a == b):
    if(VERBOSE):
      print "Success."
    p_send = p_send + 1
  else:
    if(VERBOSE):
      print "Failed."
    f_send = f_send + 1

  if(VERBOSE):
    print "SENT: " + str(a) + "RECV: " + str(b)
    print "-------------------------------------\n"

elapsed_time = time.time() - start_time

#--------------------------------------------------------------------------
# Print results
#--------------------------------------------------------------------------
print "Test Ended   : " + str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print "\n"
print "  BAUD Rate          = " + str(baudrate)
print "  Message Size       = " + str(charLen)
print "  Number of Messages = " + str(loopLen)
print "\n"
print "  Elapsed Time       = " + str(elapsed_time)
print "  Sending characters from UUT"
print "    Number of Success  = " + str(p_send)
print "    Number of Fails    = " + str(f_send)
print "  Receiving characters from UUT"
print "    Number of Success  = " + str(p_recv)
print "    Number of Fails    = " + str(f_recv)
print "\n"

uutUSB.close()
refUSB.close()

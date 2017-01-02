import RPi.GPIO as GPIO
import time
import sys

#GPIO pins to be translated into parallel
STROBE = 3
RESET = 2
P1 = 7
P2 = 8
P3 = 25
P4 = 24
P5 = 23
P6 = 18
P7 = 15
P8 = 14



"""
Prints a binary string from an ASCII char on the VFD
"""
def printToVFD( c ):
    if c[0] == '0':
	GPIO.output(P1, False)
    else:
        GPIO.output(P1, True)
    if c[1] == '0':
       	GPIO.output(P2, False)
    else:
       	GPIO.output(P2, True)
    if c[2] == '0':
       	GPIO.output(P3, False)
    else:
       	GPIO.output(P3, True)
    if c[3] == '0':
       	GPIO.output(P4, False)
    else:
       	GPIO.output(P4, True)
    if c[4] == '0':
       	GPIO.output(P5, False)
    else:
       	GPIO.output(P5, True)
    if c[5] == '0':
       	GPIO.output(P6, False)
    else:
       	GPIO.output(P6, True)
    if c[6] == '0':
       	GPIO.output(P7, False)
    else:
       	GPIO.output(P7, True)
    if c[7] == '0':
       	GPIO.output(P8, False)
    else:
       	GPIO.output(P8, True)
    """
    Flashes the strobe. Wait is used because
    the VFD requires this much time to process the ASCII data
    """
    GPIO.output(STROBE, True)
    time.sleep(0.0005)
    GPIO.output(STROBE, False)
    time.sleep(0.0005)
    return


def main():
#Sets gpio mode and sets up pins for output
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(STROBE, GPIO.OUT)
    GPIO.setup(RESET, GPIO.OUT)
    GPIO.setup(P1, GPIO.OUT)
    GPIO.setup(P2, GPIO.OUT)
    GPIO.setup(P3, GPIO.OUT)
    GPIO.setup(P4, GPIO.OUT)
    GPIO.setup(P5, GPIO.OUT)
    GPIO.setup(P6, GPIO.OUT)
    GPIO.setup(P7, GPIO.OUT)
    GPIO.setup(P8, GPIO.OUT)
	
    #Calls the reset pin in order to blank out the VFD.
    GPIO.output(RESET, True)
    time.sleep(0.0005)
    GPIO.output(RESET, False)
    time.sleep(0.0005)
    n = sys.stdin.read()
    #n = raw_input("Enter an ascii string: ")
		
    #Takes input string from stdin and prints to 
    #the VFS
    for c in n:
	if c != '\n':
	    c = bin(ord(c))[2:].zfill(8)
            printToVFD( c )

    #cleans up GPIO on program exit
	
if __name__ == "__main__":
	main()

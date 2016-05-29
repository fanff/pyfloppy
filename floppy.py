import serial
import time
import logging

import logging





def A(self,fid):
    self.sendSound(fid,4300)
def B(self,fid):
    self.sendSound(fid,3800)
def C(self,fid):
    self.sendSound(fid,3500)
def D(self,fid):
    self.sendSound(fid,3100)
def E(self,fid):
    self.sendSound(fid,2700)
def F(self,fid):
    self.sendSound(fid,2270)
def F(self,fid):
    self.sendSound(fid,2100)
def G(self,fid):
    self.sendSound(fid,3500)
def A2(self,fid):
    self.sendSound(fid,2150)



PORTNAME  ="/dev/ttyACM0" 
def convert(value):
    hi = value/256
    lo = value -hi*256 
    
    #print hi,lo,hi*256+lo
    return hi,lo
class FloppyPlayer():

    def __init__(self,ser):
        self.ser = ser

        self.played = {}
        for i in range(6):
            self.played[i] = None

    def sendSound(self,fid,value):
        """
        Send a note to floppy drive
        """
        log = logging
        hi,lo = convert(value)
        log.debug("sending floopy %s : %s",fid,value)
        data = bytearray([fid,hi,lo])
        self.ser.write(data)
        self.ser.flush()

    def stopAll(self):
        log = logging
        for fid in range(6):
            self.sendSound(fid,0)

    
    def playNote(self,per):
        fid = self.findAvailable()
        if fid <> None:
            self.sendSound(fid,per)
            self.played[fid] = per
        else:
            pass
            #TODO STACK

    def stopNote(self,per):
        fid = self.findPer(per)
        if fid <> None:
            self.sendSound(fid,0)
            self.played[fid] = None
            #TODO unstack
            

    def findPer(self,per):
        for k,v in self.played.items():
            if v == per:
                return k
    def findAvailable(self):
        for k,v in self.played.items():
            if v == None:
                return k
        

def getserial(portname=PORTNAME):
    log = logging.getLogger("getserial")
    ser = serial.Serial(portname,
                     baudrate=115200,
                     bytesize=serial.EIGHTBITS,
                     parity=serial.PARITY_NONE,
                     stopbits=serial.STOPBITS_ONE,
                     timeout=1,
                     xonxoff=0,
                     rtscts=0)

    ser.setDTR(False)
    time.sleep(1)
    ser.flushInput()
    ser.setDTR(True)

    log.debug("opened")
    cont = True
    ser.flush()
    while (cont):
        log.debug( "try read")
        res = ser.read()
        if "#" in res:
            log.debug( "read : %s", res)
            cont = False

        time.sleep(0.1)
    

    ser.write("l")
    ser.flush()
    time.sleep(1)
    # end init 
    return ser

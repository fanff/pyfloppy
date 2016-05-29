import serial
import time
import logging

from floppy import FloppyPlayer,getserial


def main():

    log = logging.getLogger("mainfunction")
    log.debug("inmain")
    
    ser= getserial() 
    fp = FloppyPlayer(ser) 
    fp.sendSound(1,4500)
    time.sleep(10)
    # 3600 C
    # 3800 B
    # 4060 A#
    # 4XXX A

    fp.stopAll()
        
    


        



NOTES = [A,B,C,D,E,F,G,A2]

def sendSound(ser,value):
    """
    Send a note to floppy drive
    """
    log = logging
    hi,lo = convert(value)
    log.debug("sending floopy %s",value)
    for fid in range(1):
        data = bytearray([fid,hi,lo])
        ser.write(data)
        ser.flush()



def convert(value):
    hi = value/256
    lo = value -hi*256 
    
    #print hi,lo,hi*256+lo
    return hi,lo


if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)
    main()


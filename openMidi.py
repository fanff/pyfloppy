
import wave
import argparse
import numpy as np


from pprint import pprint
if __name__=="__main__":

    
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('infile',type=str,help="")

    args = parser.parse_args()

    wf = wave.open(args.infile,"r")
    
    params= dict(zip(("nchannels","sampwidth","framerate","nframes","comptype","compname"),wf.getparams()))
    
    pprint(params)
    def toInt(framestr):
        if len(framestr)>0:
            l = ord(framestr[0])
            h = ord(framestr[1])
            return l+(h*255)
        else:
            print "end frame ?"
            return 0
    
    asList = [toInt(wf.readframes(1)) for i in range(0,params["nframes"])]
        

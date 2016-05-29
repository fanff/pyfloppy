
import pyaudio
import sys
from array import array


chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100 *2
RECORD_SECONDS = 5

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS, 
                rate=RATE, 
                input=True,
                output=True,
                frames_per_buffer=chunk)

print "* recording"
for i in range(0, RATE / chunk * RECORD_SECONDS):

    print "here"
    data = stream.read(chunk)
    # check for silence here by comparing the level with 0 (or some threshold) for 
    # the contents of data.
    # then write data or not to a file
    as_ints = array('h', data)

    print sum((abs(i) for i in as_ints))
print "* done"

stream.stop_stream()
stream.close()
p.terminate()



####################
##AttentionGrabber##
#######################################################################
##This Limits OR "focuses" the output of MindwaveMobile parser to the##
##AttentionDataPoint(dataPoint)########################################
#################################
#First, we grab our input from the MindwaveMobile
import time
import bluetooth
from MindwaveDataPoints import RawDataPoint

##Added following to stock files from Neurosky DEV
from MindwaveDataPoints import AttentionDataPoint
##
from MindwaveDataPointReader import MindwaveDataPointReader

if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()
	
    while(True):
        dataPoint = mindwaveDataPointReader.readNextDataPoint()
        if (dataPoint.__class__ is AttentionDataPoint):
            print dataPoint
#I opted to let the DevKit do most of the work for me
## we will just take the individual datapoints as seen in
## the real-time readout from Neurosky and focus on AttentionDataPoint(dataPoint)
####################
##Meditation##
#######################################################################
##This Limits OR "focuses" the output of MindwaveMobile parser to the##
##MeditationDataPoint(dataPoint)########################################
#################################
#First, we grab our input from the MindwaveMobile
import time
import bluetooth
from MindwaveDataPoints import RawDataPoint
from MindwaveDataPointReader import MindwaveDataPointReader
##Added following to stock files from Neurosky
from MindwaveDataPoints import MeditationDataPoint
##Now we need to display the Meditation Value each time it is next in the queue

if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()

    while(True):
        dataPoint = mindwaveDataPointReader.readNextDataPoint()
##EDIT
        if (dataPoint.__class__ is MeditationDataPoint):
            print dataPoint
##

import time
import bluetooth
from MindwaveDataPoints import RawDataPoint
from MindwaveDataPointReader import MindwaveDataPointReader
##Added following to stock files from Neurosky
from MindwaveDataPoints import MeditationDataPoint
##

if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()

    while(True):
        dataPoint = mindwaveDataPointReader.readNextDataPoint()
##EDIT
        if (dataPoint.__class__ is MeditationDataPoint):
            print dataPoint
##

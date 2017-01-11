import time
import bluetooth
from MindwaveDataPoints import RawDataPoint
#Added following to stock files from Neurosky
from MindwaveDataPoints import MeditationDataPoint
#
from MindwaveDataPointReader import MindwaveDataPointReader


if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()

    while(True):
        dataPoint = mindwaveDataPointReader.readNextDataPoint()
        if (dataPoint.__class__ is MeditationDataPoint):
            print dataPoint

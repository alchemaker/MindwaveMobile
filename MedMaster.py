##Meditation Master##
#Built on the same principals as AttenGrabber
import time
import bluetooth
from MindwaveDataPoints import RawDataPoint
from MindwaveDataPoints import AttentionDataPoint
from MindwaveDataPointReader import MindwaveDataPointReader


if __name__ == '__main__':
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()

    while(True):
        dataPoint = mindwaveDataPointReader.readNextDataPoint()
        if (dataPoint.__class__ is AttentionDataPoint):
            print dataPoint

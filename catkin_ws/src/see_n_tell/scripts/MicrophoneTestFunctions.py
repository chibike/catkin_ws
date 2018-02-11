import sounddevice as sd
import numpy as np

def printDevices():
    print '--- Devices ---'
    print sd.query_devices()

def getDevice(name = u'ASTRA S: USB Audio (hw:2,0)'):
    devices = sd.query_devices()
    for i in range(len(devices)):
        if devices[i]['name'] == name:
            return devices[i]
    return None

def setDefaultDevice(device=None):
    sd.default.device = device

def setDefaultSampleRate(fs=48000):
    sd.default.samplerate = fs

def setDefaultChannel(channels=2):
    sd.default.channels = channels
    
def playSoundFs(array=[], fs=44100):
    sd.play(array, fs)

def playSound(array=[]):
    sd.play(array)

def stopSound():
    sd.stop()

def getRecording(duration=10.5, fs=44100, blocking=False):#duration = sec
    return sd.rec(int(duration * fs), samplerate=fs, channels=2, blocking=blocking, dtype='float64')

def waitUntilFinished():
    return sd.wait()

def simPlay_n_Rec(array=[], fs=44100, channels=2):
    myrecording = sd.playrec(array, fs, channels, dtype='float64', blocking = False)

def stream_callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    #outdata[:] = indata
    print type(indata),type(outdata),frames,time

def inputstream_callback(indata, frames, time, status):
    if status:
        print(status)
    #outdata[:] = indata
    print type(indata),frames,time

def outputstream_callback(outdata, frames, time, status):
    if status:
        print(status)
    #outdata[:] = indata
    print type(outdata),frames,time


def startOutputStream(duration):
    p = sd.OutputStream(channels=2, callback=outputstream_callback)
    p.start()
    sd.sleep(int(duration * 1000))
    p.close()

def startInputStream(duration):
    p = sd.InputStream(channels=2, callback=inputstream_callback)
    p.start()
    sd.sleep(int(duration * 1000))
    p.close()

def startStream(duration):
    p = sd.Stream(channels=2, callback=stream_callback)
    p.start()
    sd.sleep(int(duration * 1000))
    p.close()

def testMic_n_Speaker():
    s = getRecording(duration=5, blocking=True)
    playSoundFs(s)

def getCalibrationData(l1,r1,l2,r2):
    dl = l2 - l1
    dr = r2 - r1
    m = dl/dr
    k = (r2 - (m*l2)) + (r1 - (m*l1))
    k = k/2.0
    #n_dl = m*dl - k
    return [m, -k]

def getCalibrationDataf(quiet_signal, noisy_signal):
    l1 = np.average(quiet_signal[:,0])
    r1 = np.average(quiet_signal[:,1])
    
    l2 = np.average(noisy_signal[:,0])
    r2 = np.average(noisy_signal[:,1])
    
    return getCalibrationData(l1,r1,l2,r2)

def testCalibf(s1, m, k, index):
    print "Before:", s1[index,0], 'vs', s1[index, 1], 'diff =', abs(s1[index,0] - s1[index, 1])
    print "After:", s1[index,0]*m + k, 'vs', s1[index, 1], 'diff =', abs((s1[index,0]*m + k) - s1[index, 1])

if __name__ == "__main__":
    testMic_n_Speaker()

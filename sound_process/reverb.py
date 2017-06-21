from django.db.models import Model
from django.shortcuts import redirect
from scipy import signal

from MultiMedia_Project.settings import MEDIA_ROOT, DIRECT_ROOT
from sound_process.utility.sound_util import *


def reverb(id):
    source = wave.open(DIRECT_ROOT + '/Fe_sp_1.wav', 'r')
    nChannels = source.getnchannels()
    sampWidth = source.getsampwidth()  # sampling width
    FrameRate = source.getframerate()  # sampling rate
    nFrames = source.getnframes()

    revb = wave.open(DIRECT_ROOT + '/Reverberation.wav', 'r')

    source_str = wav2str(source)
    revb_str = wav2str(revb)

    output = wave.open(DIRECT_ROOT + '/temp.wav', 'w')

    if nChannels == 1:
        revb_output = signal.lfilter(revb_str, [1.], source_str) / np.max(np.abs(revb_str))

        output.setparams((1, sampWidth, FrameRate, nFrames, 'NONE', 'not compressed'))
        copyWav(output, revb_output)
    elif nChannels == 2:
        revb_output = np.transpose(np.vstack((
            signal.lfilter(revb_str, [1.], source_str[:, 0]) / np.max(np.abs(revb_str)),
            signal.lfilter(revb_str, [1.], source_str[:, 1]) / np.max(np.abs(revb_str))
        )))
        output.setparams((2, sampWidth, FrameRate, nFrames, 'NONE', 'not compressed'))
        copyWav2(output, revb_output)
    source.close()
    revb.close()
    output.close()

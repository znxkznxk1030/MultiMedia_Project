import numpy as np
import wave
import os
import subprocess
import ffmpy

import struct

import pydub
from pydub import AudioSegment

from MultiMedia_Project.settings import DIRECT_ROOT

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_DIR = DIRECT_ROOT

aiz = "00"
hl_file = file_DIR + "L0e0" + aiz + "a.wav"
hr_file = file_DIR + "R0e0" + aiz + "a.wav"
sound_file = "sound/gd_wav.wav"
noise_file = "sound/W2.wav"


def stereo2mono(src: np.array):
    d = (src[:, 0] + src[:, 1]) / 2
    return d


def mono2stereo(dest: wave.Wave_write, src_l: str, src_r: str):
    duration = min(len(src_l), len(src_r))
    for i in range(duration):
        l = src_l[i]
        r = src_r[i]
        packed_value = struct.pack('<hh', np.int16(l), np.int16(r))
        dest.writeframes(packed_value)


def copyWav(dest: wave.Wave_write, src):
    for i in src:
        packed_value = struct.pack('<h', np.int16(i))
        dest.writeframes(packed_value)


def copyWav2(dest: wave.Wave_write, src):
    for i in src:
        packed_value = struct.pack('<hh', np.int16(i[0]), np.int16(i[1]))
        dest.writeframes(packed_value)


def getWavStr(file_dir, mode):
    try:
        source = wave.open(file_dir, mode)
        source_raw = source.readframes(-1)
        source_raw = np.fromstring(source_raw, 'Int16')

        print(file_dir, source.getnchannels())

        return source_raw
    except FileExistsError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)


def wav2str(input_sound: wave.Wave_read):
    source_signal = input_sound.readframes(-1)

    if input_sound.getnchannels() == 1:
        source_signal = np.fromstring(source_signal, 'Int16')
    else:
        source_signal = np.fromstring(source_signal, 'Int16')
        source_signal = np.array(np.reshape(source_signal, (input_sound.getnframes(), 2)))
    return source_signal


def stereo2str(input: wave.Wave_read):
    source_signal = input.readframes(-1)
    source_signal = np.fromstring(source_signal, 'Int16')

    source_signal = np.array(np.reshape(source_signal, (input.getnframes(), 2)))

    return source_signal


def incVolume(wav_name):
    src = AudioSegment.from_wav(file_DIR + wav_name + '.wav')
    src = src - 10
    src.export(file_DIR + wav_name + '_dec' + '.wav', format='wav')


def decVolume(wav_name):
    src = AudioSegment.from_wav(file_DIR + wav_name + '.wav')
    src = src - 10
    src.export(file_DIR + wav_name + '_dec' + 'wav', format='wav')


def synthesize(src1: np.array, src2: np.array):
    return src1 + src2


def mpeg2wav(mp3_name):
    # ff = ffmpy.FFmpeg(
    #     inputs={file_DIR + mp3_name + '.mp3': None},
    #     outputs={file_DIR + mp3_name + '_wav' + '.wav': None}
    # )
    #
    # ff.run()

    pydub.AudioSegment.ffmpeg = file_DIR + "/ffmpeg-3.3.2.tar.bz2"
    src = AudioSegment.from_mp3(file_DIR + mp3_name + '.mp3')
    src.export(file_DIR + mp3_name + '_wav.wav', format='wav')
    return file_DIR + mp3_name + '_wav.wav'


def float2int16(str):
    return np.fromstring(str, 'Int16')


def lms(u, d, M, step, leak=0, initCoeffs=None, N=None, returnCoeffs=False):
    if N is None:
        N = len(u) - M + 1

    initCoeffs = np.zeros(M)

    # Initialization
    y = np.zeros(N)  # Filter output
    e = np.zeros(N)  # Error signal
    w = initCoeffs  # Initialise equaliser
    leakstep = (1 - step * leak)
    if returnCoeffs:
        W = np.zeros((N, M))  # Matrix to hold coeffs for each equaliser step

    # Equalise
    for n in range(N):

        x = np.flipud(u[n:n + M])  #

        y[n] = np.dot(x, w)

        e[n] = d[n + M - 1] - y[n]

        w = leakstep * w + step * x * e[n]

        y[n] = np.dot(x, w)

        if returnCoeffs:
            W[n] = w

        if returnCoeffs:
            w = W

    return y, e, w

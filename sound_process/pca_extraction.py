import pydub
from numpy import *
from scipy import fftpack

from sound_process.utility.sound_util import *


def primary_extract():
    file_type = '.wav'
    mp3_file = '.mp3'

    # path of files (.wav)

    untitled_name = '/gd'
    input_name = '/booster'
    output_name = '/primary_example'
    hl_name = '/L0e' + '00' + '0a'
    hr_name = '/R0e' + '00' + '0a'
    noi_name = '/W2'
    primary_name = '/ret_primary'
    ambient_name = '/ret_ambient'
    synth_name = '/ret_synth'

    untitled_path = file_DIR + untitled_name + '.mp3'
    input_path = file_DIR + input_name + '.wav'
    output_path = file_DIR + output_name + '.wav'
    hl_path = file_DIR + hl_name + '.wav'
    hr_path = file_DIR + hr_name + '.wav'
    noi_path = file_DIR + noi_name + '.wav'
    primary_path = file_DIR + primary_name + '.wav'
    ambient_path = file_DIR + ambient_name + '.wav'
    synth_name = file_DIR + synth_name + '.wav'

    file_name, file_extensiton = os.path.splitext(untitled_path)

    if file_extensiton == '.mp3':
        input_path = mpeg2wav(untitled_name)

    # open source file and get params

    input = wave.open(input_path)
    nChannels = input.getnchannels()
    FrameRate = input.getframerate()
    sampWidth = input.getsampwidth()  # sampling width
    nFrames = input.getnframes()
    print(input)
    # open impulse file and change str

    # hl = wav2str(wave.open(hl_path, 'r'))
    # hr = wav2str(wave.open(hr_path, 'r'))
    noise = wav2str(wave.open(noi_path, 'r'))

    # check sound channel

    if nChannels == 2:
        source = wav2str(input)
        lenSource = len(source[:, 0])
    else:
        source = wav2str(input)
        lenSource = len(source)
        source = np.transpose(np.vstack((source, source)))

    # synthesize noise

    if len(noise) > lenSource:
        noise = noise[:lenSource, :]
    else:
        source = source[:int(lenSource / 10), :]
        lenSource = len(source)

    # source = synthesize(source, noise)

    # create stereo window function
    # - hanning function (nfft : 4096, N : 2048)

    nfft = 516
    N = int(nfft / 2)

    hanning2 = zeros((N, 2))
    hanning2[:, 0] = hanning(N)
    hanning2[:, 1] = hanning(N)

    hanning1 = hanning2

    hanning2 = np.vstack((hanning2, hanning2))

    # define frequency parameters

    n = int(len(source) / nChannels)
    k = np.arange(n)
    T = n / FrameRate
    frq = k / T
    frq = frq[range(int(n / 2))]

    # define parameters

    frame = int(lenSource / N)

    init = 1.e-4
    lamb = 0.8

    xp = zeros((N, 2))

    xout_pre = zeros(N)
    XL = zeros((N, 1))
    XR = zeros((N, 1))

    psd = ones((2, 2, N)) * init

    Sest = zeros(N)
    Nlest = zeros(N)
    Nrest = zeros(N)

    OutVec = empty(0)
    OutAmbL = empty(0)
    OutAmbR = empty(0)

    temp = 0
    band = 1000

    for i in range(frame):
        subSignal = source[i * N: (i + 1) * N, :]

        print("%d %s %d" % (i, '/', frame))

        XVL = fftpack.rfft(subSignal[:, 0])
        XVR = fftpack.rfft(subSignal[:, 1])

        for k in range(N):
            subIn = vstack((XVL[k], XVR[k]))
            currP = dot(subIn.transpose(), subIn)

            psd[:, :, k] = psd[:, :, k] * lamb + (1 + lamb) * currP
            Cpsd = psd[:, :, k]

            # compute eigenvalue & eigenvector

            eigVal, eigVec = np.linalg.eig(Cpsd)
            pan = eigVec[:, 1]

            Sest[k] = pan[0] * XVL[k] + pan[1] * XVR[k]

            Nlest[k] = XVL[k] - Sest[k] * pan[0]
            Nrest[k] = XVR[k] - Sest[k] * pan[1]

        xout = fftpack.irfft(Sest)
        xl = fftpack.irfft(Nlest)
        xr = fftpack.irfft(Nrest)
        OutVec = append(OutVec, xout)
        OutAmbL = append(OutAmbL, xl)
        OutAmbR = append(OutAmbR, xr)

    print('process end : copy start')
    ext_primary = OutVec
    ext_ambient = transpose(vstack((OutAmbL, OutAmbR)))

    ret_primary = wave.open(primary_path, 'w')
    ret_primary.setparams((1, sampWidth, FrameRate, nFrames, 'NONE', 'not compressed'))

    copyWav(ret_primary, ext_primary)

    ret_primary.close()
    print('primary copy end')

    ret_ambient = wave.open(ambient_path, 'w')
    ret_ambient.setparams((2, sampWidth, FrameRate, nFrames, 'NONE', 'not compressed'))

    copyWav2(ret_ambient, ext_ambient)

    ret_ambient.close()

    print('ambient copy end')

    input.close()

import cv2
import numpy as np
import librosa

def solution(audio_path):
    ############################
    ############################

    ############################
    ############################
    ## comment the line below before submitting else your code wont be executed##
    # pass
    f = 1024
    h = 512
    cardboard_mean=0.31187767
    metal_mean=1.299
    unknown_audio, unknown_sr = librosa.load(audio_path, sr=None)
    unknown_audio_normalized = unknown_audio / np.max(np.abs(unknown_audio))
    unknown_spectrogram = np.abs(librosa.stft(unknown_audio_normalized, n_fft=f, hop_length=h))
    unknown_mean_energy = np.mean(unknown_spectrogram[50:200, :], axis=0)
    unknown_mean=np.mean(unknown_mean_energy)
    metal_similarity = abs(metal_mean-unknown_mean)
    cardboard_similarity = abs(cardboard_mean - unknown_mean)

    class_name1='cardboard'
    class_name2='metal'

    if metal_similarity < cardboard_similarity:
        return class_name2
    else:
        return class_name1
        

import librosa
import numpy as np

y1, sample_rate1 = librosa.load("ambi_sample_60/ambi_60_azi_0_ele.wav", mono=False)
y2, sample_rate2 = librosa.load("ambi_basketball_60/ambi_240_azi_0_ele.wav", mono=False)
y11, sample_rate11 = librosa.load("ambi_sample_60/ambi_240_azi_0_ele.wav", mono=False)
y22, sample_rate22 = librosa.load("ambi_basketball_60/ambi_60_azi_0_ele.wav", mono=False)
y111, sample_rate111 = librosa.load("ambi_sample_60/ambi_180_azi_0_ele.wav", mono=False)
y222, sample_rate222 = librosa.load("ambi_basketball_60/ambi_0_azi_0_ele.wav", mono=False)
l = len(y2[0,:])//6

combined1 = (y1[:,1000000:1000000+l] + y2[:,:l])/2
combined2 = (y11[:,1000000:1000000+l] + y22[:,:l])/2
combined3 = (y111[:,1000000:1000000+l] + y222[:,:l])/2

combined = np.concatenate((combined3, combined2,combined1), axis=1)
librosa.output.write_wav(f'combined_ambi.wav', combined, sample_rate1)
librosa.output.write_wav(f'combined_ambi1.wav', combined1, sample_rate1)
librosa.output.write_wav(f'combined_ambi2.wav', combined2, sample_rate1)
librosa.output.write_wav(f'combined_ambi3.wav', combined3, sample_rate1)

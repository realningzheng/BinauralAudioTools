from pydub import AudioSegment
sound = AudioSegment.from_wav("./src/basketball-bouncing.wav")
sound = sound.set_channels(1)
sound.export("./src/basketball-bouncing_mono.wav", format="wav")
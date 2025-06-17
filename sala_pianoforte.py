# Melodia per la parola "CRYPTA"
# C - D - B - F - G - A

melody_notes_crypta = ['C', 'D', 'B', 'F', 'G', 'A']
melody_crypta = AudioSegment.silent(duration=0)

for note in melody_notes_crypta:
    freq = notes_freq[note]
    tone = Sine(freq).to_audio_segment(duration=duration_ms).fade_in(50).fade_out(50)
    melody_crypta += tone

file_path_crypta = "/mnt/data/melodia_crypta.wav"
melody_crypta.export(file_path_crypta, format="wav")

file_path_crypta

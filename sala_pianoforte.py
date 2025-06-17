from pydub import AudioSegment
from pydub.generators import Sine

# Frequenze approssimative delle note musicali (Hz)
notes_freq = {
    'C': 261.63,  # Do
    'D': 293.66,  # Re
    'E': 329.63,  # Mi
    'F': 349.23,  # Fa
    'G': 392.00,  # Sol
    'A': 440.00,  # La
    'B': 493.88,  # Si
}

duration_ms = 500  # durata di ogni nota in millisecondi

# Melodia per la parola "CRYPTA"
melody_notes_crypta = ['C', 'D', 'B', 'F', 'G', 'A']
melody_crypta = AudioSegment.silent(duration=0)

for note in melody_notes_crypta:
    freq = notes_freq[note]
    tone = Sine(freq).to_audio_segment(duration=duration_ms).fade_in(50).fade_out(50)
    melody_crypta += tone

file_path_crypta = "melodia_crypta.wav"
melody_crypta.export(file_path_crypta, format="wav")

print(f"File audio salvato in: {file_path_crypta}")

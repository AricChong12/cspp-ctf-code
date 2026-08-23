import wave

wav = wave.open("whisper.wav", "rb")

frames = wav.readframes(wav.getnframes())

# 16-bit samples = 2 bytes each
samples = [
    int.from_bytes(frames[i:i+2], byteorder="little", signed=True)
    for i in range(0, len(frames), 2)
]

bits = []

for sample in samples:
    bits.append(sample & 1)

# Pack bits MSB first
data = bytearray()

for i in range(0, len(bits) - 7, 8):
    byte = 0

    for bit in bits[i:i+8]:
        byte = (byte << 1) | bit

    if byte == 0:
        break

    data.append(byte)

print(data.decode(errors="replace"))
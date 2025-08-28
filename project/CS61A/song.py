from wave import open
from struct import Struct
from math import floor

frame_rate = 11025

def encode(x):
    i = int(16384 * x)
    return Struct('h').pack(i)

def play(sampler, name='song.wav',seconds=2):
    out = open(name, 'wb')
    out.setnchannels(1)
    out.setsampwidth(2)
    out.setframerate(frame_rate)
    t = 0
    while t< seconds * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t += 1
    out.close()

def tri(frequency, amplitude=0.3):
    period = frame_rate // frequency
    def sampler(t):
        saw_wave = t / period - floor(t / period + 0.5)
        tri_wave = 2 * abs(2*saw_wave)-1
        return amplitude * tri_wave
    return sampler
c_freq = 261.63
e_freq = 329.63
g_freq = 392.00

def both(f, g):
    return lambda t: f(t) + g(t)

def note(f,start,end, fade_in=0.05, fade_out=0.05):
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade_in:
            return (seconds - start) / fade_in * f(t)
        elif seconds > end - fade_out:
            return (end - seconds) / fade_out * f(t)
        else:
            return f(t)
    return sampler

c, e ,g= tri(c_freq), tri(e_freq), tri(g_freq)
low_g= tri(g_freq/2)
z=0
song = note(e,z,z+1/8)
z+=1/8
song = both(song,note(e,z,z+1/8))
z+=1/4
song = both(song,note(e,z,z+1/8))
z+=1/4
song = both(song,note(c,z,z+1/8))
z+=1/8
song = both(song,note(e,z,z+1/8))
z+=1/4
song = both(song,note(g,z,z+1/4))
z+=1/2
song = both(song,note(low_g,z,z+1/4))
z+=1/2
play(song)
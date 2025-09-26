#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

KEYS = "q2we4r5ty7u8i9op-[=]"
BASE = 1.059463
FREQ = [440 * (BASE ** (i - 12)) for i in range(len(KEYS))]

MIN_DECAY = 0.990
MAX_DECAY = 0.988

def clamp_sample(x: float) -> float:
    # clamp into valid float range when playing the sample
    max = 1.0
    min = -max
    if x > max: return max
    elif x < min: return min
    return x

def sample(keymap) -> float:
    # compute the superposition of samples
    s = 0.0
    for k in keymap.values():
        ks = k.sample()
        if ks != 0: s += ks
    s = clamp_sample(s)
    return round(s, 4)

def advance(keymap):
    # advance the simulation of each guitar string by one step
    for k in KEYS:
        if not 0 < abs(keymap[k].sample()): continue
        if not keymap[k].has_sustain():
            keymap[k].zero_buffer()
            continue
        keymap[k].tick()

if __name__ == '__main__':
    # initialize window
    stdkeys.create_window()

    # create dict to relate the characters to the GuitarString Objects
    keymap = {}
    for i, k in enumerate(KEYS):
        frequency = FREQ[i]
        gs = GuitarString(frequency)

        f_min = min(FREQ)
        f_max = max(FREQ)

        # linear interpolation from f_min..f_max => low_decay..high_decay
        decay = MIN_DECAY - ((MIN_DECAY - MAX_DECAY) * ((frequency - f_min) / (f_max - f_min)))

        gs.set_decay(decay)
        keymap[k] = gs

    n_iters = 0
    while True:
        # it turns out that the bottleneck is in polling for key events
        # for every iteration, so we'll do it less often, say every 
        # 1000 or so iterations
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        # check if the user has typed a key; if so, process it
        if stdkeys.has_next_key_typed():
            k = stdkeys.next_key_typed()
            if k != '' and k in KEYS: keymap[k].pluck()

        # play the sample on standard audio
        play_sample(sample(keymap))

        # advance the simulation
        advance(keymap)

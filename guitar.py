#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

KEYS = "q2we4r5ty7u8i9op-[=]"
BASE = 1.059463
FREQ = [440 * (BASE ** (i - 12)) for i in range(len(KEYS))]
ROUND = 4 # round sample by int n digits, where n > 3 (noise present for n <= 3)

LOW_DECAY = 0.990
HIGH_DECAY = 0.988

def sample(keymap) -> float:
    # compute the superposition of samples
    # clamp and round the audio sample
    # to make it safe and easy for play_sample() to process
    lim = 1.0
    min = 10**(-(ROUND + 1))
    sample = 0.0
    for k in keymap.values():
        s = k.sample()
        if min <= abs(s): sample += s
    if abs(sample) > lim: sample = lim if sample > 0 else -lim
    return round(sample, ROUND)

def advance(keymap):
    # advance the simulation of each guitar string by one step
    # exclude processing of strings that are not playing
    # reset strings to 0 when they cannot be heard
    for k in KEYS:
        if 0 == keymap[k].sample(): continue
        if not keymap[k].is_sustained():
            keymap[k].zero_buffer()
            continue
        keymap[k].tick()

if __name__ == '__main__':
    # initialize window
    stdkeys.create_window()

    # create dictionary to relate the each char to each GuitarString
    keymap = {}
    for i, k in enumerate(KEYS):
        frequency = FREQ[i]
        gs = GuitarString(frequency)

        f_min = min(FREQ)
        f_max = max(FREQ)

        # extra: decay factor dependent on frequency
        # linear interpolation from f_min...f_max => low_decay...high_decay
        decay = LOW_DECAY - ((LOW_DECAY - HIGH_DECAY) * ((frequency - f_min) / (f_max - f_min)))

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

"""
1. The first character of the base value is the single most frequently
   occurring character in the signal.
2. Each following character of the base value is the one that occurs the most
   frequently in the signal immediately after the previous character of the
   base value. For example, if the first character of the base value is A, then
   the second character of the base value is the one that occurs the most
   frequently immediately after A in the signal.
3. The most frequently occurring character after the last character of the base
   value is ';'.
"""
def most_freq(signal):
    freqs = {}
    for c in signal:
        if c not in freqs:
            freqs[c] = 0
        freqs[c] = freqs[c]+1
    return sorted(freqs.items(), key=lambda x: x[1], reverse=True)[0][0]

def most_freq_after(signal, c):
    freqs = {}
    i = 0
    while i < len(signal)-1:
        if signal[i] != c:
            i = i+1
            continue
        s = signal[i+1]
        if s not in freqs:
            freqs[s] = 0
        freqs[s] = freqs[s]+1
        i = i+2
    return sorted(freqs.items(), key=lambda x: x[1], reverse=True)[0][0]


if __name__ == "__main__":
    with open("nanobots_signal.txt", "r") as f:
        signal = f.read() 

    new_base = ""
    current = most_freq(signal)
    while current != ';':
        new_base += current
        current = most_freq_after(signal, current)

    # for item in sorted(freqs.items(), key=lambda x: x[1], reverse=True):
        # if item[0] == ';':
            # break
        # new_base += item[0]

    print(new_base)


# PbToNjqk2rht^9CWu5vmpn%YEdKsX7AFB4Sxl6aVLiIURwG#&fM@y$Oc*ez3gH!D0QJ18Z




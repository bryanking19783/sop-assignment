str = "The quick brown fox jumps over the lazy dog"
freq = {}
for i in str:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] = 1
print(freq)


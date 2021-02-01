s = "Locked in for Camping Project goes out tomorrow so no workday update today and tonight's booked for actual writing so this will be written up post-project submittal tomorrow afternoon Which is perfect because I will not want to do any work at all for a while after this Thank god the next couple weeks will be short and empty"
k = 15
finaloutput = []
chunkedString = s.split()
print("Chunked String length is " + str(len(chunkedString)))
chunk = ""
for word in chunkedString:
    if len(chunk) + len(word) + 1 <= k:
        if len(chunk) != 0:
            chunk += " " + str(word)
        else:
            chunk = word
    else:
        finaloutput.append(chunk)
        chunk = word
finaloutput.append(chunk)
print(finaloutput)
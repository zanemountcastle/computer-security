# Returns ordered tuple list as (character, percentage)
def characterFrequency(message):
    d = dict([(chr(i),0.0) for i in range(97,123)]) # Creates dictionary of all letters with value initialized at 0.0

    for char in message:
        if char != ' ':
            d[char] += 1 # Increase count of letter in dictionary when read

    for char in d:
        d[char] = d[char]/len(message) * 100 # Get percentage

    d = [(k,v) for v,k in sorted([(v,k) for k,v in d.items()],reverse=True)] # Sort dictionary by percentage (decending)

    print "Character Frequency:"
    for char in d:
        print char[0] + " : " + str(char[1]) + "%" # Print character frequency

    return d

# Decrypt the message using unique substitution cipher key
def decryptMessage(message, key): # Takes message and substitution cipher key
    d = characterFrequency(message) # Returns ordered tuple list of characters

    print "\nKey: " # Build dictionary of cipher characters and their key pairs
    keyDictionary = {}
    for i in range(0,26):
        keyDictionary[d[i][0]] = key[i]
        print d[i][0] + " : " + key[i]

    decryptedMessage = "" # String to build decrypted message with key
    for char in message:
        if char != ' ':
            decryptedMessage += keyDictionary[char] # Replace each character with key
        else:
            decryptedMessage += ' '

    print "\nDecrypted Message: "
    print decryptedMessage # Finally return decrypted message

def decrypt(message):
    # For loop to exhaustively search the key space (26)
    # using the brute force method and print result.
    for key in range (1, 26): # Key space = 26
        print ("Key: " + str(key))
        m = "" # String for shifted message
        for l in message: # Each letter in message
            a = (ord(l)-97) # 0-base char list
            b = ((a + key) % 26) # Shift a by 'key' characters
            m += chr(b + 97) # Add new character to message and un-zero base
        print "Message: " + m + "\n" # Print decrypted message

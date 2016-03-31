# Author: Jim Thompson, jim.thompson@pobox.com

# Create and populate an array to contain the inverse of the y = 129 *
# x operation. This makes the inverse-digest calculation just a tiny
# bit easier to write.

# Instantiate the array
invmap = list(range(256))

# Populate the array
for i in range(256):
    v = (i * 129) & 255
    invmap[v] = i

# Take the given digest and reverse it to the message that generated
# it.
def answer(digest):
    # your code here

    # Allocate a place to store the message. It will be the same
    # length as the digest.
    message = list(range(len(digest)))
    
    # Use a variable to hold the message[i - 1] octet. This keeps us
    # from using a negative index in the message array.
    prevmessageoctet = 0

    # Iterate over the characters in the digest
    for i in range(len(digest)):

        # Compute the corresponding message value
        message[i] = invmap[(prevmessageoctet ^ digest[i])]
        
        # Keep a copy of the message value. In the next iteration,
        # this is message[i - 1].
        prevmessageoctet = message[i]

    # Return the message we just computed.
    return message

if __name__ == '__main__':
    
    digest = [0, 129, 3, 129, 7, 129, 3, 129, 15, 129, 3, 129, 7, 129, 3, 129]
    message = answer(digest)
    print message

    digest = [0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]
    message = answer(digest)
    print message

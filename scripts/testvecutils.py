# Some simple utility routines for scripted test vector generation

# Generate a binary number as a string:
def bin(x, width):
    s = ""
    for i in range(width):
        s = str(x & 1) + s
        x >>= 1
    return s

# Generate a binary number as a string, using hokey L & H for 1 and 0:
def lh(x, width):
    s = ""
    for i in range(width):
        lhch = "LH"[x&1]
        s = lhch + s
        x >>= 1
    return s

# Generate a header text field of specified width, containing title chars padded with dots:
def hd(title, width):
    s = title
    while len(s) < width:
        s = s + '.' if len(s)&1 else '.'+s

    return s



# YouTube Link:

"""
Run-length encoding (RLE) is a very simple form of lossless data compression
in which runs of data (that is, sequences in which the same data value occurs
in many consecutive data elements) are stored as a single data value and count,
rather than as the original run.

Example:
    WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
    With a run-length encoding (RLE) data compression algorithm applied to
    the above hypothetical scan line, it can be rendered as follows:

    12W1B12W3B24W1B14W
    This can be interpreted as a sequence of twelve Ws, one B, twelve Ws,
    three Bs, etc..,
"""


def run_length_encode(uncompressed_data):
    """
    Takes an uncompressed string of data and
    returns the run-length encoded string.
    """
    compressed_data = ""
    return compressed_data


def run_length_decode(compressed_data):
    """
    Takes a run-length encoded compressed string
    and returns the uncompressed decoded data.
    """
    uncompressed_data = ""
    return uncompressed_data


uncompressed_data = "aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa"

# Expects: 
compressed_data = run_length_encode(uncompressed_data)

# Expects: "aaaaahhhhhhmmmmmmmuiiiiiiiaaaaaa"
uncompressed_data = run_length_decode(compressed_data)


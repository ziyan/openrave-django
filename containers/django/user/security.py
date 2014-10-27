from __future__ import division

import math
import random
import string

_rng = random.SystemRandom()

HEXADECIMAL_DIGITS = string.digits + 'abcdef'
DIGITS = string.digits
LOWERCASE_ALPHA = string.lowercase
UPPERCASE_ALPHA = string.uppercase
LOWERCASE_ALPHANUMERIC = string.lowercase + string.digits
UPPERCASE_ALPHANUMERIC = string.uppercase + string.digits
ALPHA = string.letters
ALPHANUMERIC = string.letters + string.digits
ASCII_PRINTABLE = string.letters + string.digits + string.punctuation
ALL_PRINTABLE = string.printable
PUNCTUATION = string.punctuation

def generate_random_string(length=None, entropy=None, pool=ALPHANUMERIC):
    """Generates a random string using the given sequence pool.

    To generate stronger passwords, use ASCII_PRINTABLE as pool.

    Entropy is:

         H = log2(N**L)

    where:

    - H is the entropy in bits.
    - N is the possible symbol count
    - L is length of string of symbols

    Entropy chart::

        -----------------------------------------------------------------
        Symbol set              Symbol Count (N)  Entropy per symbol (H)
        -----------------------------------------------------------------
        HEXADECIMAL_DIGITS      16                4.0000 bits
        DIGITS                  10                3.3219 bits
        LOWERCASE_ALPHA         26                4.7004 bits
        UPPERCASE_ALPHA         26                4.7004 bits
        PUNCTUATION             32                5.0000 bits
        LOWERCASE_ALPHANUMERIC  36                5.1699 bits
        UPPERCASE_ALPHANUMERIC  36                5.1699 bits
        ALPHA                   52                5.7004 bits
        ALPHANUMERIC            62                5.9542 bits
        ASCII_PRINTABLE         94                6.5546 bits
        ALL_PRINTABLE           100               6.6438 bits

    :param length:
        The length of the random sequence. Use this or `entropy`, not both.
    :param entropy:
        Desired entropy in bits. Use this or `length`, not both.
        Use this to generate passwords based on entropy:
        http://en.wikipedia.org/wiki/Password_strength
    :param pool:
        A sequence of characters from which random characters are chosen.
        Default to case-sensitive alpha-numeric characters.
    :returns:
        A string with characters randomly chosen from the pool.
    """
    pool = list(set(pool))

    if length and entropy:
        raise ValueError('Use length or entropy, not both.')

    if length <= 0 and entropy <= 0:
        raise ValueError('Length or entropy must be greater than 0.')

    if entropy:
        log_of_2 = 0.6931471805599453
        length = long(math.ceil((log_of_2 / math.log(len(pool))) * entropy))

    return ''.join(_rng.choice(pool) for _ in xrange(length))


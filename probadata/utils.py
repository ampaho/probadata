import sys
from hashlib import sha512, sha384, sha256, sha1, md5

try:
    import StringIO
    import cStringIO
except ImportError:
    from io import BytesIO

from struct import unpack, pack
from math import ceil, log, pow

is_python_3 = sys.version_info[0] == 3

def count_min_sketch_hash(x, m, d):
    md5_ = md5(str(hash(x)))
    for i in xrange(d):
        md5_.update(str(i))
        yield int(md5_.hexdigest(), 16) % m

def getSHA1Bin(word):
    """
    Returns the SHA1 hash binary representation of the word passed as argument
    Arguments:
    - `word`: argument to the SHA1 function
    """
    hash_s = sha1()
    hash_s.update(word)
    return bin(long(hash_s.hexdigest(),16))[2:].zfill(160)
    
def getIndex(binString,endIndex=160):
    """
    Returns the possition of the first 1 bit from the left in the word until endIndex
    Arguments:
    - `binString`: String to be compared
    - `endIndex`: Maximum index tu use in the lookup for the 1 bit
    """
        #i = 0
        # hexInt = int(hexString,16)
        ## Is it worth compare if hexInt is still bigger than zero? 
        #while (i<endIndex and (hexInt & 0x01 != 1)): 
        #    hexInt = hexInt >> 1
        #    i+=1
        #return i
    res = -1
    try:
        res = binString.index('1')+1
    except(ValueError):
        res = endIndex
    return res

def make_hashfuncs(num_slices, num_bits):
    if num_bits >= (1 << 31):
        fmt_code, chunk_size = 'Q', 8
    elif num_bits >= (1 << 15):
        fmt_code, chunk_size = 'I', 4
    else:
        fmt_code, chunk_size = 'H', 2
    total_hash_bits = 8 * num_slices * chunk_size
    if total_hash_bits > 384:
        hashfn = sha512
    elif total_hash_bits > 256:
        hashfn = sha384
    elif total_hash_bits > 160:
        hashfn = sha256
    elif total_hash_bits > 128:
        hashfn = sha1
    else:
        hashfn = md5
    fmt = fmt_code * (hashfn().digest_size // chunk_size)
    num_salts, extra = divmod(num_slices, len(fmt))
    if extra:
        num_salts += 1
    salts = tuple(hashfn(hashfn(pack('I', i)).digest()) for i in range_fn(num_salts))
    def _make_hashfuncs(key):
        if is_python_3:
            if isinstance(key, str):
                key = key.encode('utf-8')
            else:
                key = str(key).encode('utf-8')
        else:
            if isinstance(key, unicode):
                key = key.encode('utf-8')
            else:
                key = str(key)
        i = 0
        for salt in salts:
            h = salt.copy()
            h.update(key)
            for uint in unpack(fmt, h.digest()):
                yield uint % num_bits
                i += 1
                if i >= num_slices:
                    return

    return _make_hashfuncs


def compute_wordsize(Nmax):
    """
	Estimates the size of the memory Units, using the maximum cardinality as an argument
    Arguments:
    - `Nmax`: Maximum Cardinality 
    """
    return int(ceil(log(log(Nmax,2),2)))


def range_fn(*args):
    if is_python_3:
        return range(*args)
    else:
        return xrange(*args)


def is_string_io(instance):
    if is_python_3:
       return isinstance(instance, BytesIO)
    else:
        return isinstance(instance, (StringIO.StringIO,
                                     cStringIO.InputType,
                                     cStringIO.OutputType))
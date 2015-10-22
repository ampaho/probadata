# probadata (Probabilistic Data Structures)
Python package for probabilistic data structures


For now, probadata implements:
* LogLog structures (LogLog, HyperLogLog and SuperLogLog)
* BloomFilter (including Scalable BloomFilter<sup>[1]</sup>)
* Count-Min Sketch


#Requirements
bitarray is required and will be automatically installed along with probadata

#Installation 

$ git clone https://github.com/ampaho/probadata.git

$ cd probadata

$ python setup.py install

#Demo

##Bloom Filter
    from probadata.bloomfilter import BloomFilter, ScalableBloomFilter
    
    b = BloomFilter(capacity=100)
    b.add("Hello")
    
    #for a scalable bf, no need to specify the capacity
    sb = ScalableBloomFilter()
    sb.add("Hi")

##LoLog
    from probadata.loglog import LogLog, SuperLogLog, HyperLogLog
    
    #could be any loglog data structure
    l = HyperLogLog(maxCardinality=200000, error_rate=.005)
    l.add("oops")
    l.add("come")
    l.getNumberEstimate()

##Count-Min Sketch
    from probadata.countminsketch import CountMinSketch
    
    sk = CountMinSketch(1000, 10)
    sk.add(2, value=456)
    
    #CountMinSketch support indexing in read-only
    sk[2]
    
    #or you can use the query method
    sk.query(2)
    
    
    








[1] Paulo Sergio Almeida et al. http://gsd.di.uminho.pt/members/cbm/ps/dbloom.pdf

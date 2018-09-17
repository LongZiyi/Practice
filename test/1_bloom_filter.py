# pip install bloom_filter
# import bloom_filter.BloomFilter 不行
from bloom_filter import BloomFilter



url = 'www.baidu.com'
bf = BloomFilter(1024*1024*16, 0.01)
bf.add(url)

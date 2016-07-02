import hashlib
m = hashlib.md5()
m.update('Priya Kapoor')
print m.digest()
print m.digest_size
print m.block_size
print hashlib.algorithms
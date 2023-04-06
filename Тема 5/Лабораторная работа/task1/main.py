from pprint import pprint

dic = [{n: v for n, v in zip(["bin", "dec", "hex", "oct"], [bin(i), i, hex(i), oct(i)])} for i in range(16)]

pprint(dic)

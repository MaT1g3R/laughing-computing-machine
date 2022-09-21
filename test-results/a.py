import random
import xml.etree.ElementTree as ET
from string import printable


def randstring() -> str :
    length = random.randint(10,100)
    
    def a():
        for _ in range(length):
            while True:
                a = random.choice(printable)
                if a.isspace():
                    continue
                yield a
                break

    return ''.join(a())

num_tests = random.randint(10000, 100000)

suite = ET.Element('testsuite', attrib={'name': randstring(), 'tests': str(num_tests), 'failures': str(num_tests), 'errors':'0', 'time': "8.518866" , 'timestamp': "2014-10-28T05:00:31+00:00"})
prop = ET.SubElement(suite, 'properties')

for _ in range(num_tests):
    case_ = ET.SubElement(suite, 'testcase', attrib={'classname': randstring(), 'name': randstring(), 'file': randstring(), 'time': '0.00001'})
    fail = ET.SubElement(case_, 'failure', attrib={'message': randstring()})

ET.dump(suite)

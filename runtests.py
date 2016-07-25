import unittest

testmodules = [
    'tests.unit.inventorytest',
    'tests.unit.charactertest',
    # add modules here as you write them
    ]

suite = unittest.TestSuite()

for t in testmodules:
        # load  all tests in module
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

unittest.TextTestRunner().run(suite)

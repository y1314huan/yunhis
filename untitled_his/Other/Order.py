# coding:utf-8
import unittest
class grouptest(unittest.TestCase):
    def testgroupsuit(self):#必须以test开头
        # from lianxi import lx
        from case import test_001
        from case import test_004
        from case import test_005
        from case import test_006
        from commonshare import Ecount
        from case import test_008
        from case import test_009
        from case import test_010
        groupsuit=unittest.TestSuite()
        groupsuit.addTest(unittest.makeSuite(test_001.TestHis))
        groupsuit.addTest(unittest.makeSuite(test_004.TestHis))
        groupsuit.addTest(unittest.makeSuite(test_005.TestHis))
        groupsuit.addTest(unittest.makeSuite(test_006.TestHis))
        groupsuit.addTest(unittest.makeSuite(Ecount.TestHis))
        groupsuit.addTest(unittest.makeSuite(test_008.TestHis))
        groupsuit.addTest(unittest.makeSuite(test_009.TestHis))
        groupsuit.addTest(unittest.makeSuite(test_010.TestHis))
        unittest.TextTestRunner(verbosity=8).run(groupsuit)
if __name__ == '__main__':
    unittest.main()
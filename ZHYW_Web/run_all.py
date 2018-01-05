__author__ = 'wls'
# coding = utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
import HTMLTestRunner_jpg


def all_case():
    case_dir = r"C:\Users\Administrator\PycharmProjects\ZHYW_Web\test_case"
    #testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py", top_level_dir=None)
    '''
    for test_suit in discover:
        for test_case in test_suit:
            # 添加用例到testcase
            testcase.addTest(test_case)
    print(testcase)
    return testcase
    '''
    return discover


if __name__ == '__main__':
    report_path = r"C:\Users\Administrator\PycharmProjects\ZHYW_Web\report\result.html"
    fp = open(report_path, "wb")
    # runner = HTMLTestRunner(stream=fp, title=u'智慧运维回归测试报告', description=u'用例执行情况')
    runner = HTMLTestRunner_jpg.HTMLTestRunner(stream=fp, title="智慧运维回归测试报告",
                                               description="用例执行情况",
                                               verbosity=2,
                                               retry=1)

    # 执行用例
    runner.run(all_case())
    fp.close()

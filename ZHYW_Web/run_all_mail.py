__author__ = 'wls'
# coding = utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
import HTMLTestRunner_jpg
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import time
import os


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.elitel.com.cn")
    smtp.login("wanglishen@elitel.com.cn", "243717")
    smtp.sendmail("wanglishen@elitel.com.cn", "wanglishen@elitel.com.cn", msg.as_string())
    smtp.quit()
    print('email has send out !')


def new_report(report_path):
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getatime(report_path + "\\" + fn))
    file_new = os.path.join(report_path, lists[-1])
    print(file_new)
    return file_new


def all_case():
    case_dir = r"C:\Users\Administrator\PycharmProjects\ZHYW_Web\test_case"
    # testcase = unittest.TestSuite()
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
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    report_path = r"C:\\Users\\Administrator\\PycharmProjects\\ZHYW_Web\\report"
    filename = report_path + '\\' + now + "result.html"
    fp = open(filename, "wb")
    # runner = HTMLTestRunner(stream=fp, title=u'智慧运维回归测试报告', description=u'用例执行情况')
    runner = HTMLTestRunner_jpg.HTMLTestRunner(stream=fp, title="智慧运维回归测试报告",
                                               description="用例执行情况",
                                               verbosity=2,
                                               retry=1)

    # 执行用例
    runner.run(all_case())
    fp.close()
    new_report = new_report(report_path)
    send_mail(new_report)  # 发送测试报告


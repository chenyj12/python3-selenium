import unittest
import time
from HTMLTestRunner_cn import HTMLTestRunner
from Base.sentMail import send_mail, new_file
import os
import getcwd
import sys
sys.path.append('../')

test_dir = os.path.join(getcwd.get_cwd(), 'TestCases')
discovery = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    report_dir = os.path.join(getcwd.get_cwd(), 'Report')
    now = time.strftime('%Y-%m-%d-%H_%M_%S')
    report_name = report_dir + '/' + now + 'report.html'
    with open(report_name, 'wb') as f:
        runner = HTMLTestRunner(stream=f, title='测试报告', description='测试结果')
        runner.run(discovery)
    f.close()
    new_report = new_file(report_dir)
    send_mail(new_report)

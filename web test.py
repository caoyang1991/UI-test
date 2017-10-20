# -*- coding: UTF-8 -*- 
from selenium import webdriver
import time
import unittest
import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class QingShuTests(unittest.TestCase):
  
  def setUp(self):
    self.driver = webdriver.Firefox()
    self.driver.get("http://www.qingshuxuetang.com")
    self.driver.maximize_window()
    time.sleep(2)
    print'1'


  def test_Login(self):
    self.driver.find_element_by_xpath(".//*[@id='bs-example-navbar-collapse-1']/ul/li[2]/a").click()
    time.sleep(1)
    self.driver.find_element_by_xpath(".//*[@id='uname']").send_keys("qingfeng")
    time.sleep(1)
    self.driver.find_element_by_xpath(".//*[@id='pwd']").send_keys("123456")
    time.sleep(1)
    self.driver.find_element_by_id("loginBtn").click()
    time.sleep(3)
    name=self.driver.find_element_by_xpath(".//*[@id='currentCity']").text  
    self.assertEqual(name, u'南京市')  
    time.sleep(2)
    print'2'

  def tearDown(self):
    self.driver.quit()
    print'3'
	
if __name__ == '__main__':
  suite = unittest.TestSuite()#测试用例管理
  
  suite.addTest(QingShuTests("test_Login"))
  timestr = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
  filename = "E:\\webreport\\result_" + timestr + ".html"
  print (filename)
  fp = open(filename, 'wb')
  runner = HTMLTestRunner.HTMLTestRunner(
              stream=fp,
              title='测试结果',
              description='测试报告'
              )
  runner.run(suite)
  fp.close()

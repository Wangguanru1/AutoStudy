from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class AutoStudy:

    def __init__(self, num):
        """
        :param num: 选择开始播放的课时(前面所有的课时数+1)
        """
        self.number = num
        self.current_course = ' '
        self.browser = webdriver.Chrome(executable_path='chromedriver.exe')

    def play_video(self):
        """
        如果当前页面为视频页，则播放视频，如果为答题页则跳过
        :return:
        """
        time.sleep(2)
        try:
            self.browser.switch_to.frame(self.browser.find_element(By.TAG_NAME, "iframe"))
            self.browser.switch_to.frame(self.browser.find_element(By.TAG_NAME, "iframe"))
            time.sleep(2)
            self.browser.find_element(By.XPATH, '//*[@id="video"]/button').click()
            time.sleep(3)
            self.video()
        except:
            self.number = self.number + 1
            self.browser.switch_to.default_content()
            self.browser.find_elements(By.CLASS_NAME, 'hideChapterNumber')[self.number].click()
            self.current_course = self.browser.find_elements(By.CLASS_NAME, 'hideChapterNumber')[
                self.number].get_attribute(
                'textContent')

    def start(self, url):
        """
        在初始页面选择第一个要播放的课时
        :param url: 初始页面的url
        :return:
        """
        self.browser.get(url)
        time.sleep(10)
        self.current_course = self.browser.find_elements(By.CLASS_NAME, "chapterNumber")[self.number].get_attribute(
            'textContent')
        self.browser.find_elements(By.CLASS_NAME, "chapterNumber")[self.number].click()

    def get_process(self):
        """
        获取当前课时，当前播放时长与视频的总时长，并将它们打印在控制台上
        :return: 如果已经播放完返回0，否则返回1
        """
        current_time = self.browser.find_element(By.CLASS_NAME, 'vjs-current-time-display').get_attribute('textContent')
        total_time = self.browser.find_element(By.CLASS_NAME, 'vjs-duration-display').get_attribute('textContent')
        print(self.current_course + '  ' + str(current_time) + '/' + str(total_time))
        if current_time == total_time:
            return 0
        else:
            return 1

    def video(self):
        """
        每隔20s执行一次get_process，在当前视频播放完后点击下一课时
        :return:
        """
        while self.get_process():
            time.sleep(20)
        self.number = self.number + 1
        self.browser.switch_to.default_content()
        self.browser.find_elements(By.CLASS_NAME, 'hideChapterNumber')[self.number].click()
        self.current_course = self.browser.find_elements(By.CLASS_NAME, 'hideChapterNumber')[self.number].get_attribute(
            'textContent')


if __name__ == '__main__':
    study = AutoStudy(35)
    study.start(
        'http://mooc1.mooc.whu.edu.cn/mycourse/studentcourse?courseId=228108910&clazzid=62338069&cpi=197214950&enc'
        '=6fed49bb1c5da4f191db9ac3491f6f0a&fromMiddle=1&vc=1')
    while 1:
        study.play_video()

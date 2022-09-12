from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class AutoStudy:

    def __init__(self, num):
        """
        :param num: 选择开始播放的课时(要播放的课时前面所有的课时数+1)
        """
        self.number = num
        self.current_course = ' '
        self.browser = webdriver.Chrome(executable_path='chromedriver.exe')

    def get_video_num(self):
        """
            获得当前页面视频的数量
        :return: 返回视频的数量，如果没有视频则返回 0
        """
        try:
            time.sleep(2)
            self.browser.switch_to.frame(self.browser.find_element(By.TAG_NAME, "iframe"))
            video_num = self.browser.find_elements(By.TAG_NAME, "iframe")
            return len(video_num)
        except:
            return 0

    def play_video(self, num):
        """
        如果当前页面为视频页，则播放视频，如果为答题页则跳过
        :return:
        """
        if num > 0:
            for i in range(num):
                time.sleep(2)
                self.browser.switch_to.frame(self.browser.find_elements(By.TAG_NAME, "iframe")[i])
                time.sleep(2)
                self.browser.find_element(By.XPATH, '//*[@id="video"]/button').click()
                time.sleep(3)
                while self.get_process():
                    time.sleep(20)
                self.browser.switch_to.parent_frame()
            self.change_course()
        else:
            self.change_course()

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

    def change_course(self):
        """
        点击下一课时
        :return:
        """
        self.number = self.number + 1
        self.browser.switch_to.default_content()
        self.browser.find_elements(By.CLASS_NAME, 'hideChapterNumber')[self.number].click()
        self.current_course = self.browser.find_elements(By.CLASS_NAME, 'hideChapterNumber')[self.number].get_attribute(
            'textContent')

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


if __name__ == '__main__':
    study = AutoStudy(4)
    study.start(
        'http://mooc1.mooc.whu.edu.cn/mycourse/studentcourse?courseId=228133123&clazzid=62391848&cpi=197214950&enc'
        '=0d50da100b1d05cfeb24b43d2c74f988&fromMiddle=1&vc=1')
    while 1:
        study.play_video(study.get_video_num())

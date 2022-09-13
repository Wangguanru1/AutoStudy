# AutoStudy

## 使用说明

```python
if __name__ == '__main__':
    study = AutoStudy(chapternum)
    study.start('url')
    while 1:
        study.play_video(study.get_video_num())
```

| name       | value                          |
| ---------- | ------------------------------ |
| chapternum | 要播放的课时前面所有的课时数+1 |
| url        | 课程页面的url                  |

程序运行后在8s内扫码登陆（提前打开手机版学习通）

## 注意事项

1. 不要关闭浏览器的窗口，也不要将浏览器最小化，否则会运行异常
2. 如果课程设置了鼠标指针移出播放页后自动暂停播放，请不要在程序运行的过程中鼠标指针移入页面

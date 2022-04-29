# -*- coding: utf-8 -*-
# @Time   : 2022/4/15 22:54
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : combine_srt_video.py

from os.path import splitext, isfile
import os, tqdm
from moviepy.editor import (VideoFileClip,
                            TextClip,
                            CompositeVideoClip)


# 读取字幕文件
def read_srt(path):
    content = ""
    with open(path, 'r', encoding='UTF-8') as f:
        content = f.read()
        return content


# 字幕拆分
def get_sequences(content):
    sequences = content.split('\n\n')
    sequences = [sequence.split('\n') for sequence in sequences]
    # 去除每一句空值
    sequences = [list(filter(None, sequence)) for sequence in sequences]
    # 去除整体空值
    return list(filter(None, sequences))


def strFloatTime(tempStr):
    xx = tempStr.split(':')
    hour = int(xx[0])
    minute = int(xx[1])
    second = int(xx[2].split(',')[0])
    minsecond = int(xx[2].split(',')[1])
    allTime = hour * 60 * 60 + minute * 60 + second + minsecond / 1000
    return allTime

class RealizeAddSubtitles():
    '''
    合成字幕与视频
    '''

    def __init__(self, videoFile, txtFile):
        self.src_video = videoFile
        self.sentences = txtFile
        if not (isfile(self.src_video) and self.src_video.endswith(('.avi', '.mp4')) and isfile(
                self.sentences) and self.sentences.endswith('.srt')):
            print('视频仅支持avi以及mp4，字幕仅支持srt格式')
        else:
            video = VideoFileClip(self.src_video)
            # 获取视频的宽度和高度
            w, h = video.w, video.h
            # 所有字幕剪辑
            txts = []
            content = read_srt(self.sentences)
            sequences = get_sequences(content)

            for line in sequences:
                if len(line)<3:
                    continue
                sentences = line[2]
                start = line[1].split(' --> ')[0]
                end = line[1].split(' --> ')[1]

                start=strFloatTime(start)
                end=strFloatTime(end)

                start, end = map(float, (start, end))
                span=end-start
                txt = (TextClip(sentences, fontsize=40,
                                # font='/System/Library/Fonts/PingFang.ttc', size=(w - 20, 40),
                                # align='center', color='red')
                               font='PingFang.ttc', size=(w - 20, 40),
                              align = 'center', color='white', stroke_color='black')
                       .set_position((10, h - 150))
                       .set_duration(span)
                       .set_start(start))

                txts.append(txt)
            # 合成视频，写入文件
            video = CompositeVideoClip([video, *txts])
            fn, ext = splitext(self.src_video)
            video.write_videofile(f'{fn}_2带字幕{ext}')


if __name__ == '__main__':
    '''调用方法示例'''
    # srt_path = './audio/333.zh-cn.srt'
    # base_path = 'Unity3D游戏开发教程 Core核心功能01 Create Project 创建项目导入素材｜Unity中文课堂'
    # base_path = "Unity2018教程2D入门 01安装软件&导入素材"
    # todo_video = [
    #
    # ]
    # base_path = "Unity2018教程2D入门 01安装软件&导入素材"
    # for curDir, dirs, files in os.walk(base_path):
    #     for file in tqdm.tqdm(files):
    #         if file.endswith("22-22.2D光效(ver. Unity2018)-1080P 高清-AVC.srt"):
    #             # if file.endswith(".ass"):
    #             # if file.endswith(".srt") and not file.endswith("_中文（中国）.srt"):
    #             srt_path = os.path.join(curDir, file)
    #             print(srt_path)
    #             video_pth = srt_path.replace('.srt', '.mp4')
    #             # video_pth = srt_path.replace('.ass', '_2带字幕.mp4')
    #             addSubtitles = RealizeAddSubtitles(
    #                 video_pth, srt_path)
    pass


    # srt_path = '/Users/Beyoung/Movies/Unity3D游戏开发教程 Core核心功能01 Create Project 创建项目导入素材｜Unity中文课堂/1-01 Create Project 创建项目导入素材-1080P 高清-AVC_中文（中国）.srt'
    # addSubtitles = RealizeAddSubtitles('/Users/Beyoung/Movies/Unity3D游戏开发教程 Core核心功能01 Create Project 创建项目导入素材｜Unity中文课堂/1-01 Create Project 创建项目导入素材-1080P 高清-AVC.mp4', srt_path)


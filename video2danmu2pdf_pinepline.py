# -*- coding: utf-8 -*-
# @Time   : 2022/4/26 23:21
# @Author : beyoung
# @Email  : linbeyoung@stu.pku.edu.cn
# @File   : video2danmu2pdf_pinepline.py
import tqdm
from os.path import splitext, isfile
from burn_video_with_danmu import run_ass_combine
from combinepics2pdf import get_pic_pth_ls, divi_pic, pic_compose, creat_pdf
from combine_srt_video import RealizeAddSubtitles
from cut_video import one_cut

import os

if __name__ == '__main__':
    # for curDir, dirs, files in os.walk(base_path):
    todo_file = [
        # '1-01.安装软件&导入素材-1080P 高清-AVC.mp4',
        # '2-02.编辑素材& Til-1080P 高清-AVC.mp4',
        # '3-03.图层layer&角-1080P 高清-AVC.mp4',
        # '4-04.角色移动-1080P 高清-AVC.mp4',
        # '5-05.角色方向&跳跃-1080P 高清-AVC.mp4',
        # '6-06.动画效果Anima-1080P 高清-AVC.mp4',
        # '7-07.跳跃动画 Layer-1080P 高清-AVC.mp4',
        # '8-08.修复移动错误-1080P 高清-AVC.mp4',
        #

        # '22-22.2D光效(ver. Unity2018)-1080P 高清-AVC.mp4',

        # '9-09.镜头控制Cinemachine-1080P 高清-AVC.mp4',
        # '10-10.物品收集 & Prefabs-1080P 高清-AVC.mp4',
        # '11-11.物理材质&空中跳跃-1080P 高清-AVC.mp4',
        # '12-12.UI入门-1080P 高清-AVC.mp4',
        # '13-13.敌人Enemy-1080P 高清-AVC.mp4',
        # '14-14.受伤效果Hurt-1080P 高清-AVC.mp4',
        # '15-15.AI敌人移动-1080P 高清-AVC.mp4',
        # '16-16.Animation Events动画事件-1080P 高清-AVC.mp4',
        # '17-17.类的继承制作更多敌人-1080P 高清-AVC.mp4',
        # '18-18.音效Audio-1080P 高清-AVC.mp4',
        # '19-19.对话框Dialog-1080P 高清-AVC.mp4',
        # '20-20.趴下效果Crouch-1080P 高清-AVC.mp4',
        # '21-21.场景控制SceneManager-1080P 高清-AVC.mp4',
        # '22-22.2D光效(ver. Unity2018)-1080P 高清-AVC.mp4',
        # '23-23.优化代码Fix code-1080P 高清-AVC.mp4',
        # '24-24.视觉差Parallax-1080P 高清-AVC.mp4',
        # '25-25.主菜单MainMenu-1080P 高清-AVC.mp4',
        # '26-26.暂停菜单 AudioMixer-1080P 高清-AVC.mp4',
        # '27-27.手机控制 触控操作 真机测试-1080P 高清-AVC.mp4',
        # '28-28.二段跳 & 单向平台-1080P 高清-AVC.mp4',
        # '29-29.音效管理SoundManager-1080P 高清-AVC.mp4',
        # '30-30.End 游戏生成Build-1080P 高清-AVC.mp4',

        '1-01 Create Project 创建项目导入素材-1080P 高清-AVC.mp4',
        '10-10 Enemy Set States 设置敌人的基本属性和状态-1080P 高清-AVC.mp4',
        '11-11 Player Attack 实现攻击动画-1080P 高清-AVC.mp4',
        '12-12 FoundPlayer 找到Player追击-1080P 高清-AVC.mp4',
        '13-13 Enemy Animator设置敌人的动画控制器-1080P 高清-AVC.mp4',
        '14-14 Patrol Randomly 随机巡逻点-1080P 高清-AVC.mp4',
        '15-15 CharacterStats 人物基本属性和数值-1080P 高清-AVC.mp4',
        '16-16 AttackData 攻击属性-1080P 高清-AVC.mp4',
        '17-17 Execute Attack 实现攻击数值计算-1080P 高清-AVC.mp4',
        '18-18 Guard & Dead 守卫状态和死亡状态-1080P 高清-AVC.mp4',
        '19-19 泛型单例模式 Singleton-1080P 高清-AVC.mp4',
        '2-02 Build Level 尝试熟悉基本工具-1080P 高清-AVC.mp4',
        '20-20 Observer Pattern 接口实现观察者模式的订阅和广播-1080P 高清-AVC.mp4',
        '21-21 More Enemies 制作更多的敌人-1080P 高清-AVC.mp4',
        '22-22 Setup Grunt 设置兽人士兵-1080P 高清-AVC.mp4',
        '23-23 Extension Method 扩展方法-1080P 高清-AVC.mp4',
        '24-24 Setup Golem 设置石头人Boss-1080P 高清-AVC.mp4',
        '25-25 Throw Rocks 设置可以扔出的石头-1080P 高清-AVC.mp4',
        '26-26 Kick it Back 反击石头人-1080P 高清-AVC.mp4',
        '27-27 Health Bar 设置血条显示-1080P 高清-AVC.mp4',
        '28-28 Player LevelUp 玩家升级系统-1080P 高清-AVC.mp4',
        '29-29 Player UI 添加玩家信息显示-1080P 高清-AVC.mp4',
        '3-03 PolyBrush 发挥创意构建场景-1080P 高清-AVC.mp4',
        '30-30 Create Portal 创建传送门-1080P 高清-AVC.mp4',
        '31-31 Transition 实现同场景内传送-1080P 高清-AVC.mp4',
        '32-32 Different Scene 跨场景传送-1080P 高清-AVC.mp4',
        '33-33  Save Data 保存数据-1080P 高清-AVC.mp4',
        '34-34 Main Menu 制作主菜单-1080P 高清-AVC.mp4',
        '35-35 SceneFader 场景转换的渐入渐出-1080P 高清-AVC.mp4',
        '36-36 Build & Run打包及运行-1080P 高清-AVC.mp4',
        '4-04 Navigation 智能导航地图烘焙-1080P 高清-AVC.mp4',
        '5-05 MouseManager 鼠标控制人物移动-1080P 高清-AVC.mp4',
        '6-06 SetCursor 设置鼠标指针-1080P 高清-AVC.mp4',
        '7-07 Cinemachine & Post Processing 摄像机跟踪和后处理-1080P 高清-AVC.mp4',
        '8-08 Animator 动画控制器-1080P 高清-AVC.mp4',
        '9-09 Shader Graph 遮挡剔除-1080P 高清-AVC.mp4'
    ]
    # vroot = 'Unity3D游戏开发教程 Core核心功能01 Create Project 创建项目导入素材｜Unity中文课堂'
    vroot = 'Unity3D游戏开发教程 Core核心功能01 Create Project 创建项目导入素材｜Unity中文课堂'
    # srtroot = 'Unity2018教程2D入门_final/srt'
    srtroot = 'Unity3D游戏开发教程 Core核心功能01 Create Project 创建项目导入素材｜Unity中文课堂'
    for file in tqdm.tqdm(todo_file):
        video_path = os.path.join(vroot, file)
        srt_path = os.path.join(srtroot, file.replace('.mp4', '.srt'))
        print(video_path)
        print(srt_path)
        # video_pth = srt_path.replace('_中文（中国）.srt', '.mp4')
        # video_pth = srt_path.replace('.ass', '_2带字幕.mp4')
        addSubtitles = RealizeAddSubtitles(video_path, srt_path)
        fn, ext = splitext(video_path)
        srt_video_pth = f'{fn}_2带字幕{ext}'
        # ass_pth =
        # ass_pth = os.path.join('Unity2018教程2D入门_final/danmu/', file[:-4] + '.ass')
        ass_pth = os.path.join(srtroot, file[:-4] + '.ass')
        op_pth = os.path.join('Unity3D游戏开发教程 Core核心功能_final', file[:-4] + '_带弹幕.mp4')
        run_ass_combine(srt_video_pth, ass_pth, op_pth)
        filename = file[:-4] + '_带弹幕.mp4'
        ip_path = 'Unity3D游戏开发教程 Core核心功能_final'
        # op_path = 'Unity2018教程2D入门_带弹幕_screenshot_9_30_60'
        op_path = 'Unity3D游戏开发教程 Core核心功能_final_screenshot_60_danmu'
        one_cut(ip_path, filename, op_path)

    root = op_path
    pic_ls = os.listdir(root)
    # pic_ls.sort(key=lambda arr: (arr[:2], int(arr[2:])))
    pic_ls.sort(key=lambda arr: (int(arr.split('-')[0]), int(arr.split('_')[-1][:-4])))
    # print(pic_ls)
    row = 2
    line = 2

    pic_ls = get_pic_pth_ls(root, pic_ls)
    print('divd pic')
    page_list = divi_pic(pic_ls, row, line)
    print('pic_compose')
    pdf_folder = pic_compose(page_list, root)
    # pdf_folder = 'Unity3D游戏开发教程 Core核心功能01 Create Project 创建项目导入素材｜Unity中文课堂_screenshot_30_combine'
    # pdf_folder = 'Unity2018教程2D入门 01安装软件&导入素材_screenshot_30/'
    # pdf_pic_ls = get_pdf_pic_ls(pdf_folder)
    # pdf1_filename = 'u2课件_fps30_4page_9_30.pdf'
    pdf1_filename = 'u3课件_fps60_4page.pdf'
    print('creat pdf')
    creat_pdf(pdf_folder, pdf1_filename)


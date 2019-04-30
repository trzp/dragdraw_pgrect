#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/30 22:00
# @Version : 1.0
# @File    : dragdraw_pgrect.py
# @Author  : Jingsheng Tang
# @Version : 1.0
# @Contact : mrtang@nudt.edu.cn   mrtang_cs@163.com
# @License : (C) All Rights Reserved

import pygame
#本脚本用于绘制鼠标拖动时的方框

class DragDraw_pgRect:
    def __init__(self,root,color = (255,0,0),width = 1):
        self.root = root
        self.x0 = self.x1 = self.y0 = self.y1 = self.w = self.h = 0
        self.flg = False
        self.color = color
        self.width = width

    def update(self,events):
        for ev in events:
            if ev.type == pygame.MOUSEBUTTONDOWN:  # 记录起始点
                self.x0, self.y0 = self.x1, self.y1 = ev.pos
                self.flg = 1
            elif ev.type == pygame.MOUSEBUTTONUP:  # 记录终止点
                self.x1, self.y1 = ev.pos
                self.flg = 0
            elif ev.type == pygame.MOUSEMOTION:  # 更新终止点
                if self.flg: self.x1, self.y1 = ev.pos
            else:
                pass

        w, h = self.x1 - self.x0, self.y1 - self.y0
        if w > 0 and h > 0:
            rec = ((self.x0,self.y0), (w, h))
            pygame.draw.rect(self.root, self.color, rec, self.width)
            return 1,rec
        else:
            return 0,None


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    END = False
    dr = DragDraw_pgRect(screen)

    while not END:
        screen.fill((0,0,0))
        events = pygame.event.get()
        flg,rec = dr.update(events)

        for ev in events:
            if ev.type == pygame.QUIT:
                END = True
            elif ev.type == pygame.KEYUP and ev.key == 13:  # enter key
                if flg:
                    print 'you have seleted the area: %s'%(str(rec))
                else:
                    print "you havn't selected any region"
        pygame.display.update()

    pygame.quit()





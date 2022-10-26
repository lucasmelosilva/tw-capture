#!/usr/bin/python3
# -*- coding: utf-8 -*-

import youtube_dl
import json
import os

def lerjson():
    base = '#EXTM3U8\n\n'

    os.system('rm streamer.m3u8')

    arquivo = open('streamer.m3u8', 'w+')
    arquivo.write('base')
    arquivo.close()

if __name__ == '__main__':
    lerjson()

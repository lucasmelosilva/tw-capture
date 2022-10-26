#!/usr/bin/python3
# -*- coding: utf-8 -*-

import youtube_dl
import json
import os

def cria_streamer():
    base = '#EXTM3U8\n\n'

    arquivo_existe = os.path.exists('./streamer.m3u8')

    if arquivo_existe:
        os.system('rm streamer.m3u8')
        print('Atualizando stream')


    arquivo = open('streamer.m3u8', 'w+')
    arquivo.write('base')
    arquivo.close()


def lerjson():
    pass

if __name__ == '__main__':
    cria_streamer()

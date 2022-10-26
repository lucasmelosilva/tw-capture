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
    arquivo.write(base)
    arquivo.close()


def lerJson():
    array = []
    arquivo = open('streamers.json', 'r')
    nomes = json.load(arquivo)

    for nome in nomes['streamers']:
        array.append(nome)

    return array 

def pegaUrl(nome):
    url = f'https://twitch.tv/{nome}'
    return url

def escreveLink(link, nome):
    with open('streamer.m3u8', 'a') as arquivo:
        text = f'#EXTINF:-1, {str(nome).capitalize()}\n{link}\n\n'

        arquivo.write(text)
        arquivo.close()

def geraLink(url, nome):
    ytdl = youtube_dl.YoutubeDL()

    try:
        stream_link = ytdl.extract_info(url, download=False)
        return stream_link['url']
    except youtube_dl.utils.DownloadError:
        print(f'O Streamer {nome} esta Offline')

def main():
    cria_streamer()
    nomes = lerJson()
    
    for nome in nomes:
        url = pegaUrl(nome)
        link = geraLink(url, nome)
        escreveLink(link, nome)


if __name__ == '__main__':
    main()

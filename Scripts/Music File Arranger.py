#!/usr/bin/env python
# -- ############################################################################
# -- #      Copyright (C) 2020-2021 Vivek Kumar <vivekkumar.xda@gmail.com>      #
# -- #                All rights reserved.                                      #
# -- ############################################################################
# -- #
# -- # Project          : MusicFileArranger
# -- # Application      : MusicFileArranger
# -- # File Name        : MusicFileArranger.py
# -- # Exec Method      : Python General Script
# -- # Description      : This Script made to automatically arrange music file in
# -- #                    different folder as per the artist or the music
# -- #
# -- # Change History
# -- # -----------------------------------------------------------------------
# -- # Version     Date             Author                      Remarks
# -- # =======  ===========     =============               ============================
# -- # 1.0      17-July-2021     Vivek Kumar                Initial Version
# -- #
# -- ############################################################################

from tinytag import TinyTag
from glob import glob
import os
import shutil

MUSIC_DIR = r"C:/Database(D)/Random Song Collection/Audio Songs Library/"
MUSIC_DIR_ISSUE_FILE = r"C:/Database(D)/Random Song Collection/Audio Songs Library/issue file"
MUSIC_DIR_ISSUE_ARIJIT = r"C:/Database(D)/Random Song Collection/Audio Songs Library/Udit"

os.chdir(MUSIC_DIR)
for music_file in glob('*.mp3'):
    # print(music_file)
    try:
        music_file_details = TinyTag.get(music_file)
        # print(music_file_details.artist)
        # print(str(music_file_details).upper())
        if "Udit".upper() in str(music_file_details).upper():
            print(music_file, music_file_details.artist)
            shutil.move(music_file, MUSIC_DIR_ISSUE_ARIJIT)
    except:
        pass
        # print(f'Exception with File : {music_file}')
        # shutil.move(music_file, MUSIC_DIR_ISSUE_FILE)

    # print(music_file,music_file_details.artist)


# tag = TinyTag.get('/some/music.mp3')
# print('This track is by %s.' % tag.artist)
# print('It is %f seconds long.' % tag.duration)

# tag.album         # album as string
# tag.albumartist   # album artist as string
# tag.artist        # artist name as string
# tag.audio_offset  # number of bytes before audio data begins
# tag.bitrate       # bitrate in kBits/s
# tag.disc          # disc number
# tag.disc_total    # the total number of discs
# tag.duration      # duration of the song in seconds
# tag.filesize      # file size in bytes
# tag.genre         # genre as string
# tag.samplerate    # samples per second
# tag.title         # title of the song
# tag.track         # track number as string
# tag.track_total   # total number of tracks as string
# tag.year          # year or data as string

# music_dir=""
# list_of_opsc_files = glob.glob(os.path.join(tmp, '*.opsc'))
# song = songdetails.scan("data/commit.mp3")
# song.artist = "Great artist"
# song.save()

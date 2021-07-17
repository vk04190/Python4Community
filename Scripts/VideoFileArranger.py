
#!/usr/bin/env python
# -- ############################################################################
# -- #      Copyright (C) 2020-2021 Vivek Kumar <vivekkumar.xda@gmail.com>      #
# -- #                All rights reserved.                                      #
# -- ############################################################################
# -- #
# -- # Project          : VideoFileArranger
# -- # Application      : VideoFileArranger
# -- # File Name        : VideoFileArranger.py
# -- # Exec Method      : Python General Script
# -- # Description      : This Script made to automatically arrange Video Music file in
# -- #                    different folder as per the artist or the Movie names
# -- #
# -- # Change History
# -- # -----------------------------------------------------------------------
# -- # Version     Date             Author                      Remarks
# -- # =======  ===========     =============               ============================
# -- # 1.0      17-July-2021     Vivek Kumar                Initial Version
# -- #
# -- ############################################################################

from glob import glob
import os
from os import path
import shutil
from typing import Pattern

PATTERN = "arijit"
MOVE_DIR = "C:/Database(D)/Random Song Collection/Video Songs Library/Love Songs/"
# MOVE_DIR = r"C:/Database(D)/Random Song Collection/Video Songs Library/Party Songs"

VIDEO_DIR = r"C:/Database(D)/Random Song Collection/Video Songs Library/"

if path.isdir(MOVE_DIR):
    os.chdir(VIDEO_DIR)
    video_file_extensions = ['*.mp4', '*.avi', '*.3gp']
    video_files = []
    for video_file_extension in video_file_extensions:
        video_files.extend(glob(video_file_extension))

    for video_file in video_files:
        if PATTERN.upper() in video_file.upper():
            print(video_file)
            # shutil.move(video_file, MOVE_DIR)
else:
    print(f"Moving Directory is not correct: {MOVE_DIR}")

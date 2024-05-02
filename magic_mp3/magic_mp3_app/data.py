from moviepy.editor import *
from pytube import YouTube
from winshell import shortcut, desktop
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip, ffmpeg_extract_audio
import os

def descargar_mp4 (url=""):
    try:
        shortcut_path = os.path.join(desktop())
        video = YouTube(url)
        video_mp4 = video.streams.filter(progressive=True, file_extension='mp4').first().download(shortcut_path)
    except Exception as error:
        print(f"Error {error}")


def descargar_mp3 (url=""):
    try:
        shortcut_path = os.path.join(desktop())
        video = YouTube(url)
        video_mp4 = video.streams.filter(progressive=True, file_extension='mp4').first().download(shortcut_path)
        output_file = f'{video_mp4.replace(".mp4", "")}.mp3'
        video = VideoFileClip(video_mp4)
        audio = video.audio
        audio.write_audiofile(output_file)
        video.close()
        os.remove(video_mp4)
    except Exception as error:
        print(f"Error {error}")


def descargar_mp3_2 (url=""):
    try:
        shortcut_path = os.path.join(desktop())
        video = YouTube(url)
        video_mp4 = video.streams.filter(progressive=True, file_extension='mp4').first().download(shortcut_path)
        output_file = f'{video_mp4.replace(".mp4", "")}.mp3'
        ffmpeg_extract_audio(video_mp4, output_file)
        os.remove(video_mp4)
    except Exception as error:
        print(f"Error {error}")


def descargar_mp4_clip (url="", start_time=0, end_time=0):
    try:
        shortcut_path = os.path.join(desktop())
        video = YouTube(url)
        video_mp4 = video.streams.filter(progressive=True, file_extension='mp4').first().download(shortcut_path)
        start_time = float(start_time)
        end_time = float(end_time)
        input_file = video_mp4
        output_file = f"{video_mp4}.mp4"
        ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)
        os.remove(video_mp4)
    except Exception as error:
        print(f"Error {error}")


def descargar_mp3_clip (url="", start_time=0, end_time=0):
    try:
        shortcut_path = os.path.join(desktop())
        video = YouTube(url)
        video_mp4 = video.streams.filter(progressive=True, file_extension='mp4').first().download(shortcut_path)
        start_time = float(start_time)
        end_time = float(end_time)
        input_file = video_mp4
        output_file = f"{video_mp4}.mp4"
        ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)
        output_file2 = f'{video_mp4.replace(".mp4", "")}.mp3'
        video = VideoFileClip(output_file)
        audio = video.audio
        audio.write_audiofile(output_file2, codec='libmp3lame')
        video.close()
        os.remove(video_mp4)
        os.remove(output_file)
    except Exception as error:
        print(f"Error {error}")


def descargar_mp3_clip_2 (url="", start_time=0, end_time=0):
    try:
        shortcut_path = os.path.join(desktop())
        video = YouTube(url)
        video_mp4 = video.streams.filter(progressive=True, file_extension='mp4').first().download(shortcut_path)
        start_time = float(start_time)
        end_time = float(end_time)
        input_file = video_mp4
        output_file = f"{video_mp4}.mp4"
        ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)
        output_file2 = f'{video_mp4.replace(".mp4", "")}.mp3'
        ffmpeg_extract_audio(output_file, output_file2)
        os.remove(output_file)
        os.remove(video_mp4)
    except Exception as error:
        print(f"Error {error}")


### Este escript lo desarrolle sin entorno virtual por lo que necesitaras algunas de estas librerias ###

# Por falta de tiempo en unos dias actualizare el repositorio con todo.

# pip list

# Package                   Version
# ------------------------- ------------
# altgraph                  0.17.4      
# annotated-types           0.6.0       
# anyio                     3.7.1
# bcrypt                    4.1.2
# certifi                   2023.7.22
# cffi                      1.16.0
# charset-normalizer        3.3.2
# click                     8.1.7
# colorama                  0.4.6
# comtypes                  1.2.0
# cryptography              42.0.5
# darkdetect                0.8.0
# dearpygui                 1.11.1
# dearpygui-ext             0.9.5
# decorator                 4.4.2
# dnspython                 2.4.2
# ecdsa                     0.18.0
# email-validator           2.1.0.post1
# fastapi                   0.104.1
# ffmpeg-python             0.2.0
# future                    0.18.3
# h11                       0.14.0
# httpcore                  1.0.2
# httptools                 0.6.1
# httpx                     0.25.2
# idna                      3.4
# imageio                   2.32.0
# imageio-ffmpeg            0.4.9
# itsdangerous              2.1.2
# Jinja2                    3.1.2
# MarkupSafe                2.1.3
# MouseInfo                 0.1.3
# moviepy                   1.0.3
# numpy                     1.26.2
# orjson                    3.9.10
# packaging                 23.2
# pandas                    2.1.3
# passlib                   1.7.4
# pefile                    2023.2.7
# Pillow                    10.0.1
# pip                       24.0
# proglog                   0.1.10
# pyasn1                    0.6.0
# PyAutoGUI                 0.9.54
# pycparser                 2.22
# pycryptodomex             3.19.0
# pydantic                  2.5.2
# pydantic_core             2.14.5
# pydantic-extra-types      2.1.0
# pydantic-settings         2.1.0
# pydub                     0.25.1
# pyee                      11.0.1
# pygame                    2.5.2
# PyGetWindow               0.0.9
# pyglet                    2.0.10
# pyinstaller               6.1.0
# pyinstaller-hooks-contrib 2023.10
# pylnk                     0.2
# pylnk3                    0.4.2
# pymongo                   4.6.3
# PyMsgBox                  1.0.9
# pyperclip                 1.8.2
# PyRect                    0.2.0
# PyScreeze                 0.1.30
# PySimpleGUI               4.60.5
# python-dateutil           2.8.2
# python-dotenv             1.0.0
# python-jose               3.3.0
# python-magic              0.4.27
# python-multipart          0.0.6
# pytube                    15.0.0
# pytweening                1.2.0
# pytz                      2023.3.post1
# pywin32                   306
# pywin32-ctypes            0.2.2
# pywinauto                 0.6.8
# PyYAML                    6.0.1
# requests                  2.31.0
# rsa                       4.9
# setuptools                68.2.2
# six                       1.16.0
# sniffio                   1.3.0
# starlette                 0.27.0
# tqdm                      4.66.1
# typing_extensions         4.8.0
# tzdata                    2023.3
# ujson                     5.8.0
# urllib3                   2.0.7
# uvicorn                   0.24.0.post1
# watchfiles                0.21.0
# websockets                12.0
# winshell                  0.6

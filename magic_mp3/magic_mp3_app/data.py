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

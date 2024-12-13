import asyncio
from edge_tts import Communicate
import pygame
import librosa
import time
import numpy as np

VOICE = "zh-CN-XiaoxiaoNeural"  # 选择一个合适的中文语音


async def my_tts(text, save_path):
    tts = Communicate(text=text, voice=VOICE, rate="+0%", volume="+0%")

    tts.save_sync(save_path)


def tts_and_play_audio(text):
    tmp_audio_path = "tmp.mp3"
    # 使用 asyncio 来运行异步函数
    asyncio.run(my_tts(text, tmp_audio_path))

    pygame.mixer.init()
    pygame.mixer.music.load(tmp_audio_path)
    pygame.mixer.music.set_volume(0.8)

    x, sr = librosa.load(tmp_audio_path, sr=8000)

    x = x - min(x)
    x = x / max(x)
    x = np.log(x + 1)  # 防止对0取log导致的问题
    x = x / max(x) * 1.2

    pygame.mixer.music.play()
    s_time = time.time()
    try:
        for _ in range(int(len(x) / 800)):
            it = x[int((time.time() - s_time) * 8000)]
            if it < 0:
                it = 0
            with open("tmp.txt", "w") as f:
                f.write(str(float(it)))
            time.sleep(0.1)
    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(0.1)
    with open("tmp.txt", "w") as f:
        f.write("0")

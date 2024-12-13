from pyutils.live2d_control import tts_and_play_audio
import warnings

warnings.filterwarnings("ignore")


from openai import OpenAI

API_KEY = "USE YOUR OWN OPENAI API KEY"
BASE_URL = "USE YOUR OWN BASE URL"
MODEL_NAME = "CHOOSE YOUR MODEL"


def call_model(query):
    client = OpenAI(
        api_key=API_KEY,
        base_url=BASE_URL,
    )
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant",
            },
            {
                "role": "user",
                "content": query,
            },
        ],
        max_tokens=4096,
        temperature=0,
        frequency_penalty=1,
        presence_penalty=1,
        stream=False,
    )
    return response.choices[0].message.content


while True:
    q = input("输入问题:")
    res = call_model(q)
    print(res)
    tts_and_play_audio(res)

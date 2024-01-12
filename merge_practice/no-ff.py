import time
import random


# 지연된 느낌을 내보고자 일부로 메세지를 쪼갠다.
def split_message(message, chunk_size=2):
    return [message[i : i + chunk_size] for i in range(0, len(message), chunk_size)]


def dobongi(message, min_delay=0.5, max_delay=2):
    # 딜레이 시간도 일부로 만들어봤다.
    for chunk in split_message(message):
        time.sleep(random.uniform(min_delay, max_delay))
        yield chunk


responses = {
    "안녕": "안녕하세요!",
    "넌 뭐하는 애니?": "제가 뭘 어쨌다구요?",
    "내가 너 때문에 미치겠다.": "그러시던가요",
    "안녕히 계세요": "안녕히 가세요!",
}

while True:
    user_input = input("User: ")
    if user_input == "종료":
        break
    response = responses.get(user_input, "뭔 소리에요?")

    print(
        f"User>>> {user_input}",
    )
    print("도봉이>>> ", end="")
    for chunk in dobongi(response):
        print(chunk, end="", flush=True)
    print("\n", end="")

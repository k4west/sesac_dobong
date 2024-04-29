import re


def calculate_medal(medal_dict: dict, country: str, medal: str) -> dict:
    """
    medal_dict: 현재 medal 집계 상황이 담긴 사전
    country: medal을 획득한 나라
    medal: 획득한 medal의 종류
    return: 업데이트된 medal 집계 사전
    """
    if country not in medal_dict:
        medal_dict[country] = {"금메달": 0, "은메달": 0, "동메달": 0}
    medal_dict[country][medal] += 1
    return medal_dict


# assert calculate_medal({}, "한국", "금매달") == {"한국": {"금매달: 1"}}


def display_progress(medal_data):
    """
    올림픽 medal을 country별로 집계하는 동안 진행 상황을 발표합니다.
    medal_data: ('country', 'medal')이 포함된 튜플 목록
    return: country를 키로 하고 medal 집계 결과를 값으로 하는 사전
    """
    medal_dict = {}
    total = len(medal_data)

    for index, (country, medal) in enumerate(medal_data, start=1):
        medal_dict = calculate_medal(medal_dict, country, medal)
        print(f"{index} / {total} 메달 처리 중...")

    return medal_dict


def print_medals(medal_dict):
    result = []
    for country, medals in medal_dict.items():
        result.append(
            f"{country}은(는) 금메달 {medals['금메달']}개, 은메달 {medals['은메달']}개, 동메달 {medals['동메달']}개 획득했습니다."
        )
    return "\n".join(result)


medal_data = [
    ("한국", "금메달"),
    ("미국", "금메달"),
    ("중국", "은메달"),
    ("한국", "동메달"),
    ("에스토니아", "금메달"),
]


medal_dict = display_progress(medal_data)
sentences = print_medals(medal_dict)
print(sentences)
print("메달 획득 국가: ", ", ".join(re.findall(r"[가-힣]{2,}(?=은)", sentences)))

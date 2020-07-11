import requests
import json

from URL import SERVER_URL


def test_no_args():
    assert SERVER_URL is not None

    res = requests.get(SERVER_URL)
    resJson = json.dumps(res.json(), sort_keys=True)
    expectedJson = json.dumps({"emoji0": "", "emoji0_emotion": "", "emoji1": "", "emoji1_emotion": "", "emoji2": "",
                               "emoji2_emotion": "", "emoji3": "", "emoji3_emotion": "", "emoji4": "", "emoji4_emotion": ""}, sort_keys=True)

    assert resJson == expectedJson


def test_empty_string():
    assert SERVER_URL is not None

    res = requests.get(SERVER_URL, params={"text": ""})
    resJson = json.dumps(res.json(), sort_keys=True)
    expectedJson = json.dumps({"emoji0": "", "emoji0_emotion": "", "emoji1": "", "emoji1_emotion": "", "emoji2": "",
                               "emoji2_emotion": "", "emoji3": "", "emoji3_emotion": "", "emoji4": "", "emoji4_emotion": ""}, sort_keys=True)

    assert resJson == expectedJson


def test_sample_text():
    assert SERVER_URL is not None

    res = requests.get(SERVER_URL, params={
                       "text": "I know good movies, this ain't one"})
    resJson = json.dumps(res.json(), sort_keys=True)
    expectedJson = json.dumps({"emoji0": "\ud83d\ude45", "emoji0_emotion": "Disapproval", "emoji1": "\ud83d\udcaf", "emoji1_emotion": "Amazement", "emoji2": "\u270b",
                               "emoji2_emotion": "Dismay", "emoji3": "\ud83d\ude0c", "emoji3_emotion": "Optimism", "emoji4": "\ud83d\ude0f", "emoji4_emotion": "Amusement"})

    assert resJson == expectedJson

if __name__ == "__main__":
    test_no_args()
    test_empty_string()
    test_sample_text()

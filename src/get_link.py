import requests
from .builder import Builder


class GetLink:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Referer": "https://www.y2mate.com/youtube/QI7W4UQMmn4",
        }

    def get_key(self, url):
        key_payload = {"k_query": url, "k_page": "home", "hl": "en", "q_auto": 1}
        response = requests.post(
            "https://www.y2mate.com/mates/analyzeV2/ajax",
            data=key_payload,
            headers=self.headers,
        )
        print(f"Key req status: {response.status_code}")
        json_data = response.json()
        builder = Builder()
        return builder.build_link_res(json_data)

    def get_link(self, url):
        download_link_res = requests.post(
            "https://www.y2mate.com/mates/convertV2/index",
            headers=self.headers,
            data=self.get_key(url),
        )
        print(f"Link req status: {download_link_res.status_code}")
        print(f"Status: {download_link_res.json()['status']}")
        link = download_link_res.json()["dlink"]

        return {"link": link, "title": download_link_res.json()["title"]}

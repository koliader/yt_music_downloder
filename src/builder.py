class Builder:
    # Build key res object
    @staticmethod
    def build_key_res(json_data):
        key = json_data["links"]["mp3"]["mp3128"]["k"]
        vid = json_data["vid"]
        link_payload = {
            "vid": vid,
            "k": key
        }
        return link_payload

    # Build link res object
    @staticmethod
    def build_link_res(json_data):
        link = json_data.json()["dlink"]
        title = json_data.json()["title"]

        return {"link": link, "title": title}

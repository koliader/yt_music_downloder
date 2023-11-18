class Builder:
    @staticmethod
    def build_link_res(json_data):
        key = json_data["links"]["mp3"]["mp3128"]["k"]
        vid = json_data["vid"]
        link_payload = {
            "vid": vid,
            "k": key
        }
        return link_payload

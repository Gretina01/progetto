import json
import requests

def get_dictionary_from_url(url:str):
    try:
        out = requests.get(url)
        if out.status_code == 200:
            return json.loads(out.text)
        else:
            raise Exception("error during requests")
    except Exception as ex:
        raise Exception (f"we got an error {ex}")

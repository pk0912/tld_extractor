import os
import requests
import pygtrie as trie
from joblib import dump
from config import PUBLIC_SUFFIX_LIST_URL, SUFFIX_TRIE, DATA_DIR


def fetch_public_suffix_data():
    data = []
    try:
        r = requests.get(PUBLIC_SUFFIX_LIST_URL, stream=True)
        data = r.text.split("\n")
    except Exception as e:
        print("EXCEPTION IN FETCHING PUBLIC SUFFIX LIST : " + str(e))
    return data


def create_public_suffix_trie():
    pub_suf_trie = trie.StringTrie()
    data = fetch_public_suffix_data()
    if len(data) > 0:
        for ps in data:
            if ps != "" and not ps.startswith("//"):
                pub_suf_trie[ps] = True
    return pub_suf_trie


def dump_suffix_trie():
    pub_suf_trie = create_public_suffix_trie()
    try:
        dump(pub_suf_trie, os.path.join(DATA_DIR, SUFFIX_TRIE))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    dump_suffix_trie()





# TLD EXTRACTOR

Features:
- Extracts subdomains, domain and suffix from a URL
- If IP is given instead of domain, returns IP, PORT and IP Version.
- Updates public suffix list by fetching data from https://publicsuffix.org/list/public_suffix_list.dat

---
* Requirements Installation
```bash
pip install -r requirements.txt
```

---
* Updating Public Suffix Trie
```bash
python fetch_public_suffix_list.py
```

---
* Retrieving URL info
```bash
from tld_extractor import get_url_parts
url = "abc.xyz"
print(get_url_parts(url))
```

- Author: Praveen
- Revision: 1

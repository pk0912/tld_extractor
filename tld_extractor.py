import os
from joblib import load
from ipaddress import ip_address
from config import DATA_DIR, SUFFIX_TRIE

pub_suf_trie = load(os.path.join(DATA_DIR, SUFFIX_TRIE))


def is_ip(test_string):
    test_string = test_string.strip()
    try:
        result = ip_address(test_string)
        return {
            "IP": test_string.strip(),
            "PORT": "",
            "IP_VERSION": "IPv" + str(result.version),
        }
    except ValueError:
        ip_port = test_string.rsplit(":", 1)
        if len(ip_port) > 1:
            ip = ip_port[0]
            port = ip_port[1]
            if not port.isnumeric():
                return None
        else:
            return None
        ip = ip.strip("[").strip("]")
        try:
            result = ip_address(ip)
            return {"IP": ip, "PORT": port, "IP_VERSION": "IPv" + str(result.version)}
        except:
            return None
    except Exception as e:
        print(e)
        return None


def get_url_parts(url):
    subdomain = ""
    domain = ""
    suffix = ""
    url = url.strip().split("://")
    if len(url) > 1:
        url = url[1]
    else:
        url = url[0]
    url = url.strip().split("/")[0]
    url = url.split(".", 1)[-1].strip() if url.startswith("www") else url
    check_ip = is_ip(url)
    if check_ip is not None:
        return check_ip
    if pub_suf_trie.has_key(url):
        return {"subdomain": subdomain, "domain": domain, "suffix": url}
    i = 1
    tot_parts = len(url.split("."))
    status = False
    while i < tot_parts:
        url_parts = url.split(".", i)
        start = url_parts[:-1]
        end = url_parts[-1]
        if pub_suf_trie.has_key(end):
            status = True
            suffix = end
            domain = start[-1]
            if len(start) > 1:
                subdomain = start[:-1]
            break
        i += 1

    if status:
        return {"subdomain": subdomain, "domain": domain, "suffix": suffix}
    else:
        return None

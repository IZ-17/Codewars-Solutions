def domain_name(url):
    url = url.replace("http://", "").replace("https://", "")
    url = url.replace("www.", "")
    return url.split(".")[0]
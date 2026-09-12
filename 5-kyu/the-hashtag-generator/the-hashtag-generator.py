def generate_hashtag(s):
    hashtag = f"#{''.join(st.title() for st in s.split())}"
    return hashtag if 1 < len(hashtag) <= 140 else False
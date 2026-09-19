def bouncing_ball(h, bounce, window):
    result = 1
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        while h * bounce > window:
            result += 2
            h *= bounce
        return result
    return -1
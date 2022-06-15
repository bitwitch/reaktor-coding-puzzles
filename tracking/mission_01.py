import base64

if __name__ == "__main__":
    with open("distress_signal.txt", "r") as f:
        signal = f.read().strip()

    length = 16
    message = ""

    for c in signal:
        if c in message:
            message = c
        else:
            message += c
        if len(message) == length:
            break

    print(base64.b64decode(message))

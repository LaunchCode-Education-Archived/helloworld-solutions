for i in range(1, 21):
    msg = str(i) + ": "
    if i % 3 == 0:
        msg = msg + "Hip"

    if i % 7 == 0:
        msg = msg + "Hooray"

    print(msg)

kata = "The right format"
# kata = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm"
# kata = ""
# kata = "012345678901234567890123456789012345678901"

if len(kata) > 42:
    print("String is too long")
else:
    dash = (42 - len(kata)) * "-"
    print(dash + kata, end="")

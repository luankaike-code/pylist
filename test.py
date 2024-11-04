import re

text = "./imgs/oi/tudo/bem/img.png"
text = re.split(r"[\\/]", text)
text = list(filter(lambda x: x != ".", text))
text.reverse()
text = "/".join(text)
text = re.split(r"[\\/]", text, maxsplit=1)
text[1] = re.split(r"[\\/]", text[1])
text[1].reverse()
text[1] = "/".join(text[1])
text = "/".join(text)
text = text.replace("/", ":", 1)

print(text)
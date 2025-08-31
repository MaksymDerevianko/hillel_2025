import re

adwentures_of_tom_sawer = """Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked .... 
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# task 01: replace line breaks with space
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02: replace "...." with space
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03: remove extra spaces
adwentures_of_tom_sawer = re.sub(r"\s+", " ", adwentures_of_tom_sawer)

# task 04: count letter 'h'
print("task 04:", adwentures_of_tom_sawer.count("h"))

# task 05: count words starting with uppercase
uppercase_words = [word for word in adwentures_of_tom_sawer.split() if word.istitle()]
print("task 05:", len(uppercase_words))

# task 06: position of second 'Tom'
first_index = adwentures_of_tom_sawer.find("Tom")
second_index = adwentures_of_tom_sawer.find("Tom", first_index + 1)
print("task 06:", second_index)

# task 07: split into sentences
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(".")

# task 08: print 4th sentence in lowercase
if len(adwentures_of_tom_sawer_sentences) >= 4:
    print("task 08:", adwentures_of_tom_sawer_sentences[3].lower())

# task 09: check if any sentence starts with 'By the time'
starts_with_phrase = any(s.strip().startswith("By the time") for s in adwentures_of_tom_sawer_sentences)
print("task 09:", starts_with_phrase)

# task 10: count words in last sentence
last_sentence_words = adwentures_of_tom_sawer_sentences[-1].split()
print("task 10:", len(last_sentence_words))
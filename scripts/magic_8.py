import random

# https://github.com/arduino/Arduino/blob/master/build/shared/examples/10.StarterKit/p11_CrystalBall/p11_CrystalBall.ino
answers = """
Yes
Most likely
Certainly
Outlook good
Unsure
Ask again
Doubtful
No
""".strip().split("\n")

answer = random.choice(answers)

print(answer)

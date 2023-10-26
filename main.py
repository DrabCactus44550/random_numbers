import random
class Encrypt:
    def __init__(self):
        self.num2 = random.randint(1, 1000)
    def enc(self, num):
        opert=random.randint(1,6)
        if opert==1:
            enc_num = num + self.num2
        if opert==2:
            enc_num = num - self.num2
        if opert==3:
            enc_num = num * self.num2
        if opert==4:
            enc_num = num / self.num2
        if opert==5:
            enc_num = num ** 2
        if opert==6:
            enc_num = num // 2
        return enc_num
    def dec(self, enc_num):
        orig_num = enc_num - self.num2
        return orig_num
enc = Encrypt()
orig = int(input("Введіть число: "))
enc_num = enc.enc(orig)
print(f"Оригінальне число: {orig}")
print(f"Число після операції: {enc_num}")


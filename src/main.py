# -*- coding = utf-8 -*-
# @Time : 2020/8/7 0:15
# @Author : Cristime
# @File : main.py
# @Software: NeoVim(Vim Like)


Char_Case = int(5)

# 主程序
def Main():
    Interface()
    mode = int(input('Please select a mode: '))
    while (mode != 1 and mode != 2):
        print("\nBad input! Please enter again!")
        mode = int(input('Please select a mode: '))
    GetInput(mode)


# 加密
def Encrypt(Passwd):
    try:
        print("The encrypted password is: ", end='')
        i = 0
        while i < len(Passwd):
            if Passwd[i] == ' ':
                print(Passwd[i], end='')
            else:
                print(chr(ord(Passwd[i]) + int(Char_Case)), end='')
            i += 1
        print("")
    except Exception as Error:
        print("An error occurred: ", Error)
    pause()


# 解密
def Decrypt(Passwd):
    try:
        print("The decrypted password is: ", end='')
        for i in range(0, len(Passwd)):
            if Passwd[i] == ' ':
                print(Passwd[i], end='')
            else:
                print(chr(ord(Passwd[i]) - int(Char_Case)), end='')
    except Exception as Error:
        print("An error occurred: ", Error)
    print()
    pause()


# 主界面
def Interface():
    print("Encrypt_Password Version_0.1")
    print("-"*30)
    print("1. Encrypt a password.")
    print("2. Decrypt a password.")
    print("-"*30)


# 获取输入
def GetInput(mode):
    if mode == 1:
        passwd = input("Enter password: ")
        passwd_a = input("Enter password again: ")
        while passwd != passwd_a:
            print("Password error! Please enter the password again! ", end="\n\n")
            passwd = input("Enter password: ")
            passwd_a = input("Enter password again: ")
        Encrypt(passwd)

    else:
        passwd = input("Enter the encrypted password: ")
        Decrypt(passwd)

# 暂停函数
def pause():
    tmp = input("Please input ENTER to continue. ")

# 程序从这里开始
if __name__ == "__main__":
    Main()

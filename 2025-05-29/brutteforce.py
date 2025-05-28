#!/usr/bin/python3

import zipfile
# Для работы с архивом лучше использовать 7z
# Шифр дложен быть с
# Encryption method:ZipCripto
# Обязательно указать пароль при создании архива
# Расширение архива должно быть *.zip

class Archive:
    def __init__(self, path, description):
        self.path = path
        self.description = description
        self.password = None

    def getinfo(self):
        print(f"Path: {self.path} \n Desc: {self.description} \n"
              f"Password: {self.password}")

class Bruteforce:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def hack(self, archive):
        zip_file = zipfile.ZipFile(archive)
        password = None
        f = open(self.dictionary, 'r')
        for line in f.readlines():
            password = line.strip('\n')
            try:
                zip_file.extractall(pwd=password.encode())
                print("-"*11)
                print(f"RESULT:{password}")
                f.close()
                return(True, password)
            except:
                print(password)
        f.close()
        return (False, None)

class Library:
    def __init__(self, bruteforce):
        self.bruteforce = bruteforce
        self.archives = []

    def showarchives(self):
        for archive in self.archives:
            archive.getinfo()
            print("")

    def hackall(self):
        for archive in self.archives:
            if archive.password == None:
                res = self.bruteforce.hack(archive.path)
                if res[0] == True:
                    archive.password = res[1]

library = Library(Bruteforce("dictionary.txt")) #Передаем файл с паролями
library.archives.append(Archive("test.zip", "TEST")) #Передаем архив
library.showarchives() #Показываем на экране данные о архивах
library.hackall() #Вызываем взлом методов bruteforce
library.showarchives() #Показываем на экране данные о архивах


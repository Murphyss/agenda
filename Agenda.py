#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#program Agenda v1
#qpy:kivy

#POGForever

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
import sqlite3
import datetime
conn = sqlite3.connect("Clientes.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS agenda(
Cliente varchar(30) NOT NULL,
Valor real NOT NULL,
Data date NOT NULL
)
""")
class Menu(Screen):
    global cursor
    global conn
    def __init__(self,**kwargs):
        super(Menu,self).__init__(**kwargs)
        self.grid = GridLayout(cols=3)
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text="Agenda"))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=' '))

        self.grid.add_widget(Label(text=" "))
        self.b_cadastro = Button(text='Cadastro')
        self.b_cadastro.bind(on_press = self.cadastro)
        self.grid.add_widget(self.b_cadastro)
        self.grid.add_widget(Label(text=" "))

        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))

        self.grid.add_widget(Label(text=" "))
        self.b_orc = Button(text='Orçamento')
        self.b_orc.bind(on_press = self.orc)
        self.grid.add_widget(self.b_orc)
        self.grid.add_widget(Label(text=" "))
        
        self.grid.add_widget(Label(text=' '))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text='Author:Murphys'))
        self.grid.add_widget(Label(text=' '))

        self.add_widget(self.grid)


    def cadastro (self,*args):
        self.manager.current = "scc"
        

    def orc(self,*args):
        self.manager.current = "scd"


class Cadastroo(Screen):
    def __init__(self,**kwargs):
        global cursor
        global conn
        super(Cadastroo,self).__init__(**kwargs)
        self.grid = GridLayout(cols=3)
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))
        
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text="Cadastro"))
        self.grid.add_widget(Label(text=" "))
        
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=' '))

        self.grid.add_widget(Label(text="Cliente:"))
        self.inpc = TextInput(multiline = False)
        self.grid.add_widget(self.inpc)
        self.grid.add_widget(Label(text=" "))

        self.grid.add_widget(Label(text="Valor:"))
        self.inpt = TextInput(multiline = False)
        self.grid.add_widget(self.inpt)
        for contador in range(0,8):
            self.grid.add_widget(Label(text=" "))
       
        self.bt = Button(text="Enviar")
        self.bt.bind(on_press= self.Epop)
        self.grid.add_widget(self.bt)
        
        for contador in range(0,8):
            self.grid.add_widget(Label(text=" "))
            
        self.btd = Button(text='Deletar Dados')
        self.btd.bind(on_press = self.Opop)
        self.grid.add_widget(self.btd)
        for contador in range(0,11):
            self.grid.add_widget(Label(text=" "))
            
        self.btv = Button(text='Voltar')
        self.btv.bind(on_press=self.VV)
        self.grid.add_widget(self.btv)
        self.grid.add_widget(Label(text=' '))
        
        

        self.add_widget(self.grid)

    def Epop(self,*args):
        gri = GridLayout(cols=3)
        gri.add_widget(Label(text=" "))
        gri.add_widget(Label(text="Certeza?"))
        gri.add_widget(Label(text=" "))
        
        gri.add_widget(Label(text=" "))
        con = Button(text='Sim')
        con.bind(on_press = self.Enviar)
        gri.add_widget(con)
        gri.add_widget(Label(text=" "))

        gri.add_widget(Label(text=" "))
        cono = Button(text ='Não')
        cono.bind(on_press = self.demis)
        gri.add_widget(cono)
        gri.add_widget(Label(text=" "))
        
        self.pop = Popup(title = "Confirmação",content = gri,size_hint=(None, None), size=(300, 300))
        
        self.pop.open()
    def demis(self,*args):
        self.pop.dismiss()

    def Opop(self,*args):
        
        gri = GridLayout(cols=3)
        gri.add_widget(Label(text=" "))
        gri.add_widget(Label(text="Isso ira apagar TUDO"))
        gri.add_widget(Label(text=" "))
        
        gri.add_widget(Label(text=" "))
        con = Button(text='Sim')
        con.bind(on_press = self.delall)
        gri.add_widget(con)
        gri.add_widget(Label(text=" "))

        gri.add_widget(Label(text=" "))
        cono = Button(text ='Não')
        cono.bind(on_press = self.demiss)
        gri.add_widget(cono)
        gri.add_widget(Label(text=" "))
        
        self.popp = Popup(title = "Confirmação",content = gri,size_hint=(None, None), size=(300, 300))
        
        self.popp.open()
        
    def demiss(self,*args):
        self.popp.dismiss()

        
    def delall(self,*args):
        cursor.execute("DELETE FROM agenda")
        conn.commit()
        self.popp.dismiss()

    def VV(self,*args):
        self.manager.current = 'scm'
    def Enviar(self,*args):
        self.clien=self.inpc.text
        self.val=self.inpt.text
        self.dat = datetime.date.today()
        self.dat=self.dat.strftime('%y-%m-%d')
        self.perso = self.clien,self.val,self.dat
        cursor.execute("INSERT INTO agenda VALUES (?,?,?)",self.perso)
        conn.commit()
        self.pop.dismiss()
        
class Dato(Screen):
    def __init__(self,**kwargs):
        super(Dato,self).__init__(**kwargs)
        self.grid = GridLayout(cols=3)
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))
        
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text="Orçamento"))
        self.grid.add_widget(Label(text=" "))
        
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=' '))
        
        self.grid.add_widget(Label(text=' '))
        self.grid.add_widget(Label(text="Data inicial:"))
        self.grid.add_widget(Label(text=' '))
        
        self.grid.add_widget(Label(text='Dia'))
        self.grid.add_widget(Label(text='Mes'))
        self.grid.add_widget(Label(text='Ano'))
        
        self.inpdd = TextInput(multiline = False)
        self.grid.add_widget(self.inpdd)
        self.inpdm = TextInput(multiline = False)
        self.grid.add_widget(self.inpdm)
        self.inpda = TextInput(multiline = False)
        self.grid.add_widget(self.inpda)
        
        self.grid.add_widget(Label(text=' '))
        self.grid.add_widget(Label(text="Data Final:"))
        self.grid.add_widget(Label(text=' '))

        self.grid.add_widget(Label(text='Dia'))
        self.grid.add_widget(Label(text='Mes'))
        self.grid.add_widget(Label(text='Ano'))
        
        self.inpdf = TextInput(multiline = False)
        self.grid.add_widget(self.inpdf)
        self.inpdfe = TextInput(multiline = False)
        self.grid.add_widget(self.inpdfe)
        self.inpdfa = TextInput(multiline = False)
        self.grid.add_widget(self.inpdfa)
        
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=' '))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=" "))
        self.grid.add_widget(Label(text=' '))
        self.grid.add_widget(Label(text=" "))
        self.bt = Button(text="Gerar orçamento")
        self.bt.bind(on_press= self.Gorc)
        self.grid.add_widget(self.bt)
        for contador in range(0,14):
            self.grid.add_widget(Label(text=" "))
        
        self.btv = Button(text='Voltar')
        self.btv.bind(on_press=self.VV)
        self.grid.add_widget(self.btv)
        self.grid.add_widget(Label(text=' '))

        self.add_widget(self.grid)
        
    def Gorc(self,*args):
        di = StringProperty()
        df= StringProperty()
        self.conta=StringProperty()
        self.conta = 0
        t1=  self.inpdd.text
        t2=  self.inpdm.text
        t3=  self.inpda.text
        di=(t3+"-"+t2+"-"+t1)
        
        d1 = self.inpdf.text
        d2 = self.inpdfe.text
        d3 = self.inpdfa.text
        df=d3+"-"+d2+"-"+d1
        
        self.dt = di,df
        meio = cursor.execute("SELECT Valor FROM agenda WHERE Data >= (?) and Data <= (?)",self.dt).fetchall()
        for cont in range(0,len(meio)):
            mat = meio[cont][0]
            mat = float(mat)
            self.conta += (70 * mat)/100
        self.conta = str(self.conta)   
        g=GridLayout(cols=2)
        l1=Label(text='Ganhou:')
        l2=Label(text=self.conta)
        g.add_widget(l1)
        g.add_widget(l2)
        bt=Button(text="Fechar")
        bt.bind(on_press = self.pquit)
        g.add_widget(bt)
        self.Gpop = Popup(title='Orçamento',content = g,size_hint=(None, None), size=(300, 300))
        self.Gpop.open()
            
    def pquit(self,*args):
        self.Gpop.dismiss()
        
    def VV(self,*args):
        self.manager.current = 'scm'
        


class Agenda(App):
    def build(self):
        self.sm = ScreenManager()
        self.scm=Menu(name = "scm")
        self.scc=Cadastroo(name = "scc")
        self.scd=Dato(name ="scd")
        self.sm.add_widget(self.scm)
        self.sm.add_widget(self.scc)
        self.sm.add_widget(self.scd)
        
        return self.sm

Agenda().run()

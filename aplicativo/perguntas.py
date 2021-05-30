from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.screen import MDScreen

class PerguntasScreen(MDScreen):
    dialog=None
    def __init__(self, **kwargs):
        super(PerguntasScreen,self).__init__(**kwargs)
        ...
        
    def mostrar_notificacao(self,nome,texto):
        text=''
        users=['saidino','Bilal'.lower()]
        print(texto)
        for i in users:
            if i.lower() ==texto.lower():
                print('O administrador !!!')
            else:
                print('Not logaed')
        if(texto.lower() not in users):
            text='Voce nao esta permitido a user este servico'
        else:
            text=f'oi [color=#ff0000FF]{texto} [/color]Seja Bem vindo ao App'
        def cancel_notify():
            # self.dialog.dismiss()
            ...

        btn1=MDFlatButton(text='Cancel',on_release=lambda x:self.dialog.dismiss())
        if self.dialog==None:
            print('Me clicast')
            self.dialog=MDDialog(
            title="Administradores",
            # type='simple',
            size_hint=(.8,.5),
            auto_dismiss=False,
            text=text,
            buttons=[btn1]
        )
        self.dialog.open()

        

        

        

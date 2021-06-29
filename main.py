
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from random import randint

Window.size = (1300,600)
# R G B
Window.clearcolor = (0.19, 0.22, 0.22, 1)


class Generator(App):
    def build(self):
        #return window object
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.65, 0.90)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

         # label widget
        self.greeting = Label(
                        text= "Cześć Tobie dziś! Wygeneruj motywacyjny cytat na dziś !",
                        font_size= 24,
                        italic=True,
                        color= '#eab676'
                        )
        self.window.add_widget(self.greeting)

        # image widget
        self.window.add_widget(Image(source="sky.jpg"))

        # label widget
        self.quotation = Label(
                        text= "",
                        font_size= 20,
                        italic=True,
                        color= '#eab676',
                        )
        self.window.add_widget(self.quotation)

        # button widget
        self.button = Button(
                      text= "Losuj cytat!",
                      size_hint = (1, 0.5),
                      bold= True,
                      italic=True,
                      background_color ='#76b5c5',
                      #remove darker overlay of background colour
                      background_normal = ""
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        # close button widget
        self.button = Button(
                      text= "Zamknij!",
                      size_hint= (1,0.3),
                      bold= True,
                      italic=True,
                      background_color ='#76b5c5',
                      #remove darker overlay of background colour
                      background_normal = "",
                      )
        self.button.bind(on_press=self.closeFun)
        self.window.add_widget(self.button)

        return self.window

    def closeFun(self, object):
        App.get_running_app().stop()
        Window.close()

    def callback(self, event):
        # pobieranie z pliku txt cytatow
        with open("cytaty.txt") as f:
            content = []
            content = f.readlines()
      
        #sprawdzanie ilosci cytatow w liscie, zaczyna od 0
        num_of_quo = len(content) - 1

        #losowanie liczby w zaleznosci od ilosci cytatow
        rando = randint(0, num_of_quo)

        # sprawdzanie ilosci cytatow w liscie, zaczyna od 0
        num_of_quo = len(content) - 1
            
        self.quotation.text = content[rando]

# urochamia klase aplikacji
if __name__ == "__main__":
    Generator().run()

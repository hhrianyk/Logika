from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        button = Button(text="Go to Second Screen", size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        button.bind(on_press=self.change_screen)
        layout.add_widget(button)
        self.add_widget(layout)

    def change_screen(self, *args):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        button = Button(text="Go Back", size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        button.bind(on_press=self.change_screen)
        layout.add_widget(button)
        self.add_widget(layout)

    def change_screen(self, *args):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        return sm

if __name__ == '__main__':
    MyApp().run()

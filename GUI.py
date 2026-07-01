import PySimpleGUI as sg

def home(location=(200,200)):
    layout_home = [[sg.Text("PIZZA SHOPPING LIST GENERATOR")],
              [sg.Button("CREATE MENU")],
              [sg.Button("MODIFY PIZZAS")],
              [sg.Button("EXIT")],]

    window_home = sg.Window("Pizza Shopping List", layout_home, size=(600, 400), location=location)

    while True:
        event, values = window_home.read()
        if event == sg.WINDOW_CLOSED or event == 'EXIT':
            window_home.close()
            break
        if event == "CREATE MENU":
            loc = window_home.current_location()
            window_home.close()
            pizzas(loc, window_home)
            break



def pizzas(location=(0,0), previous_window=None):
    layout_pizzas = [[sg.Text("PIZZA SHOPPING LIST")]]
    window_pizzas = sg.Window("Pizza Shopping List", layout_pizzas, size=(600, 400), location=location)

    while True:
        event, values = window_pizzas.read()
        if event == sg.WIN_CLOSED:
            window_pizzas.close()
            break

if __name__ == "__main__":
    home()
from nicegui import ui
import timer_app

'''
Main Screen
'''

@ui.page('/main_screen')
def main_screen():
    ui.add_css('''
        .button_padding {
            padding: 0.25rem;
        }
    ''')

    ui.query('body').style(f'background-color: #ddeeff')

    with ui.row().classes("w-full").style("justify-content: space-evenly;"):
        with ui.column().style("justify-content: flex-start;"):
            with ui.card().classes("w-[250px] button_padding").style("text-align: center;"):
                ui.label("APPLICATIONS:").classes('w-full').style("font-size: 175%; font-weight: 400").tailwind.background_color('orange-200')
            with ui.card().classes('button_padding'):
                ui.button("TIMER", on_click=lambda: ui.navigate.to(f'/timer_app')).classes("w-[100px]")

        with ui.card().style("background-color: rgb(226 232 240);"):
            ui.label("PAST WORKOUTS:").classes('w-full').style("font-size: 175%; font-weight: 400")
            ui.link("place holder")

'''
took about 2 hours to create layout, design and figure out how to link page from login screen
'''
from nicegui import ui

'''
Timer application screen
'''
num_exercises = [1]

def add_exercise():
    next = num_exercises[-1] + 1
    num_exercises.append(next)
    second_column.refresh()

@ui.refreshable
def second_column():
    with ui.column().classes("items-center"):                  
        with ui.card().classes("button_padding"):
            ui.button("Add Group")

        with ui.card().classes("w-[400px]"):
            with ui.row().classes("w-full").style("text-align: center;"):
                ui.label("Exercise Group").classes("w-full").style("font-size: 175%; font-weight: 400")
            with ui.row().classes("w-full").style("justify-content: space-between; align-items: center;"):
                with ui.card().classes("button_padding"):
                    ui.button("Add exercise line:", on_click=add_exercise)
                ui.label("Duration min.").style("font-size: 125%; font-weight: 400")
            for i in num_exercises:
                with ui.row().classes("w-full").style("justify-content: space-between;"):
                    ui.input(f"Exercise {i}").classes("w-[275px]")
                    ui.dropdown_button(f"1")
            with ui.row().classes("w-full"):
                ui.label("Repeat")
                ui.dropdown_button("0")




@ui.page("/timer_app")
def timer_app():
    ui.add_css('''
        .button_padding {
            padding: 0.25rem;
        }
    ''')    
    ui.query('body').style(f'background-color: #ddeeff')

    with ui.card().classes("w-full h-[800px]"):
        with ui.row().classes("w-full h-full").style("justify-content: space-evenly;"):
            with ui.column():                                               # column 1
                with ui.row().classes("w-full").style("align-items: center;"):
                    ui.label("ROUNDS:").style("font-size: 175%; font-weight: 400")
                    ui.dropdown_button("0")
                with ui.card().classes('button_padding'):
                    ui.button("Start")

            second_column()                                                 # column 2

            with ui.column():                                               # column 3
                with ui.card().classes("w-[300px]").style("text-align: center;"):
                    ui.label("Current Workout:").classes("w-full")

# timer_app()
# ui.run()
'''
3 hour current work time
'''

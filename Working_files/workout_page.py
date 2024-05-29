from nicegui import ui


@ui.page("/workout_screen")
def workout_screen():
    ui.add_css('''
        .button_padding {
            padding: 0.25rem;
        }
    ''')    
    ui.query('body').style(f'background-color: #ddeeff')
    with ui.row().classes("w-full h-[200px]"):
        with ui.card().classes("w-full h-full"):
            ui.label("top row")

    with ui.row().classes("w-full").style("justify-content: space-evenly;"):
        with ui.column().classes("w-[400px] h-[1100px]"):
            with ui.card().classes("w-full h-full").style("background-color: rgb(240 249 255); justify-content: center; align-items: center;"):
                ui.label("first column")


        with ui.column().classes("w-[950px] h-[1100px]"):
            with ui.card().classes("w-full h-full").style("background-color: rgb(240 249 255); justify-content: center; align-items: center;"):    
        
                with ui.card().classes("w-full h-[200px]"):
                    with ui.row().classes("w-full"):
                        ui.label("this is a row")

                with ui.card().classes("w-full h-full"):
                    ui.label("starting here")


        with ui.column().classes("w-[400px] h-[1100px]"):
            with ui.card().classes("w-full h-full").style("	background-color: rgb(240 249 255); justify-content: center; align-items: center;"):
                ui.label("third column")


# workout_page()
# ui.run
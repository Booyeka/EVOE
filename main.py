from nicegui import ui

'''
LOGIN SCREEN
'''
ui.query('body').style(f'background-color: #ddeeff')

with ui.column().classes('w-full items-center'):
    with ui.card().classes('w-[400px] items-center'):
        ui.label("") #                   creating space
        ui.label("") #                   creating space        
        ui.label('Login or Create Account:').style('color: #808080; font-size: 200%; font-weight: 400')
        ui.label("") #                   creating space
        ui.label("") #                   creating space
        ui.button('Create Account')
        ui.label("") #                   creating space
        ui.label("") #                   creating space
        ui.input(label='Username')
        ui.input(label='Password')
        ui.label("") #                   creating space    
        ui.button('LOG IN')

ui.run()

'''
4 hours
'''

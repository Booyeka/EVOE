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
        ui.button('LOG IN', on_click=lambda: ui.navigate.to(f'/main_screen'))


'''
login screen took 4 hours to complete. 1 hour was me hyperfocusing on an unimportant task. As well this was my first interaction with the gui framework
'''


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


'''
Timer application screen
'''
num_exercises = [1]
workout_dict = {}
exercise_data = {}

ex_list = ["" for i in range(10)]
dur_list = [1 for i in range(10)]
repeat = []
rounds = [1]

def add_exercise():
    next = num_exercises[-1] + 1
    num_exercises.append(next)
    second_column.refresh()

def extract_exercises():
    b = False
    for i in ex_list:
        if "" != i:
            b = True
    if not b:
        return None

    if not workout_dict:
        group_num = 1
        workout_dict.update({
            'group1' : {} 
        })
    else:
        group_num = len(workout_dict)+1
        next_group = {f'group{group_num}' : {}}
        workout_dict.update(next_group)

    for count, ex in enumerate(ex_list):
        workout_dict[f'group{group_num}'].update({
            f"ex{count+1}" : {
                'ex_desc' : ex,
                'dur' : dur_list[count]
            }
    })
    # print(workout_dict)
    second_column.refresh()
    third_column.refresh()
    for count, i in enumerate(ex_list):
        ex_list[count] = ""
    for count, d in enumerate(dur_list):
        dur_list[count] = 1  
    

def update_string(string, pos):
    ex_list[pos] = string
    # print(ex_list[pos])
def update_dur(dur, pos):
    dur_list[pos] = dur
def update_repeat(val):
    repeat.append(val)
def update_rounds(val):
    rounds[0] = val

@ui.refreshable
def second_column():
    with ui.column().classes("items-center"):                  
        with ui.card().classes("button_padding"):
            ui.button("Add Group", on_click=extract_exercises)

            '''
            when clicked, take info in text boxes and update workout_dict with data
            '''

        with ui.card().classes("w-[550px]"):
            with ui.row().classes("w-full").style("text-align: center;"):
                ui.label("Exercise Group").classes("w-full").style("font-size: 175%; font-weight: 400")
            with ui.row().classes("w-full").style("justify-content: space-between; align-items: center;"):
                with ui.card().classes("button_padding"):
                    ui.button("Add exercise line:", on_click="")
                ui.label("Duration min.").style("font-size: 125%; font-weight: 400")
            
            # easiest way to complete on first run, but has to be a better way...
            with ui.row().classes("w-full").style("justify-content: space-between; align-items: flex-end;"):
                ex1 = ui.input(on_change=lambda e: update_string(e.value, 0)).classes("w-[425px]")
                dur1 = ui.select([1,2,3,4,5,6,7,8,9,10], value=1, on_change=lambda e: update_dur(e.value, 0))

            with ui.row().classes("w-full").style("justify-content: space-between; align-items: flex-end;"):
                ex2 = ui.input(on_change=lambda e: update_string(e.value, 1)).classes("w-[425px]")
                dur2 = ui.select([1,2,3,4,5,6,7,8,9,10], value=1, on_change=lambda e: update_dur(e.value, 1))
               
            with ui.row().classes("w-full").style("justify-content: space-between; align-items: flex-end;"):
                ex3 = ui.input(on_change=lambda e: update_string(e.value, 2)).classes("w-[425px]")
                dur3 = ui.select([1,2,3,4,5,6,7,8,9,10], value=1, on_change=lambda e: update_dur(e.value, 2))
                
            with ui.row().classes("w-full").style("justify-content: space-between; align-items: flex-end;"):
                ex4 = ui.input(on_change=lambda e: update_string(e.value, 3)).classes("w-[425px]")
                dur4 = ui.select([1,2,3,4,5,6,7,8,9,10], value=1, on_change=lambda e: update_dur(e.value, 3))
              
            with ui.row().classes("w-full").style("justify-content: space-between; align-items: flex-end;"):
                ex5 = ui.input(on_change=lambda e: update_string(e.value, 4)).classes("w-[425px]")
                dur5 = ui.select([1,2,3,4,5,6,7,8,9,10], value=1, on_change=lambda e: update_dur(e.value, 4))
                                                                
            with ui.row().classes("w-full").style("justify-content: space-between; align-items: flex-end;"):
                ex6 = ui.input(on_change=lambda e: update_string(e.value, 5)).classes("w-[425px]")
                dur6 = ui.select([1,2,3,4,5,6,7,8,9,10], value=1, on_change=lambda e: update_dur(e.value, 5))
                              
            with ui.row().classes("w-full").style("justify-content: space-between; align-items: flex-end;"):
                ex7 = ui.input(on_change=lambda e: update_string(e.value, 6)).classes("w-[425px]")
                dur7 = ui.select([1,2,3,4,5,6,7,8,9,10], value=1, on_change=lambda e: update_dur(e.value, 6))
               
            with ui.row().classes("w-full").style("justify-content: space-between; align-items: flex-end;"):
                ex8 = ui.input(on_change=lambda e: update_string(e.value, 7)).classes("w-[425px]")
                dur8 = ui.select([1,2,3,4,5,6,7,8,9,10], value=1, on_change=lambda e: update_dur(e.value, 7))
               
            with ui.row().classes("w-full").style("justify-content: space-between; align-items: flex-end;"):
                ex9 = ui.input(on_change=lambda e: update_string(e.value, 8)).classes("w-[425px]")
                dur9 = ui.select([1,2,3,4,5,6,7,8,9,10], value=1, on_change=lambda e: update_dur(e.value, 8))
               
            with ui.row().classes("w-full").style("justify-content: space-between; align-items: flex-end;"):
                ex10 = ui.input(on_change=lambda e: update_string(e.value, 9)).classes("w-[425px]")
                dur10 = ui.select([1,2,3,4,5,6,7,8,9,10], value=1, on_change=lambda e: update_dur(e.value, 9))
                                                                              

            with ui.row().classes("w-full").style("align-items: center;"):
                ui.label("Repeat").style("font-size: 110%;")
                ui.select([0,1,2,3,4,5,6,7,8,9,10], value=0, on_change= lambda e: update_repeat(e.value))

@ui.refreshable
def third_column():
    with ui.column():                                               # column 3
        with ui.card().classes("w-[500px] h-[1000px]").style("text-align: center;"):
            ui.label("Current Workout:").classes("w-full").style("font-size: 175%;")
            ui.label("________________________________").classes("w-full")
            for count,k in enumerate(workout_dict.keys()):
                with ui.card().tight():
                    with ui.row():
                        ui.label(f"{k}").style("font-size: 120%;")
                        try:
                            if 0 != repeat[count]:
                                ui.label(f"X {repeat[count]} TIMES").style("font-size: 110%")                            
                        except IndexError:
                            repeat.append(0)
                            if 0 != repeat[count]:
                                ui.label(f"X {repeat[count]} TIMES").style("font-size: 110%")
                    with ui.card():
                        for g, v in workout_dict[k].items():
                            if v['ex_desc'] == "":
                                continue
                            else:
                                ui.label(f"{v['ex_desc']} x {v['dur']} minute(s)").style('font-size: 110%;')
                            '''
                            add group button functionalty before continuing
                            '''

@ui.page("/timer_app")
def timer_app():
    ui.add_css('''
        .button_padding {
            padding: 0.25rem;
        }
    ''')    
    ui.query('body').style(f'background-color: #ddeeff')

    with ui.card().classes("w-full h-[1100px]").style("	background-color: rgb(240 249 255);"):
        with ui.row().classes("w-full h-full").style("justify-content: space-between;"):
            with ui.column():                                               # column 1
                with ui.row().classes("w-full").style("align-items: center; background-color: rgb(255 255 255);"):
                    ui.label("ROUNDS:").classes("w-[125px] h-[57px]").style("font-size: 185%; font-weight: 400; background-color: rgb(240 249 255);")
                    ui.select([1,2,3,4,5,6,7,8,9,10], value=1, on_change=lambda e: update_rounds(e.value))
                with ui.card().classes('button_padding'):
                    ui.button("Start", on_click=lambda: ui.navigate.to(f'/workout_screen'))

            second_column()                                                 # column 2
            third_column()                                                  # column 3

'''
10 hour work time -- at least 2-3 hours were spent going back and forth on how to capture user input to store in dictionary
'''


'''
WORKOUT SCREEN
'''
@ui.page("/workout_screen")
def workout_screen():
    ui.add_css('''
        .button_padding {
            padding: 0.25rem;
        }
    ''')    
    ui.query('body').style(f'background-color: #ddeeff')
    with ui.row().classes("w-full h-[150px]").style("justify-content: center;"):
        with ui.card().classes("w-[1950px] h-full").style("background-color: rgb(240 249 255);"):
            ui.label("top row")

    with ui.row().classes("w-full h-[875px]").style("justify-content: space-evenly;"):
        with ui.column().classes("w-[450px] h-full "):
            with ui.card().classes("w-full h-full").style("background-color: rgb(240 249 255); justify-content: center; align-items: center;"):
                ui.label("first column")


        with ui.column().classes("w-[1150px] h-full"):
            with ui.card().classes("w-full h-full").style("background-color: rgb(240 249 255); justify-content: center; align-items: center;"):    
        
                with ui.card().classes("w-full h-[1000px]").style(" border-color: rgb(0 0 0);"):
                    with ui.row().classes("w-full h-full"):
                        ui.label("this is a row")

                with ui.card().classes("w-[475px] h-full").style("border-color: rgb(0 0 0);"):
                    ui.label("starting here")


        with ui.column().classes("w-[450px] h-full"):
            with ui.card().classes("w-full h-full").style("	background-color: rgb(240 249 255); justify-content: center; align-items: center;"):
                ui.label("third column")


ui.run()
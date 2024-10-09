from nicegui import ui
import json
from workout_page import workout_screen

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
with open("JSONS\saved_workouts.json", "r") as openfile:
    saved_workouts = json.load(openfile)
saved_workout_count = [0]

@ui.refreshable
def workout_display_column():
    if not saved_workouts:
        pass
    else:
        other_info_ref = saved_workouts[saved_workout_count[0]]["other_info"]
        repeat = other_info_ref['repeats_list']
        date = other_info_ref['date']
        time = other_info_ref['time']
        rounds = other_info_ref['rounds']
        total_mins = other_info_ref['total_mins']
        with ui.card():
            with ui.scroll_area().classes("w-[600px] h-[600px]"):
                with ui.column():
                    ui.label(f"DATE: {date}")
                    ui.label(f"TIME: {time}")
                    ui.label(f"TOTAL MINUTES: {total_mins[0]}")
                    ui.label(f"ROUNDS: {rounds[0]}")                
                for count,k in enumerate(saved_workouts[saved_workout_count[0]].keys()):
                    if k == 'other_info':
                        continue
                    with ui.card().tight():
                        with ui.row():
                            ui.label(f"{k}").style("font-size: 120%;")
                            if 0 != repeat[count]:
                                ui.label(f"X {repeat[count]+1} TIMES").style("font-size: 110%")                            
                        with ui.card():
                            for g, v in saved_workouts[saved_workout_count[0]][k].items():
                                if v['ex_desc'] == "":
                                    continue
                                else:
                                    ui.label(f"{v['ex_desc']} x {v['dur']} minute(s)").style('font-size: 110%;')
    

def display_prev_workout():
    if saved_workout_count[0] < len(saved_workouts)-1:
        saved_workout_count[0] += 1
    else:
        ui.notify("This is the farthest recored workout")
    workout_display_column.refresh()

def display_next_workout():
    if saved_workout_count[0] > 0:
        saved_workout_count[0] -= 1
    else:
        ui.notify("This is the most recent workout on record")
    workout_display_column.refresh()


@ui.page('/main_screen')
def main_screen():
    ui.add_css('''
        .button_padding {
            padding: 0.25rem;
        }
    ''')

    ui.query('body').style(f'background-color: #ddeeff')

    with ui.row().classes("w-full").style("justify-content: space-between;"):
        with ui.column().style("justify-content: flex-start;"):
            with ui.card().classes("w-[250px] button_padding").style("text-align: center;"):
                ui.label("APPLICATIONS:").classes('w-full').style("font-size: 175%; font-weight: 400").tailwind.background_color('orange-200')
            with ui.card().classes('button_padding'):
                ui.button("TIMER", on_click=lambda: ui.navigate.to(f'/timer_app')).classes("w-[100px]")

        workout_display_column()

        with ui.card().style("background-color: rgb(226 232 240);"):
            ui.label("PAST WORKOUTS:").classes('w-full').style("font-size: 175%; font-weight: 400")
            with ui.scroll_area().classes("w-[400px] h-[500px]"):
                ui.button(f'PREV WORKOUT', on_click= lambda: display_prev_workout())
                ui.button(f'NEXT WORKOUT', on_click= lambda: display_next_workout())

''' 
took about 2 hours to create layout, design and figure out how to link page from login screen
'''


'''
Timer application screen
'''
num_exercises = [1]
''' auto populate workout dictionary for testing / demo purposes '''
# workout_dict = {"group1" : {'ex1' : {'ex_desc' : 'catcow exercise description',
#                                      'dur' : 1},
#                             'ex2' : {'ex_desc' : 'torso twists',
#                                      'dur' : 1}},
#                 "group2" : {'ex1' : {'ex_desc' : 'catcow exercise description - group2',
#                                      'dur' : 1},
#                             'ex2' : {'ex_desc' : 'torso twists - group2',
#                                      'dur' : 1}},
#                 "group3" : {'ex1' : {'ex_desc' : 'catcow exercise description - group3',
#                                      'dur' : 1},
#                             'ex2' : {'ex_desc' : 'torso twists - group3',
#                                      'dur' : 1}}
#                 }
workout_dict = {}

exercise_data = {}

ex_list = ["" for i in range(10)]
dur_list = [1 for i in range(10)]
repeat = []
# repeat = [0,1,0] # auto populate for testing / demo purposes
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
        if "" == ex:
            continue
        workout_dict[f'group{group_num}'].update({
            f"ex{count+1}" : {
                'ex_desc' : ex,
                'dur' : dur_list[count]
            }
    })
    second_column.refresh()
    third_column.refresh()
    for count, i in enumerate(ex_list):
        ex_list[count] = ""
    for count, d in enumerate(dur_list):
        dur_list[count] = 1  
    

def update_string(string, pos):
    ex_list[pos] = string
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
            
            #  easiest way to complete on first run, but has to be a better way...
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


def save_json_nav(w_dict):
    if not workout_dict:
        ui.notify('Please enter exercises')
    else:
        with open("JSONS\workout_dict.json", "w") as outfile:
            json.dump(w_dict, outfile, indent=2)
        with open("JSONS\\repeat_list.json", "w") as outfile:
            json.dump(repeat, outfile, indent=2)
        with open("JSONS\\rounds.json", "w") as outfile:
            json.dump(rounds, outfile, indent=2)
        
        ui.navigate.to(f'/workout_screen')

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
                    ui.button("Start", on_click=lambda: save_json_nav(workout_dict))

            second_column()                                                 # column 2
            third_column()                                                  # column 3

'''
10 hour work time -- at least 2-3 hours were spent going back and forth on how to capture user input to store in dictionary
'''

ui.run()
from nicegui import ui, run
from playsound import playsound
import json
from datetime import date, datetime
'''
WORKOUT SCREEN
'''

''' end sound path needs changed to machine specific file path  -- FULL PATH'''
end_sound_path = "audio_files\\end exercise.mp3"


group_count = [0]
min_elapsed = [0]

def get_exs(group, workout_dict):
   exs = [i for i in workout_dict[group].keys()] # list of stings -- ex1, ex2 etc.
   return exs

round_count = [1]
ex_count = [0]
TA = [False, False]
total_min = [0]
saved_switch = [0]

    
async def next_exercise(exercises, repeats_list, group_list, rounds, static_repeats_list):
    sound = await run.cpu_bound(playsound, end_sound_path)
    # if last exercise of group, if repeat is 0, iterate to next group
    if exercises[ex_count[0]] == exercises[-1]:
        if repeats_list[group_count[0]] != 0:
            repeats_list[group_count[0]] -= 1
            ex_count[0] = 0
            TA[0] = not TA[0]
            TA[1] = not TA[1]  
                    
        else:
            # if last group, end timer
            if group_list[group_count[0]] == group_list[-1]:
                # check if last round
                if rounds[0] != round_count[0]:
                    round_count[0] += 1
                    group_count[0] = 0
                    ex_count[0] = 0
                    for count,i in enumerate(static_repeats_list):
                        repeats_list[count] = i
                    TA[0] = not TA[0]
                    TA[1] = not TA[1]
                else:
                    TA[0] = False
                    TA[1] = True     
                    print("allll donnneeee")
            else:
                TA[0] = not TA[0]
                TA[1] = not TA[1]
                group_count[0] += 1
                ex_count[0] = 0 # reset exercise count
                
    else:
    # iterate to next exercise
        ex_count[0] += 1
        TA[0] = not TA[0]
        TA[1] = not TA[1]
    exercise_card.refresh() 



async def end_buffer():
    TA[0] = not TA[0]
    TA[1] = not TA[1]  
 
    workout_column_2.refresh()
    workout_column_3.refresh()
    workout_column_1.refresh()


def save_workout(workout_dict, static_repeats_list, rounds):
    if saved_switch[0] < 1:
        with open("Working_files\JSONS\saved_workouts.json", "r") as openfile:
            whole_d= json.load(openfile)

        today = date.today()
        today = today.strftime('%b-%d-%Y')
        time = datetime.now()
        time = time.strftime('%H:%M')
        to_save = workout_dict
        to_save.update({
            "other_info" : {
                "rounds" : rounds,
                "repeats_list" : static_repeats_list,
                "total_mins" : total_min,
                "date" : today,
                "time" : time
            }
        })
        whole_d.insert(0, to_save)

        with open("Working_files\JSONS\saved_workouts.json", "w") as outfile:
            json.dump(whole_d, outfile, indent=2)

        saved_switch[0] += 1
        exercise_card.refresh()


@ui.refreshable
def exercise_card(workout_dict, group_list, repeats_list, rounds, static_repeats_list):
    exercises = get_exs(group_list[group_count[0]], workout_dict)
    if TA[0]:
        ex_label =  ui.label(f"{workout_dict[group_list[group_count[0]]][exercises[ex_count[0]]]['ex_desc']}").classes("h-[150px]").style("font-size: 275%; text-align: center;")
        time_label = ui.label(f"{(int(workout_dict[group_list[group_count[0]]][exercises[ex_count[0]]]['dur'])*60)+1}").style("font-size: 700%;")
        min_elapsed[0] += workout_dict[group_list[group_count[0]]][exercises[ex_count[0]]]['dur']
        workout_top_row.refresh()
        timer = ui.timer(1.0, lambda: time_label.set_text((int(time_label.text)-1)) if int(time_label.text)!= 0 else next_exercise(exercises, repeats_list, group_list, rounds, static_repeats_list))
    elif not TA[1]:
        ex_label = ui.label(f"Next exercise starting in:")
        time_label = ui.label(5)
        timer = ui.timer(1.0, lambda: time_label.set_text((int(time_label.text)-1)) if int(time_label.text)!= 0 else end_buffer())
    elif not TA[0] and TA[1]:
        if saved_switch[0] < 1:
            with ui.column().classes("w-full").style("justify-content: center;"):
                ex_label = ui.label("WORKOUT").style("font-size: 700%;")
                ui.button("SAVE WORKOUT", on_click=lambda:save_workout(workout_dict, static_repeats_list, rounds)).classes("w-full")
                ui.label("COMPLETE").style("font-size: 700%;")
        else:
                with ui.column().classes("w-full").style("justify-content: center;"):
                    ex_label = ui.label("WORKOUT").style("font-size: 700%;")
                    ui.label("WORKOUT SAVED").classes("w-full").style("text-align: center;")
                    ui.label("COMPLETE").style("font-size: 700%;")            
    else:
        ex_label = ui.label(f"")

    return ex_label,exercises


@ui.refreshable
def workout_column_2(workout_dict, group_list, repeats_list, rounds, static_repeats_list):
    with ui.column().classes("w-[550px] h-full"):
        with ui.card().classes("w-full h-full").style("background-color: rgb(240 249 255); justify-content: center; align-items: center;"):    
            with ui.card().classes("w-full h-[800px]").style(" border-color: rgb(0 0 0);"):
                with ui.column().classes("w-full h-full").style("align-items: center;"):
                    ex_label = exercise_card(workout_dict, group_list, repeats_list, rounds, static_repeats_list)

            with ui.card().classes("w-[450px] h-full").style("border-color: rgb(0 0 0);"):
                switch = True
                with ui.card():
                    for g, v in workout_dict[group_list[group_count[0]]].items():
                        if switch == False:
                            ui.label(f"NEXT: {v['ex_desc']} x {v['dur']} minutes").style("font-size: 125%;")
                            switch = True                       
                        elif v['ex_desc'] == ex_label[0].text:
                            switch = False
                            ui.label(f"{v['ex_desc']} x {v['dur']} minutes")
                        else:
                            ui.label(f"{v['ex_desc']} x {v['dur']} minutes")  
                ui.label(f"Repeated {repeats_list[group_count[0]]} more times").style("text-align: center; font-size: 150%;")

@ui.refreshable                     
def workout_column_3(workout_dict, repeat, group_count):
    with ui.column().classes("w-[400px] h-full"):
        with ui.scroll_area().classes("w-full h-full"):
            with ui.card().classes("w-full h-full").style("	background-color: rgb(240 249 255); justify-content: center; align-items: center;"):
                ui.label("NEXT").style("font-size: 175%; font-weight: 500;")
                for count,k in enumerate(workout_dict.keys()):
                    if count <= group_count[0]:
                        continue
                    else:
                        with ui.card().classes("w-full").tight():
                            with ui.row().classes('w-full').style("justify-content: center;"):
                                ui.label(f"{k}").style("font-size: 120%;")
                                try:
                                    if 0 != repeat[count]:
                                        ui.label(f"X {repeat[count]+1} TIMES").style("font-size: 110%")                            
                                except IndexError:
                                    repeat.append(0)
                                    if 0 != repeat[count]:
                                        ui.label(f"X {repeat[count]+1} TIMES").style("font-size: 110%")
                            with ui.card():
                                for g, v in workout_dict[k].items():
                                    if v['ex_desc'] == "":
                                        continue
                                    else:
                                        ui.label(f"{v['ex_desc']} x {v['dur']} minute(s)").style('font-size: 110%;')

@ui.refreshable                         
def workout_column_1(workout_dict, repeat, group_count, static_repeats_list):
    with ui.column().classes("w-[400px] h-full"):
        with ui.scroll_area().classes("w-full h-full"):
            with ui.card().classes("w-full h-full").style("background-color: rgb(240 249 255); justify-content: center; align-items: center;"):
                ui.label("PREVIOUS").style("font-size: 175%; font-weight: 500;")
                for count,k in reversed(list(enumerate(workout_dict.keys()))):
                    if count < group_count[0]:
                        with ui.card().classes("w-full").tight():
                            with ui.row().classes('w-full').style("justify-content: center;"):
                                ui.label(f"{k}").style("font-size: 120%;")
                                if 0 != static_repeats_list[count]:
                                    ui.label(f"X {static_repeats_list[count]+1} TIMES").style("font-size: 110%")                            

                            with ui.card().classes(""):
                                for g, v in workout_dict[k].items():
                                    if v['ex_desc'] == "":
                                        continue
                                    else:
                                        ui.label(f"{v['ex_desc']} x {v['dur']} minute(s)").style('font-size: 110%;')
                    else:
                        continue
@ui.refreshable
def workout_top_row(rounds, total_min):
    with ui.row().classes("w-full h-[85px]"):
        with ui.card().classes("w-full h-full").style("background-color: rgb(240 249 255);"):
            with ui.row().classes('w-full').style('justify-content: space-between;'):
                with ui.column():
                    with ui.row().style("font-size: 200%"):
                        ui.label("Minutes Elapsed:")
                        ui.label(f"{min_elapsed[0]}")
                with ui.column():
                    with ui.row().style("font-size: 200%"):
                        ui.label("Round:")
                        ui.label(f"{round_count[0]} / {rounds[0]}")                         
                with ui.column():
                    with ui.row().style("justify-content: flex-end; font-size: 200%"):
                        ui.label(f"{total_min[0] - min_elapsed[0]}")
                        ui.label(":Minutes left")
                        
                    

@ui.page("/workout_screen")
def workout_screen():
    with open('JSONS\workout_dict.json', 'r') as openfile:
        workout_dict = json.load(openfile)
    with open('JSONS\\repeat_list.json', 'r') as openfile:
        repeats_list = json.load(openfile) 
    with open("JSONS\\rounds.json", "r") as openfile:
        rounds = json.load(openfile)

    static_repeats_list = repeats_list[:]

    group_list = [i for i in workout_dict.keys()] # list of strings -- group1, group2 etc.
    
    for count, key in enumerate(workout_dict.keys()):
        for k, v in workout_dict[key].items():
            total_min[0] += v['dur'] + (repeats_list[count] * v['dur'])
    total_min[0] *= rounds[0]

    ui.add_css('''
        .button_padding {
            padding: 0.25rem;
        }
    ''')    
    ui.query('body').style(f'background-color: #ddeeff')

    workout_top_row(rounds, total_min)

    with ui.row().classes("w-full h-[650px]").style("justify-content: center;"):

        workout_column_1(workout_dict, repeats_list, group_count, static_repeats_list)

        workout_column_2(workout_dict, group_list, repeats_list, rounds, static_repeats_list)
        
        workout_column_3(workout_dict, repeats_list, group_count)


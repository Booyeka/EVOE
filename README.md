# EVOE
Fitness inspired applications with record keeping


1: this application assists with time based workouts using a web based gui package: nicegui:

THINGS TO DO BEFORE RUNNING:
 -  In workout_page.py you will need to update the path of "end_sound_path" to your own specific full file path.

TO RUN:
 - run the file "main_file.py"

 How to navigate:
 - it will take you to a login page -- it is not functional at the moment but the login button will take you to the main page
 - once there, there will be a left column to navigate to the one timer application, middle column to display past workouts, and right column to navigate past workouts
 - the program is populated with two past workouts as examples to view past workouts

 - to start a new workout, click the "Timer" button in the left column
 - this will navigate to a screen to input data, groups of exercises, minutes, repeats of groups and rounds of exercises for circuit type formats -- the "add exercise" button doesnt do anything - it used to, but now doesnt
 - the right column will populate with previously added groups of exercises - there is no editting it, so double check info before commiting
 
 - once all info is entered, clicking the "start" button will navigate to the workout page
 - there will be a pause of 5 seconds before workout starts after clicking this button
 - the program will display current exercise and time remaining, next exercsises of the group will be found below that, as well previous and next groups of exercises will be found to the left and right respectfully
 - the program will notify you of the end of an exercise by playing a sound, so be sure your volume is up

 - once workout is complete, it will notify you with text and a button prompt to save workout, if clicked, the workout will append to workout history to be viewed on main page.

 - there is no exit condition, so just close the browser or terminal that is running python file.
 

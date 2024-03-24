import datetime
import json

now = datetime.datetime.now()

f_e = open('formula_e.json')
f_one = open('formula_one.json')

f_e_data = json.load(f_e)
f_one_data = json.load(f_one)

def get_fe():
    count_f_e = 0
    text = "No Upcoming Formula E Races This Week!"
    for data in f_e_data:
        if int(f_e_data[data]['start_date']) <= (now.day + 8)%31 + 1 and f_e_data[data]['month'] == now.strftime("%b") and int(f_e_data[data]['start_date']) == now.day: 
            round = data
            month = f_e_data[data]['month']
            day = f_e_data[data]['start_date']
            location = f_e_data[data]['location']
            text = f'🏎️ Formula E Alert! 🏁\n----\nReminder: {round} of the Formula E season is scheduled to start on {month} {day} in {location}.'
        count_f_e += 1
    return text

def get_fone():
    count_f_one = 0
    text =  "No Upcoming Formula 1 Races This Week!"
    for data in f_one_data:
        if int(f_one_data[data]['start_date']) <= (now.day + 8)%31 + 1 and f_one_data[data]['month'].split("-")[0] == now.strftime("%b"): 
            title = f_one_data[data]['event_title']
            start = f_one_data[data]['start_date']
            end = f_one_data[data]['end_date']
            month = f_one_data[data]['month']
            location = f_one_data[data]['location']
            text = f'🏎️ Formula 1 Alert! 🏁\n---\nReminder: {title} is scheduled for {start} to {end} {month} in {location}.'
        count_f_one += 1
    return text
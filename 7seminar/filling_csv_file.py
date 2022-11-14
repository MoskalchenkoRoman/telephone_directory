from ui import get_dict as get

dict = get()
def write_csv ():
    file = 'Phone_dictionary.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{dict[0]} {dict[1]} {dict[2]} {dict[3]} {dict[4]} {dict[5]}\n')
outside_colors=["Red","Green","Blue","Yellow"]

def player_choice(name,choices):
    player_has_chosen_ok = False

    while not player_has_chosen_ok:
        print()
        print("choose a "+ name + ":")
        for i in range(0,len(choices)):
            print(choices[i])

        choice = input(" ---> ")

        player_has_chosen_ok = (choice in choices)

        if not player_has_chosen_ok:

            print("Please choose something on the list")

    return choice

color_choice = player_choice("colour",outside_colors)

n_letter_in_color = len(color_choice)

if n_letter_in_color in [3,5]:
    first_number_choices = ["1","2","5","6"]
else:
    first_number_choices = ["3","4","7","8"]

first_number_chosen = player_choice("number",first_number_choices)

if n_letter_in_color in ["3","5"]:

    if first_number_chosen in ["1","5"]:
        second_number_choices = ["3","4","7","8"]
    else:
        second_number_choices = ["1","2","5","6"]

else:

    if first_number_chosen in ["3","7"]:
        second_number_choices = ["1","2","5","6"]
    else:
        second_number_choices = ["3","4","7","8"]




second_number_chosen = player_choice('number', second_number_choices)

fortune_number = int(second_number_chosen) - 1
print('fortune chosen:')
print(fortune_number)

fortunes = ['You will become very rich!',
            'You will fall into a big hole!',
            'You will find a worm in your next apple!',
            'You will lose your umbrella!',
            'You will dig up some treasure at the beach!',
            'You will turn into a newt!',
            'You will get no homework tomorrow!',
            'You will get eaten by a dragon!']

player_fortune = fortunes[fortune_number]

print()
print(player_fortune)
print()


import sys
import datetime
import random
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


list_of_greetings = [
    "buenos dias",
    "buenas",
    "Que tengas una excelente mañana"
]

list_of_names = [
    "mi amor! ❤️️",
    "mi corazon! 🫀",
    "mi pollacita! 🐤🐤❤️️",
    "mi flor! 🌹",
    "hermosa! 🌹",
    "bonita! 🌻",
    "conejita! 🐰🐰❤️️",
    "cabayita! 🐎🐎❤️️",
    "mi rayo de sol! ☀️ 🌅 ☀️"
]


def select_random_item_with_seed(seed_datetime, items_list):
    seed_timestamp = seed_datetime.timestamp()
    random.seed(seed_timestamp)
    
    selected_item = random.choice(items_list)
    return selected_item


def main():
    script_name = sys.argv[0]
    
    curr = str(datetime.datetime.now())
    seed = datetime.datetime.strptime(curr, "%Y-%m-%d %H:%M:%S.%f")

    greeting = select_random_item_with_seed(seed, list_of_greetings)
    name = select_random_item_with_seed(seed, list_of_names)


    print(greeting + ' ' + name)


if __name__ == "__main__":
    main()


import random
from collections import defaultdict
from prettytable import PrettyTable
import json

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.money = 1500
        self.properties = []
        self.houses = defaultdict(int)
        self.hotels = defaultdict(int)
        self.mortgaged_properties = []
        self.is_bankrupt = False
        self.in_jail = False
        self.jail_turns = 0
        self.consecutive_doubles = 0

    def mortgage(self, property_name):
        for property in self.properties:
            if property['name'] == property_name:
                mortgage_value = property['price'] // 2
                self.money += mortgage_value
                self.mortgaged_properties.append(property)
                self.properties.remove(property)
                property['mortgaged'] = True
                print(f"{self.name} mortgaged {property_name} for ${mortgage_value}")
                return
        print(f"{self.name} does not own {property_name}")

    def unmortgage(self, property_name):
        for property in self.mortgaged_properties:
            if property['name'] == property_name:
                unmortgage_value = property['price'] // 2
                if self.money >= unmortgage_value:
                    self.money -= unmortgage_value
                    self.mortgaged_properties.remove(property)
                    self.properties.append(property)
                    property['mortgaged'] = False
                    print(f"{self.name} unmortgaged {property_name} for ${unmortgage_value}")
                    return
        print(f"{self.name} does not have {property_name} mortgaged")

board = [
    {"square": 0, "name": "GO", "price": 0},
    {"square": 1, "name": "Mediterranean Avenue", "price": 60, "rent": [2, 10, 30, 90, 160, 250]},
    {"square": 2, "name": "Community Chest", "price": 0},
    {"square": 3, "name": "Baltic Avenue", "price": 60, "rent": [4, 20, 60, 180, 320, 450]},
    {"square": 4, "name": "Income Tax", "price": 0},
    {"square": 5, "name": "Reading Railroad", "price": 200, "rent": [25, 50, 100, 200]},
    {"square": 6, "name": "Oriental Avenue", "price": 100, "rent": [6, 30, 90, 270, 400, 550]},
    {"square": 7, "name": "Chance", "price": 0},
    {"square": 8, "name": "Vermont Avenue", "price": 100, "rent": [6, 30, 90, 270, 400, 550]},
    {"square": 9, "name": "Connecticut Avenue", "price": 120, "rent": [8, 40, 100, 300, 450, 600]},
    {"square": 10, "name": "Jail", "price": 0},
    {"square": 11, "name": "St. Charles Place", "price": 140, "rent": [10, 50, 150, 450, 625, 750]},
    {"square": 12, "name": "Electric Company", "price": 150, "rent": [4, 10]},
    {"square": 13, "name": "Virginia Avenue", "price": 160, "rent": [12, 60, 180, 500, 700, 900]},
    {"square": 14, "name": "Pennsylvania Railroad", "price": 200, "rent": [25, 50, 100, 200]},
    {"square": 15, "name": "St. James Place", "price": 180, "rent": [14, 70, 200, 550, 750, 950]},
    {"square": 16, "name": "Community Chest", "price": 0},
    {"square": 17, "name": "Tennessee Avenue", "price": 180, "rent": [14, 70, 200, 550, 750, 950]},
    {"square": 18, "name": "New York Avenue", "price": 200, "rent": [16, 80, 220, 600, 800, 1000]},
    {"square": 19, "name": "Free Parking", "price": 0},
    {"square": 20, "name": "Kentucky Avenue", "price": 220, "rent": [18, 90, 250, 700, 875, 1050]},
    {"square": 21, "name": "Chance", "price": 0},
    {"square": 22, "name": "Indiana Avenue", "price": 220, "rent": [18, 90, 250, 700, 875, 1050]},
    {"square": 23, "name": "Illinois Avenue", "price": 240, "rent": [20, 100, 300, 750, 925, 1100]},
    {"square": 24, "name": "B&O Railroad", "price": 200, "rent": [25, 50, 100, 200]},
    {"square": 25, "name": "Atlantic Avenue", "price": 260, "rent": [22, 110, 330, 800, 975, 1150]},
    {"square": 26, "name": "Ventnor Avenue", "price": 260, "rent": [22, 110, 330, 800, 975, 1150]},
    {"square": 27, "name": "Water Works", "price": 150, "rent": [4, 10]},
    {"square": 28, "name": "Marvin Gardens", "price": 280, "rent": [24, 120, 360, 850, 1025, 1200]},
    {"square": 29, "name": "Go to Jail", "price": 0},
    {"square": 30, "name": "Pacific Avenue", "price": 300, "rent": [26, 130, 390, 900, 1100, 1275]},
    {"square": 31, "name": "North Carolina Avenue", "price": 300, "rent": [26, 130, 390, 900, 1100, 1275]},
    {"square": 32, "name": "Community Chest", "price": 0},
    {"square": 33, "name": "Pennsylvania Avenue", "price": 320, "rent": [28, 150, 450, 1000, 1200, 1400]},
    {"square": 34, "name": "Short Line Railroad", "price": 200, "rent": [25, 50, 100, 200]},
    {"square": 35, "name": "Chance", "price": 0},
    {"square": 36, "name": "Park Place", "price": 350, "rent": [35, 175, 500, 1100, 1300, 1500]},
    {"square": 37, "name": "Luxury Tax", "price": 0},
    {"square": 38, "name": "Boardwalk", "price": 400, "rent": [50, 200, 600, 1400, 1700, 2000]}
]

chance_cards = [
    "Advance to GO",
    "Go to Jail",
    "Pay Poor Tax of $15",
    "Your building and loan matures. Collect $150",
    "You have won a crossword competition. Collect $100",
    "Bank pays you dividend of $50",
    "Get out of Jail Free",
    "Advance to Illinois Ave",
    "Advance to St. Charles Place",
    "Take a ride on the Reading Railroad",
    "Advance to Boardwalk",
    "Advance to the nearest Utility",
    "Advance to the nearest Railroad",
    "You are assessed for street repairs: $40 per house, $115 per hotel",
    "Pay each player $50",
    "Collect $150"
]

community_chest_cards = [
    "Advance to GO",
    "Bank error in your favor. Collect $200",
    "Doctor's fees. Pay $50",
    "From sale of stock you get $50",
    "Get out of Jail Free",
    "Go to Jail",
    "Grand Opera Night. Collect $50 from every player",
    "Holiday Fund matures. Receive $100",
    "Income tax refund. Collect $20",
    "It is your birthday. Collect $10 from each player",
    "Life insurance matures. Collect $100",
    "Pay hospital fees of $100",
    "Pay school fees of $150",
    "Receive $25 consultancy fee",
    "You are assessed for street repairs: $40 per house, $115 per hotel",
    "You have won second prize in a beauty contest. Collect $10",
    "You inherit $100"
]

def draw_card(deck):
    card = random.choice(deck)
    print(f"Card drawn: {card}")
    return card

def handle_card(player, card):
    if card == "Advance to GO":
        player.position = 0
        player.money += 200
    elif card == "Go to Jail":
        player.in_jail = True
        player.position = 10
    elif card == "Pay Poor Tax of $15":
        player.money -= 15
    elif card == "Your building and loan matures. Collect $150":
        player.money += 150
    elif card == "You have won a crossword competition. Collect $100":
        player.money += 100
    elif card == "Bank pays you dividend of $50":
        player.money += 50
    elif card == "Get out of Jail Free":
        player.get_out_of_jail_free = True
    # Add remaining card effects similarly...

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def move_player(player, steps):
    if player.in_jail:
        player.jail_turns += 1
        if player.jail_turns == 3:
            player.in_jail = False
            player.jail_turns = 0
            print(f"{player.name} is released from jail after 3 turns.")
        else:
            print(f"{player.name} is in jail and cannot move.")
        return

    dice1, dice2 = steps
    if dice1 == dice2:
        player.consecutive_doubles += 1
    else:
        player.consecutive_doubles = 0

    if player.consecutive_doubles == 3:
        print(f"{player.name} rolled doubles three times and is going to jail.")
        player.in_jail = True
        player.position = 10
        player.consecutive_doubles = 0
        return

    player.position = (player.position + dice1 + dice2) % len(board)
    current_square = board[player.position]
    print(f"{player.name} moved to square {current_square['square']}: {current_square['name']} (${current_square['price']})")

    if current_square['name'] == "Go to Jail":
        print(f"{player.name} landed on 'Go to Jail' and is going to jail.")
        player.in_jail = True
        player.position = 10
    elif current_square['name'] == "Chance":
        card = draw_card(chance_cards)
        handle_card(player, card)
    elif current_square['name'] == "Community Chest":
        card = draw_card(community_chest_cards)
        handle_card(player, card)
    elif current_square['name'] in player.properties:
        print(f"{player.name} owns this property and doesn't need to pay rent.")
    else:
        for owner in [p for p in [player1, player2] if current_square['name'] in p.properties]:
            rent = current_square['rent'][owner.houses[current_square['name']]]
            print(f"{player.name} pays ${rent} in rent to {owner.name}")
            player.money -= rent
            owner.money += rent

    print(f"Properties owned by {player.name}:")
    for property in player.properties:
        print(f"- {property}")

def buy_property(player, square):
    if square['price'] <= player.money:
        player.money -= square['price']
        player.properties.append(square['name'])
        print(f"{player.name} bought {square['name']} for ${square['price']}")
        print(f"{player.name} has cash at hand: ${player.money}")
    else:
        print(f"{player.name} does not have enough money to buy {square['name']}")

def buy_house(player, property_name):
    for square in board:
        if square['name'] == property_name:
            if property_name in player.properties and player.money >= square['rent'][player.houses[property_name] + 1]:
                player.money -= square['rent'][player.houses[property_name] + 1]
                player.houses[property_name] += 1
                print(f"{player.name} bought a house on {property_name} for ${square['rent'][player.houses[property_name]]}")
                print(f"{player.name} has cash at hand: ${player.money}")
                return
    print(f"{player.name} cannot buy a house on {property_name}")

def buy_hotel(player, property_name):
    for square in board:
        if square['name'] == property_name:
            if property_name in player.properties and player.money >= square['rent'][5] and player.houses[property_name] == 4:
                player.money -= square['rent'][5]
                player.houses[property_name] = 5
                player.hotels[property_name] = 1
                print(f"{player.name} bought a hotel on {property_name} for ${square['rent'][5]}")
                print(f"{player.name} has cash at hand: ${player.money}")
                return
    print(f"{player.name} cannot buy a hotel on {property_name}")

def save_game(player1, player2):
    game_state = {
        "player1": {
            "name": player1.name,
            "position": player1.position,
            "money": player1.money,
            "properties": player1.properties,
            "houses": dict(player1.houses),
            "hotels": dict(player1.hotels),
            "is_bankrupt": player1.is_bankrupt,
            "in_jail": player1.in_jail,
            "jail_turns": player1.jail_turns,
            "consecutive_doubles": player1.consecutive_doubles
        },
        "player2": {
            "name": player2.name,
            "position": player2.position,
            "money": player2.money,
            "properties": player2.properties,
            "houses": dict(player2.houses),
            "hotels": dict(player2.hotels),
            "is_bankrupt": player2.is_bankrupt,
            "in_jail": player2.in_jail,
            "jail_turns": player2.jail_turns,
            "consecutive_doubles": player2.consecutive_doubles
        }
    }
    with open("game_state.json", "w") as f:
        json.dump(game_state, f)
    print("Game state saved.")

def load_game():
    try:
        with open("game_state.json", "r") as f:
            game_state = json.load(f)
        player1 = Player(game_state["player1"]["name"])
        player1.position = game_state["player1"]["position"]
        player1.money = game_state["player1"]["money"]
        player1.properties = game_state["player1"]["properties"]
        player1.houses = defaultdict(int, game_state["player1"]["houses"])
        player1.hotels = defaultdict(int, game_state["player1"]["hotels"])
        player1.is_bankrupt = game_state["player1"]["is_bankrupt"]
        player1.in_jail = game_state["player1"]["in_jail"]
        player1.jail_turns = game_state["player1"]["jail_turns"]
        player1.consecutive_doubles = game_state["player1"]["consecutive_doubles"]

        player2 = Player(game_state["player2"]["name"])
        player2.position = game_state["player2"]["position"]
        player2.money = game_state["player2"]["money"]
        player2.properties = game_state["player2"]["properties"]
        player2.houses = defaultdict(int, game_state["player2"]["houses"])
        player2.hotels = defaultdict(int, game_state["player2"]["hotels"])
        player2.is_bankrupt = game_state["player2"]["is_bankrupt"]
        player2.in_jail = game_state["player2"]["in_jail"]
        player2.jail_turns = game_state["player2"]["jail_turns"]
        player2.consecutive_doubles = game_state["player2"]["consecutive_doubles"]

        print("Game state loaded.")
        return player1, player2
    except FileNotFoundError:
        print("No saved game found.")
        return None, None

def play_game():
    global player1, player2
    player1, player2 = load_game()
    if player1 is None or player2 is None:
        player1 = Player("Player 1")
        player2 = Player("Computer")

    current_player = player1

    while True:
        print(f"\n{current_player.name}'s turn.")
        input("Press Enter to roll the dice.\n")
        dice1, dice2 = roll_dice()
        print(f"You rolled a {dice1} and a {dice2}.")
        move_player(current_player, (dice1, dice2))

        current_square = board[current_player.position]
        if current_square['name'] not in current_player.properties and current_square['price'] > 0:
            buy_property(current_player, current_square)

        if current_player.name == "Player 1":
            while True:
                print("What would you like to do?")
                print("1. Buy a house")
                print("2. Buy a hotel")
                print("3. Mortgage a property")
                print("4. Unmortgage a property")
                print("5. Save and exit")
                print("6. End turn")
                choice = input("Enter your choice (1-6): ")
                if choice == "1":
                    for property in current_player.properties:
                        print(f"{property} ({current_player.houses[property]} houses)")
                    prop = input("Enter the property to buy a house: ")
                    buy_house(current_player, prop)
                elif choice == "2":
                    for property in current_player.properties:
                        if current_player.houses[property] == 4:
                            print(f"{property} (4 houses)")
                    prop = input("Enter the property to buy a hotel: ")
                    buy_hotel(current_player, prop)
                elif choice == "3":
                    for property in current_player.properties:
                        print(f"{property}")
                    prop = input("Enter the property to mortgage: ")
                    current_player.mortgage(prop)
                elif choice == "4":
                    for property in current_player.mortgaged_properties:
                        print(f"{property['name']}")
                    prop = input("Enter the property to unmortgage: ")
                    current_player.unmortgage(prop)
                elif choice == "5":
                    save_game(player1, player2)
                    return
                elif choice == "6":
                    current_player = player2
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            current_player = player1

        player_table = PrettyTable()
        player_table.field_names = ["Player", "Position", "Money", "Properties"]
        player_table.add_row(["\033[94mPlayer 1\033[0m", player1.position, f"\033[94m${player1.money}\033[0m", ", \n".join(player1.properties)])
        player_table.add_row(["\033[91mComputer\033[0m", player2.position, f"\033[91m${player2.money}\033[0m", ",\n ".join(player2.properties)])
        print("\nPlayer Information:")
        print(player_table)

if __name__ == "__main__":
    play_game()
import random

def main():
    def setup_player(): 
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        name = input ('Enter your name:')

        return {
            "name": name,
            "health": 10,
            "inventory": []
        } 
       
    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        return {
            "gold coin": random.randint(3, 12),
            "ruby": random.randint(3, 12),
            "ancient scroll": random.randint(3, 12),
            "emerald": random.randint(3, 12),
            "silver ring": random.randint(3, 12)
        }
      
    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Quit the game
        """
        print (f"You are in room {room_number}.")
        print ("What would you like to do?\n \
        1. Search for treasure\n \
        2. Move to next room\n \
        3. Check health and inventory\n \
        4. Quit the game")

    def search_room(player, treasures):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        outcome = random.choice(['treasure', 'trap'])
        if outcome == 'treasure':
            selected_treasure = random.choice(list(treasures.keys()))
            player["inventory"].append (selected_treasure)
            print (f"{selected_treasure} added to inventory")
        else:
            player["health"] -= 2
            print ("Warning! You lost 2 health points.")


    def check_status(player):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        print (f"Health: {player['health']}")

        if player["inventory"] != []:
            comma_separated_string = " , ".join(player["inventory"])
            print (comma_separated_string)
        else:
            print ("You have no items yet.")


    def end_game(player, treasures):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        total = 0
        for items_from_inventory in player["inventory"]:
            if items_from_inventory in treasures:
                total += treasures[items_from_inventory]

        print (f"final health: {player['health']},\n" \
               f"inventory contents: {player['inventory']},\n" \
               f"total score value: {total}")
        print ("Game Over! Thanks for playing.")
      
    def run_game_loop(player, treasures):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        for room_number in range(1, 6):
            in_play = True
            while in_play:
                display_options(room_number)
                action_input = input ()
                if action_input == "1":
                    search_room(player, treasures)
                elif action_input == "2":
                    break
                elif action_input == "3":
                    check_status(player)
                    if player["health"] < 1:
                        in_play = False 
                elif action_input == "4":
                    in_play = False
            else:
                break
        end_game(player, treasures)

    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    run_game_loop(player, treasures)

if __name__ == "__main__":
    main()

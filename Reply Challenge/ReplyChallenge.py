def get_data(data):
    with open(data + ".txt", "r") as f:
        contents = f.readline().split(' ')
        return contents

class Game():
    def __init__(self, stamina, max_stamina, turns):
        self.stamina = int(stamina)
        self.max_stamina = int(max_stamina)
        self.turns = int(turns)

        self.remaining_turns = self.turns
        self.accumulated = 0
        self.reward_per_turn = 0

        self.enemies = []
        self.available_demon = []
        self.attacked_demon = []
        self.cannot_be_attacked = []

        self.ordered_attack_demon = []

    def get_enemy(self, data):
        with open(data + ".txt", "r") as f:
            f.readline()

            i = 0
            for line in f:
                data = [int(str(elem).strip()) for elem in line.split(' ') if str(elem).strip()]
                self.enemies.append(
                    {
                       'id': i,
                       'consume':  int(data[0]),
                       'turns': int(data[1]),
                       'recover': int(data[2]),
                       'total_fragment': int(data[3]),
                       'gained_fragment': list(map(int, data[4 : self.turns + 4])),
                       'remaining_recover_turns': int(data[1]),
                       'remaining_turns': self.turns
                    }
                )

                i = i + 1

    def available_demon_to_attack(self):
        for enemy in self.enemies:
            if enemy['consume'] <= self.stamina:
                if(enemy['id'] not in self.cannot_be_attacked):
                    self.available_demon.append(enemy)

        return self.available_demon

    def choose_which_demon_to_attack(self):
        selected_demon = 0

        if(len(self.available_demon) > 0):
            max_enemy_fragment = max(self.available_demon, key=lambda x: x['gained_fragment'])['id']
            min_enemy_consume = min(self.available_demon, key=lambda x: x['consume'])['id']

            if max_enemy_fragment == min_enemy_consume:
                selected_demon = min_enemy_consume
            else:
                selected_demon = max_enemy_fragment

            self.ordered_attack_demon.append(selected_demon)

            for enemy in self.available_demon:
                if enemy['id'] == selected_demon:
                    self.attacked_demon.append(
                        enemy
                    )

                    self.stamina -= enemy['consume']
                    self.cannot_be_attacked.append(enemy['id'])
                    break
            
            self.available_demon = []

        return self.attacked_demon

    def scoring(self):
        reward = 0

        if(self.remaining_turns > 0):
            for demon in self.attacked_demon:
                demon['remaining_recover_turns'] -= 1
                
                if(demon['remaining_recover_turns'] == 0):
                    if self.stamina + demon['recover'] < self.max_stamina:
                        self.stamina += demon['recover']
                    else :
                        self.stamina = self.max_stamina
                    
                if self.turns - demon['remaining_turns'] < len(demon['gained_fragment']):
                    self.accumulated += demon['gained_fragment'][self.turns - demon['remaining_turns']]

                demon['remaining_turns'] -= 1

        # print("Stamina ", self.stamina)
        # print(self.attacked_demon)
        # print()
                
        self.remaining_turns -= 1
        self.accumulated += reward
    
    def play(self):
        for _ in range(self.turns):
            self.available_demon_to_attack()
            self.choose_which_demon_to_attack()
            self.scoring()

        for enemy in self.enemies:
            if(enemy['id'] not in self.cannot_be_attacked):
                print(enemy['id'])
                self.ordered_attack_demon.append(enemy['id'])
                
        print(self.accumulated)

        with open('output.txt', 'w') as f:
            for enemy in self.ordered_attack_demon:
                f.write(str(enemy) + "\n")

data = get_data("data")
game = Game(data[0], data[1], data[2])
game.get_enemy("data")

game.play()
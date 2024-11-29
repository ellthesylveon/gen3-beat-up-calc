import math as mt
import random

def main() -> None :
	print("")

def damage_calc(defe):
	global damage_list
	global total_damage
	damage_list = []
	for i in range(6) :
		atk = party_list[i]
		damage = mt.floor((mt.floor(((42 * 10 * mt.floor(atk / defe))) / 50) + 2) * (random.randint(85, 100)/100))
		damage_list.append(damage)
	total_damage = sum(damage_list)

def get_user_input():
	global party_list
	party_list = []
	defe = input("Enter opponent's base defense (leave blank for default): ")
	if defe == "":
		defe = 10
	int(defe)
	hp = input("Enter opponent's HP (leave blank for default): ")
	if hp == "":
		hp = 651
	int(hp)
	for i in range(6):
		party_atk = int(input(f"Enter the base attack of pokemon number {i+1} in your party: "))
		party_list.append(party_atk)
	global opponent
	opponent=Opponent(defe=defe,hp=hp)
	return opponent, party_list


#class User:
#	def __init__(self, atk):
#		self.atk = atk

class Opponent:
	def __init__(self, defe, hp):
		self.defe = defe
		self.hp = hp

if __name__ == "__main__": 
	get_user_input()
	damage_calc(opponent.defe)
	print(f"Possible damage amounts: {damage_list}")
	print(f"{opponent.hp} - {total_damage} = {opponent.hp - total_damage}")
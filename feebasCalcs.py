"""
feebasCalcs.py

This file serves as the starting point for the Finding Feebas application. 
It initialises the interface and has functions for all interactions, like moving the map,
pressing buttons and checking the input on the entry boxes.
"""

from tkinter import ttk
from tkinter import *

from trendyPhrase import group_conditions, group_lifestyles, group_hobbies, DewfordTrend
from feebasCoordinates import FEEBAS_BRIDGE_TILES, FEEBAS_COORDINATES_ORIGINAL, FEEBAS_COORDINATES_NEW

DEBUG_ENABLED = False

class FeebasCalculator:
    """
    This class calculates the exact spots of where Feebas is located based on the Trainer ID, the Lottery Number and the Trendy Phrase.
    This class can only find Feebas if a new game has started without a working battery. 
    """
    def __init__(self, trainer_id, lottery_number, trendy_phrase_1, trendy_phrase_2, is_emerald, is_fixed_game):
        """
        This function initialises AND calculates the Feebas spots based on the parameters given.

        Args:
            self: The class itself
            trainer_id: The Trainer ID of the player 
            lottery_number: The Lottery Number found in Lilicove City
            trendy_phrase_1: The first word of the Trendy Phrase found in Dewford Town
            trendy_phrase_2: The second word of the Trendy Phrase found in Dewford Town
            is_emerald: A boolean indicating if these values are from Ruby/Sapphire (False) or Emerald (True)
        """
        
        self.is_feebas_found = False 
        self.feebas_seed = 0
        
        # Checks to make sure the values given are correct
        if not((trendy_phrase_1 in group_conditions) and ((trendy_phrase_2 in group_lifestyles) or (trendy_phrase_2 in group_hobbies))):
            return
        if(trainer_id == '' or lottery_number == ''):
            return
            
        # Initialises the values of the Feebas calculator
        self.trainer_id = int(trainer_id)
        self.secret_ids = []
        self.lottery_number = int(lottery_number)
        self.trendy_phrase_1 = trendy_phrase_1
        self.trendy_phrase_2 = trendy_phrase_2
        self.starting_seeds = []
        self.calculated_feebas_spots = []

        # Initialise the RNG based on which game is used for the calculator
        if(is_emerald == False):
            self.seedRng(0x5A0)
        else:
            self.seedRng(self.trainer_id)

        # Find the RNG starting point for the Feebas calculation
        self.findFeebasStartingPoint()
        
        # Calculate the Trendy Phrase 
        for seed in self.starting_seeds:
            if(is_emerald == False):
                self.findTrendyPhraseRubySapphire(seed)
            else:
                self.findTrendyPhraseEmerald(seed)
            
            if(self.is_feebas_found == True):
                break

        # Return if no Feebas seed was found
        if(self.is_feebas_found == False):
            return
         
        # Seed the RNG with the value found for the Trendy Phrase
        self.seedRng(self.feebas_seed)

        # Calculate the actual Feebas spots
        x = 0
        add_bridge_tiles = False
        while(x != 6):
            feebas_id = self.getFeebasRandomValue() % 447
            if(feebas_id == 0):
                feebas_id = 447
            if((is_fixed_game == False and feebas_id >= 4)):    
                self.calculated_feebas_spots.append(FEEBAS_COORDINATES_ORIGINAL[feebas_id])
                x += 1
                if(feebas_id == 132):
                    add_bridge_tiles = True
            elif(is_fixed_game == TRUE):
                self.calculated_feebas_spots.append(FEEBAS_COORDINATES_NEW[feebas_id])
                x += 1
        if(add_bridge_tiles == True):
            for tile in FEEBAS_BRIDGE_TILES:
                self.calculated_feebas_spots.append(tile)
                
    def isFeebasFound(self):
        """
        This function indicates if the class has found the Feebas spots or not

        Args:
            self: The class itself
        Returns:
            self.is_feebas_found: A boolean indicating if the class has found the Feebas spots
        """
        return self.is_feebas_found
    
    def getSecretIds(self):
        return self.secret_ids

    def getFeebasSpotCoordinates(self):
        """
        This function returns the calculated Feebas spots 

        Args:
            self: The class itself
        Returns:
            self.calculated_feebas_spots: An array containing the 6 Feebas spot coordinates
        """
        return self.calculated_feebas_spots
    
    def seedRng(self, seed):
        """
        This function seeds the local RNG function with any 32 bit seed

        Args:
            self: The class itself
            seed: A 32 bit value containing the seed for the RNG
        """
        self.random_value = seed & 0xFFFFFFFF
    
    def getFeebasRandomValue(self):
        """
        This function progresses the RNG once and returns the newly generated value for the Feebas RNG

        Args:
            self: The class itself
        Returns:
            self.random_value: The upper 16 bits of the randomly generated value.
        """
        self.random_value = 0x41C64E6D * self.random_value + 0x00003039
        self.random_value &= 0xFFFFFFFF
        return (self.random_value >> 16)    
    
    def getRandomValue(self):
        """
        This function progresses the RNG once and returns the newly generated value for the Regular RNG

        Args:
            self: The class itself
        Returns:
            self.random_value: The upper 16 bits of the randomly generated value.
        """
        self.random_value = 0x41C64E6D * self.random_value + 0x00006073
        self.random_value &= 0xFFFFFFFF
        return (self.random_value >> 16)

    def getPreviousRandomValue(self):
        """
        This function calculates the previous RNG value and returns it

        Args:
            self: The class itself
        Returns:
            self.random_value: The upper 16 bits of the previous random value.
        """
        self.random_value = 0xEEB9EB65 * self.random_value + 0x0A3561A1;
        self.random_value &= 0xFFFFFFFF
        return (self.random_value >> 16)
        
    def findFeebasStartingPoint(self):
        """
        This function finds the starting point for the Trendy Phrase calculation based on the Lottory Number. It does this by progressing the RNG
        20000 frames (around 5,5 minutes) forward and saves all moments the RNG generated the given Lottory Number in an array.

        Args:
            self: The class itself
        """
        
        self.starting_seeds = []
        for x in range(20000):
            random_value = self.getRandomValue()
            if(random_value == self.lottery_number):
                self.starting_seeds.append(self.random_value)
                        
    def findTrendyPhraseRubySapphire(self, lottery_seed):
        """
        This function generates the dewford phrases for Ruby and Sapphire based on the lottory seed that was found before. It first find the starting 
        point using the Trainer ID. Afterwards the Dewford Phrases are generated. If the last RNG call made ends with the Lottory Number and the Trendiest 
        Phrase matches, then Feebas is found successfully!

        Args:
            self: The class itself
            lottery_seed: The seed of the RNG which generated the Lottory Number
        """
        lottery_no = 0
        final_trendy_prase = ["NO", "FEEBAS"]
        
        # Seed the RNG and regress backwards a total of 50 RNG calls maximum or until the Trainer ID is found.
        self.seedRng(lottery_seed)
        for x in range(50):
            prev_rng_value = self.getPreviousRandomValue()
            if(prev_rng_value == self.trainer_id):
                break
            # Nothing is found, return back
            if(x == 50):
                return
        # Trainer ID is found! Time to calculate the rest of the values
        # First we do one more step backwards for the Secret ID
        temp_secret_id = self.getPreviousRandomValue()
        
        # 3 RNG calls before the dewford phrases
        self.getRandomValue()
        self.getRandomValue()
        self.getRandomValue()

        # Generate the 5 dewford phrases
        self.generateDewfordPhrases()
        final_trendy_prase = self.dewford_trends[0].getPhrase()
        
        # Generate the lottory number
        lottery_no = self.getRandomValue()
        
        # Check all the values. If it all matches, then Feebas is found!!
        if((self.lottery_number == lottery_no) and (final_trendy_prase[0] == self.trendy_phrase_1 and final_trendy_prase[1] == self.trendy_phrase_2)):
            if(DEBUG_ENABLED == True):
                print("FOUND!!!!!")
                print("Secret ID:" + str(temp_secret_id))
                print("Feebas Seed:" + str(self.dewford_trends[0].getRandomValue()))
            self.secret_ids.append(temp_secret_id)
            self.is_feebas_found = True
            self.feebas_seed = self.dewford_trends[0].getRandomValue()

    def findTrendyPhraseEmerald(self, lottery_seed):
        """
        This function generates the dewford phrases for Ruby and Sapphire based on the lottory seed that was found before. Emerald doesn't have a clear
        starting point, so we need to regress a variable amount of time until we Trendy Phrase and the Lottory ID matches up. If this happens, then we have
        found Feebas successfully! It also tries to find the Secret ID, but it is possible however to find more than one Secret ID...

        Args:
            self: The class itself
            lottery_seed: The seed of the RNG which generated the Lottory Number
        """

        reverse_steps = 50
        lottery_no = 0
        final_trendy_prase = ["NO", "FEEBAS"]
        
        for steps in range(20):
            self.seedRng(lottery_seed)
            for x in range(reverse_steps - steps):
                self.getPreviousRandomValue()
                
            # First the Secret ID is generated
            temp_secret_id = self.getRandomValue()

            # 3 RNG calls before the dewford phrases
            self.getRandomValue()
            self.getRandomValue()
            self.getRandomValue()

            # Generate the 5 dewford phrases
            self.generateDewfordPhrases()
            final_trendy_prase = self.dewford_trends[0].getPhrase()

            # Generate the lottory number
            lottery_no = self.getRandomValue()
                
            # Check all the values. If it all matches, then Feebas is found!!
            if((self.lottery_number == lottery_no) and (final_trendy_prase[0] == self.trendy_phrase_1 and final_trendy_prase[1] == self.trendy_phrase_2)):
                if(DEBUG_ENABLED == True):
                    print("FOUND!!!!!")
                    print("Secret ID:" + str(temp_secret_id))
                    print("Feebas Seed:" + str(self.dewford_trends[0].getRandomValue()))
                    print("Reverse Steps:" + str(reverse_steps - steps))
                self.secret_ids.append(temp_secret_id)
                self.is_feebas_found = True
                self.feebas_seed = self.dewford_trends[0].getRandomValue()
        
        
    def generateDewfordPhrases(self):
        """
        This function generates 5 Dewford Phrases and sorts them based on their Trendiness. 
        This is a direct copy of how the game does it as well.
        
        Args:
            self: The class itself
        """
        
        self.dewford_trends = []
        for x in range(5):
            new_trend = DewfordTrend()
            
            # Generate the phrase
            phrase_1 = group_conditions[self.getRandomValue() % len(group_conditions)]
            if(self.getRandomValue() & 1 == 1):
                phrase_2 = group_lifestyles[self.getRandomValue() % len(group_lifestyles)]
            else:
                phrase_2 = group_hobbies[self.getRandomValue() % len(group_hobbies)]
            new_trend.setPhrase(phrase_1, phrase_2)
            
            # Generate the Trendiness values and the Random value
            new_trend.setIsGainingTrendiness(self.getRandomValue() & 1)

            rando = self.getRandomValue() % 98
            if (rando > 50):
                rando = self.getRandomValue() % 98
                if (rando > 80):
                    rando = self.getRandomValue() % 98
            
            new_trend.setMaxTrendiness(rando + 30)
            new_trend.setTrendiness((self.getRandomValue() % (rando + 1)) + 30)
            new_trend.setRandomValue(self.getRandomValue())
            
            self.dewford_trends.append(new_trend)
            
        # Sort the trends based on their Trendiness values
        self.sortTrends()
        
    def sortTrends(self):
        """
        This function sorts the 5 Dewford Phrases based on their Trendiness values
        This is a direct copy of how the game does it as well.
        
        Args:
            self: The class itself
        """
        for x in range(5):
            y = x + 1
            while(y < 5):
                if(self.compareTrends(y, x)):
                    self.SWAP(self.dewford_trends, y, x)
                y += 1
            
    def compareTrends(self, a, b):
        """
        This function compares two trends in order to see which one has a higher Trendiness value.
        This is a direct copy of how the game does it as well.
        
        Args:
            self: The class itself
            a: A dewford trend index
            b: A dewford trend index
        """
        if(self.dewford_trends[a].getTrendiness() > self.dewford_trends[b].getTrendiness()):
            return True
        if(self.dewford_trends[a].getTrendiness() < self.dewford_trends[b].getTrendiness()):
            return False
        if(self.dewford_trends[a].getMaxTrendiness() > self.dewford_trends[b].getMaxTrendiness()):
            return True
        if(self.dewford_trends[a].getMaxTrendiness() < self.dewford_trends[b].getMaxTrendiness()):
            return False
            
        return (self.getRandomValue() & 1)

    def SWAP(self, dewford_list, pos1, pos2):
        """
        This function swaps two trends with each other in the dewford_list
        This is a direct copy of how the game does it as well.
        
        Args:
            self: The class itself
            dewford_list: The 5 dewford trends in a list
            pos1: Index of a Dewford trend that is to be swapped with pos2
            pos2: Index of a Dewford trend that is to be swapped with pos1
        """
        dewford_list[pos1], dewford_list[pos2] = dewford_list[pos2], dewford_list[pos1]
        return dewford_list

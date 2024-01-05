from tkinter import ttk
from tkinter import *

from trendyPhrase import group_conditions, group_lifestyles, group_hobbies, DewfordTrend
from feebasCoordinates import FEEBAS_COORDINATES

class FeebasCalculator:
    def __init__(self, trainer_id, lottery_number, trendy_phrase_1, trendy_phrase_2, is_rs):	
        self.is_feebas_found = False 
        if not((trendy_phrase_1 in group_conditions) and ((trendy_phrase_2 in group_lifestyles) or (trendy_phrase_2 in group_hobbies))):
            return
        if(trainer_id == '' or lottery_number == ''):
            return
        self.trainer_id = int(trainer_id)
        self.secret_id = 0
        self.lottery_number = int(lottery_number)
        self.trendy_phrase_1 = trendy_phrase_1
        self.trendy_phrase_2 = trendy_phrase_2
        self.starting_seeds = []
        self.calculated_feebas_spots = []
        self.rng_counter = 0
        self.vblank = 0xFFFFFFFF
        
        if(is_rs):
            self.seedRng(0x5A0)
        else:
            self.seedRng(self.trainer_id)
            
        self.findFeebasStartingPoint()
        for x in self.starting_seeds:
            self.findFeebasSpotsEmerald(x)
            if(self.is_feebas_found == True):
                break
        if(self.is_feebas_found == False):
            print("FUCK")
            return
        
        self.seedRng(self.dewford_trends[0].getRandomValue())
        
        x = 0
        while(x != 6):
            feebas_id = self.getFeebasRandomValue() % 447
            if(feebas_id == 0):
                feebas_id = 447
            if(feebas_id >= 4):
                self.calculated_feebas_spots.append(FEEBAS_COORDINATES[feebas_id])
                x += 1
                
        return
        
    def isFeebasFound(self):
        return self.is_feebas_found

    def getFeebasSpotCoordinates(self):
        return self.calculated_feebas_spots
        #return FEEBAS_COORDINATES
        
    def seedRng(self, seed):
        self.random_value = seed & 0xFFFFFFFF
        
    def getFeebasRandomValue(self):
        self.random_value = 0x41C64E6D * self.random_value + 0x00003039
        self.random_value &= 0xFFFFFFFF
        return (self.random_value >> 16)		
        
    def getRandomValue(self):
        self.random_value = 0x41C64E6D * self.random_value + 0x00006073
        self.random_value &= 0xFFFFFFFF
        self.rng_counter += 1
        if(self.vblank == self.rng_counter):
            self.random_value = 0x41C64E6D * self.random_value + 0x00006073
            self.random_value &= 0xFFFFFFFF
            self.rng_counter += 1
            print(self.vblank)
        return (self.random_value >> 16)

    def getPreviousRandomValue(self):
        self.random_value = 0xEEB9EB65 * self.random_value + 0x0A3561A1;
        self.random_value &= 0xFFFFFFFF
        return (self.random_value >> 16)
        
    def findFeebasStartingPoint(self):
        self.starting_seeds = []
        for x in range(20000):
            random_value = self.getRandomValue()
            if(random_value == self.lottery_number):
                self.starting_seeds.append(self.random_value)
                print(self.starting_seeds)
                        
    def findFeebasSpotsRubySapphire(self, lottery_seed):
        self.seedRng(lottery_seed)
        self.rng_counter = 0
        for x in range(50):
            self.getPreviousRandomValue()
           # if((self.random_value >> 16) == self.trainer_id)
    def findFeebasSpotsEmerald(self, lottery_seed):
        reverse_steps = 50
        lottery_no = 0
        final_trendy_prase = ["NO", "FEEBAS"]
        while((self.lottery_number != lottery_no) or (final_trendy_prase[0] != self.trendy_phrase_1 or final_trendy_prase[1] != self.trendy_phrase_2)):
            self.seedRng(lottery_seed)
            #print(lottery_seed)
            self.rng_counter = 0
            for x in range(reverse_steps):
                self.getPreviousRandomValue()
            self.generateDewfordPhrases()
            
            final_trendy_prase = self.dewford_trends[0].getPhrase()

            lottery_no = self.getRandomValue()
            
            reverse_steps -= 1
            if(reverse_steps < 30):
                print("UGH")
                return
        print("FOUND!!!!!")
        print(self.dewford_trends[0].getRandomValue())
        self.is_feebas_found = True
        
    def generateDewfordPhrases(self):
        self.dewford_trends = []
        for x in range(5):
            new_trend = DewfordTrend()
            phrase_1 = group_conditions[self.getRandomValue() % len(group_conditions)]
            if(self.getRandomValue() & 1 == 1):
                phrase_2 = group_lifestyles[self.getRandomValue() % len(group_lifestyles)]
            else:
                phrase_2 = group_hobbies[self.getRandomValue() % len(group_hobbies)]
            new_trend.setPhrase(phrase_1, phrase_2)
            #print(phrase_1)
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
        self.sortTrends()

        
    def sortTrends(self):
        for x in range(5):
            y = x + 1
            while(y < 5):
                if(self.compareTrends(y, x)):
                    self.SWAP(self.dewford_trends, y, x)
                y += 1
            
    def compareTrends(self, a, b):
        if(self.dewford_trends[a].getTrendiness() > self.dewford_trends[b].getTrendiness()):
            return True
        if(self.dewford_trends[a].getTrendiness() < self.dewford_trends[b].getTrendiness()):
            return False
        if(self.dewford_trends[a].getMaxTrendiness() > self.dewford_trends[b].getMaxTrendiness()):
            return True
        if(self.dewford_trends[a].getMaxTrendiness() < self.dewford_trends[b].getMaxTrendiness()):
            return False
            
        return (self.getRandomValue() & 1)

    def SWAP(self, list, pos1, pos2):
        list[pos1], list[pos2] = list[pos2], list[pos1]
        return list

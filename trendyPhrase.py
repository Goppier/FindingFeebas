"""
trendyPhrase.py

This file contains all the possible words used in the Trendy Phrase and also has a class that contains all the parameters of the Dewford Trend.
"""

class DewfordTrend:
    """
    This class holds the parameters of each Trendy Phrase used in Dewford
    """
    def __init__(self):
        """
        This function initialises the Trendy Phrase parameters

        Args:
            self: The class itself
        """
        self.trendiness = 0
        self.max_trendiness = 0
        self.is_gaining_trendiness = False
        self.random_value = 0
        self.easy_chat_words = ["", ""]
    
    def setTrendiness(self, trendiness):
        """
        This function sets the trendiness value for this Trendy Phrase

        Args:
            self: The class itself
            trendiness: The value of the phrase's trendiness
        """
        self.trendiness = trendiness
    
    def getTrendiness(self):
        """
        This function returns the trendiness value for this Trendy Phrase

        Args:
            self: The class itself
            
        Returns:
            self.trendiness: The trendiness value in the form on an integer
        """
        return self.trendiness
    
    def setMaxTrendiness(self, max_trendiness):
        """
        This function sets the maximum trendiness value for this Trendy Phrase

        Args:
            self: The class itself
            max_trendiness: The value of the phrase's maximum trendiness
        """
        self.max_trendiness = max_trendiness
    
    def getMaxTrendiness(self):
        """
        This function returns the maximum trendiness value for this Trendy Phrase

        Args:
            self: The class itself
            
        Returns:
            self.max_trendiness: The maximum trendiness value in the form on an integer
        """
        return self.max_trendiness
        
    def setIsGainingTrendiness(self, is_gaining_trendiness):
        """
        This function sets the is_gaining_trendiness value

        Args:
            self: The class itself
            is_gaining_trendiness: A boolean value that decides if the phrase is gaining trendiness or not
        """
        self.is_gaining_trendiness = is_gaining_trendiness
    
    def getIsGainingTrendiness(self):
        """
        This function returns the is_gaining_trendiness for this Trendy Phrase

        Args:
            self: The class itself
            
        Returns:
            self.is_gaining_trendiness: A boolean value that decides if the phrase is gaining trendiness or not
        """
        return self.is_gaining_trendiness
        
    def setRandomValue(self, random_value):
        """
        This function sets the random value for this Trendy Phrase

        Args:
            self: The class itself
            random_value: The random value of this Trendy Phrase
        """
        self.random_value = random_value
    
    def getRandomValue(self):
        """
        This function returns the random value for this Trendy Phrase

        Args:
            self: The class itself
            
        Returns:
            self.random_value: The random value in the form on an integer
        """
        return self.random_value
        
    def setPhrase(self, easy_chat_word_1, easy_chat_word_2):
        """
        This function sets the Trendy Phrase using two Easy Chat words

        Args:
            self: The class itself
            easy_chat_word_1: The first word of the Trendy Phrase
            easy_chat_word_2: The second word of the Trendy Phrase
        """
        self.easy_chat_words[0] = easy_chat_word_1
        self.easy_chat_words[1] = easy_chat_word_2
    
    def getPhrase(self):
        """
        This function returns the Easy Chat words for this Trendy Phrase

        Args:
            self: The class itself
            
        Returns:
            self.easy_chat_words: The Easy Chat words for this Trendy Phrase
        """
        return self.easy_chat_words


"""
This list holds all the Easy Chat words for the category "Conditions"
"""
group_conditions=[
    "HOT",
    "EXISTS",
    "EXCESS",
    "APPROVED",
    "HAS",
    "GOOD",
    "LESS",
    "MOMENTUM",
    "GOING",
    "WEIRD",
    "BUSY",
    "TOGETHER",
    "FULL",
    "ABSENT",
    "BEING",
    "NEED",
    "TASTY",
    "SKILLED",
    "NOISY",
    "BIG",
    "LATE",
    "CLOSE",
    "DOCILE",
    "AMUSING",
    "ENTERTAINING",
    "PERFECTION",
    "PRETTY",
    "HEALTHY",
    "EXCELLENT",
    "UPSIDEDOWN",
    "COLD",
    "REFRESHING",
    "UNAVOIDABLE",
    "MUCH",
    "OVERWHELMING",
    "FABULOUS",
    "ELSE",
    "EXPENSIVE",
    "CORRECT",
    "IMPOSSIBLE",
    "SMALL",
    "DIFFERENT",
    "TIRED",
    "SKILL",
    "TOP",
    "NONSTOP",
    "PREPOSTEROUS",
    "NONE",
    "NOTHING",
    "NATURAL",
    "BECOMES",
    "LUKEWARM",
    "FAST",
    "LOW",
    "AWFUL",
    "ALONE",
    "BORED",
    "SECRET",
    "MYSTERY",
    "LACKS",
    "BEST",
    "LOUSY",
    "MISTAKE",
    "KIND",
    "WELL",
    "WEAKENED",
    "SIMPLE",
    "SEEMS",
    "BADLY"
]

"""
This list holds all the Easy Chat words for the category "Lifestyles"
"""
group_lifestyles=[
    "CHORES",
    "HOME",
    "MONEY",
    "ALLOWANCE",
    "BATH",
    "CONVERSATION",
    "SCHOOL",
    "COMMEMORATE",
    "HABIT",
    "GROUP",
    "WORD",
    "STORE",
    "SERVICE",
    "WORK",
    "SYSTEM",
    "TRAIN",
    "CLASS",
    "LESSONS",
    "INFORMATION",
    "LIVING",
    "TEACHER",
    "TOURNAMENT",
    "LETTER",
    "EVENT",
    "DIGITAL",
    "TEST",
    "DEPT_STORE",
    "TELEVISION",
    "PHONE",
    "ITEM",
    "NAME",
    "NEWS",
    "POPULAR",
    "PARTY",
    "STUDY",
    "MACHINE",
    "MAIL",
    "MESSAGE",
    "PROMISE",
    "DREAM",
    "KINDERGARTEN",
    "LIFE",
    "RADIO",
    "RENTAL",
    "WORLD"
]

"""
This list holds all the Easy Chat words for the category "Hobbies"
"""
group_hobbies=[
    "IDOL",
    "ANIME",
    "SONG",
    "MOVIE",
    "SWEETS",
    "CHAT",
    "CHILD_S_PLAY",
    "TOYS",
    "MUSIC",
    "CARDS",
    "SHOPPING",
    "CAMERA",
    "VIEWING",
    "SPECTATOR",
    "GOURMET",
    "GAME",
    "RPG",
    "COLLECTION",
    "COMPLETE",
    "MAGAZINE",
    "WALK",
    "BIKE",
    "HOBBY",
    "SPORTS",
    "SOFTWARE",
    "SONGS",
    "DIET",
    "TREASURE",
    "TRAVEL",
    "DANCE",
    "CHANNEL",
    "MAKING",
    "FISHING",
    "DATE",
    "DESIGN",
    "LOCOMOTIVE",
    "PLUSH_DOLL",
    "PC",
    "FLOWERS",
    "HERO",
    "NAP",
    "HEROINE",
    "FASHION",
    "ADVENTURE",
    "BOARD",
    "BALL",
    "BOOK",
    "FESTIVAL",
    "COMICS",
    "HOLIDAY",
    "PLANS",
    "TRENDY",
    "VACATION",
    "LOOK"
]
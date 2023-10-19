class DewfordTrend:
	def __init__(self):
		self.trendiness = 0
		self.max_trendiness = 0
		self.is_gaining_trendiness = False
		self.random_value = 0
		self.easy_chat_words = ["", ""]
	
	def setTrendiness(self, value):
		self.trendiness = value
	
	def getTrendiness(self):
		return self.trendiness
	
	def setMaxTrendiness(self, value):
		self.max_trendiness = value
	
	def getMaxTrendiness(self):
		return self.max_trendiness
		
	def setIsGainingTrendiness(self, value):
		self.is_gaining_trendiness = value
	
	def getIsGainingTrendiness(self):
		return self.is_gaining_trendiness
		
	def setRandomValue(self, value):
		self.random_value = value
	
	def getRandomValue(self):
		return self.random_value
		
	def setPhrase(self, phrase_1, phrase_2):
		self.easy_chat_words[0] = phrase_1
		self.easy_chat_words[1] = phrase_2
	
	def getPhrase(self):
		return self.easy_chat_words


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
class database:
    def __init__(self,id,food_database=[],sport_database=[]):
        self.id=id
        # self.user=user
        self.food_database=food_database
        self.sport_database=sport_database
    #[food_name,energy_lost,fat_lost,protein_lost,vitaminA_lost,vitaminB_lost,vitaminC_lost]
    def standardlize_sport_database(self):
        standard_sport_database = [

            ["swimming",10,6,3,1,3,0], ["running",9,8,5,6,4,1], ["cycling",8,7,4,2,3,0],
            ["jump_rope",12,9,6,1,2,1], ["aerobic_dance",7,5,3,0,3,0], ["stair_climbing",11,10,5,2,2,0],
            ["rowing",13,6,7,3,4,0], ["elliptical",9,7,4,1,3,0], ["kickboxing",14,11,8,2,5,1],

            ["deadlift",5,2,9,0,4,0], ["bench_press",4,1,8,0,3,0], ["squat",6,3,10,0,5,0],
            ["pull_up",7,2,9,0,4,0], ["dumbbell_curl",3,1,6,0,2,0], ["kettlebell_swing",8,4,7,1,3,0],

            ["basketball",15,10,7,3,6,2], ["soccer",16,12,8,4,5,1], ["volleyball",9,5,5,2,4,1],
            ["rugby",18,14,10,5,7,2], ["hockey",14,11,9,4,6,1], ["ultimate_frisbee",12,8,6,3,5,1],

            ["water_polo",17,12,9,5,6,2], ["synchronized_swim",10,7,5,3,4,1],
            ["scuba_diving",8,5,4,2,3,0], ["kayaking",11,8,6,3,4,0],

            ["skiing",20,15,8,6,7,3], ["snowboarding",19,14,9,5,6,2],
            ["ice_skating",13,9,6,4,5,1], ["bobsleigh",22,18,12,7,8,3],

            ["boxing",18,12,10,5,8,2], ["taekwondo",16,10,9,4,7,1],
            ["judo",15,9,11,3,6,1], ["muay_thai",20,14,12,6,9,2],

            ["parkour",19,13,11,6,7,2], ["aerial_yoga",7,3,4,2,3,1],
            ["crossfit",21,15,15,8,10,3], ["zumba",12,9,6,3,5,1],

            ["archery",6,2,5,1,3,0], ["fencing",14,8,9,4,6,1],
            ["shot_put",8,3,10,0,4,0], ["javelin",9,4,11,1,5,0],

            ["rock_climbing",17,10,12,5,7,2], ["skydiving",5,3,3,2,2,0],
            ["bmx",15,11,9,4,6,1], ["surfing",16,12,10,6,7,2]
        ]
        self.sport_database = standard_sport_database

    def standardlize_food_database(self):
        #[food_name,energy_gain,fat_gain,protein_gain,vitaminA_gain,vitaminB_gain,vitaminC_gain]
        standard_database = [

                ["beef",10,2,3,4,6,2],
                ["pork",12,4,2,3,5,1],
                ["lamb",14,5,4,5,4,0],
                ["duck",13,6,3,8,3,1],
                ["venison",9,1,5,2,7,2],
                ["bacon",18,9,2,1,2,0],
                ["ham",11,3,4,2,5,1],
                ["sausage",16,8,3,1,3,0],
                ["rabbit",8,1,6,3,6,1],
                ["turkey",7,1,5,2,7,1],
                ["goat",10,2,4,3,5,1],
                ["bison",9,1,6,4,6,2],
                ["chicken",3,2,6,6,6,2],
                ["cornish_hen",4,2,5,5,5,1],
                ["quail",5,3,4,4,4,1],
                ["salmon",9,5,4,6,3,0],
                ["tuna",8,1,7,2,5,1],
                ["cod",6,0,6,1,4,0],
                ["mackerel",11,7,5,5,2,0],
                ["sardine",10,6,4,4,3,0],
                ["tilapia",7,2,5,1,3,0],
                ["shrimp",5,1,4,2,2,0],
                ["lobster",6,1,5,3,3,0],
                ["crab",5,1,4,4,2,0],
                ["milk",5,2,3,2,3,1],
                ["cheddar",12,8,4,3,1,0],
                ["yogurt",4,1,3,1,2,1],
                ["rice",8,0,1,0,2,0],
                ["oatmeal",7,1,2,0,3,0],
                ["quinoa",9,1,4,0,4,0],
                ["lentils",9,0,5,0,4,1],
                ["black_beans",8,0,4,0,3,1],
                ["tofu",5,2,3,0,2,0],
                ["spinach",3,0,1,56,4,28],
                ["kale",4,0,1,49,5,35],["broccoli",5,0,2,12,6,89],
                ["carrot",4,0,1,107,3,7],
                ["sweet_potato",10,0,2,283,4,4],
                ["apple",2,3,4,21,3,2],["banana",9,0,1,1,5,14],
                ["orange",5,0,1,4,4,53],
                ["strawberry",4,0,1,1,3,58],["kiwi",6,0,1,3,4,92],
                ["mango",7,0,1,25,5,46],
                ["almond",16,14,6,0,3,0],["walnut",18,18,4,0,2,0],
                ["chia_seeds",12,9,4,0,2,0],
                ["bread",7,1,2,0,3,0],
                ["pasta",10,1,3,0,2,0],
                ["cereal",9,1,2,15,12,8],
                ["egg",7,5,6,6,9,0],
                ["honey",13,0,0,0,0,1],
                ["dark_chocolate",22,12,3,0,2,0],
                ["kangaroo",9,1,8,3,5,1],["alligator",7,2,6,4,6,0],["ostrich",8,1,7,5,4,1],
                ["elk",10,2,6,3,5,1],["wild_boar",13,5,5,4,4,0],["frog_legs",5,1,4,2,3,1],
                ["snake",6,1,5,3,4,0],["horse",11,3,5,2,5,1],["camel",10,2,4,4,4,1],
                ["swordfish",12,6,5,7,4,0],["halibut",9,3,6,2,5,0],["anchovy",8,5,3,4,3,0],
                ["herring",10,7,4,5,2,0],["monkfish",7,1,5,1,4,0],["sole",6,1,4,1,3,0],
                ["scallop",5,0,4,1,2,0],["clam",4,0,3,2,1,0],["oyster",3,1,2,8,3,1],
                ["mussel",5,1,3,4,2,0],["abalone",6,1,4,3,3,0],["geoduck",5,0,3,2,2,0],
                ["pork_belly",22,15,3,1,2,0],["natto",6,4,5,0,9,0],["durian",16,5,2,3,4,19],
                ["lychee",7,0,1,1,3,72],["bamboo_shoot",3,0,1,2,2,3],["lotus_root",8,0,2,0,4,5],
                ["bird_nest",2,0,1,0,3,0],["sea_cucumber",4,0,3,0,2,0],["century_egg",9,6,4,5,3,0],

                ["acai",9,5,1,15,6,24],["spirulina",4,0,3,230,17,9],["moringa",5,1,2,42,8,23],
                ["camu_camu",2,0,0,0,2,2780],["goji_berry",12,0,2,170,3,29],

                ["shiitake",3,0,1,0,5,2],["morel",4,0,2,2,6,3],["chanterelle",3,0,1,1,4,1],
                ["porcini",5,1,2,0,3,1],["enoki",2,0,1,0,2,1],["maitake",4,0,2,0,4,1],

                ["turnip",3,0,1,0,2,21],["beetroot",6,0,1,1,3,6],["radish",2,0,1,0,2,15],
                ["jicama",5,0,1,0,3,22],["taro",11,0,1,0,4,5],["cassava",16,0,1,0,3,21]

            ]
        self.food_dababase=standard_database

    def create_standard_food_database(self):
        self.food_database=[]
    def sort_food_database_by_energy(self):

        n = len(self.database)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.database[j][1] > self.database[j + 1][1]:
                    self.database[j], self.database[j + 1] = self.database[j + 1], self.database[j]
        return self.database

    def sort_food_database_by_fat(self):

        n = len(self.database)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.database[j][2] > self.database[j + 1][2]:
                    self.database[j], self.database[j + 1] = self.database[j + 1], self.database[j]
        return self.database

    def sort_food_database_by_vita(self):

        n = len(self.database)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.database[j][3] > self.database[j + 1][3]:
                    self.database[j], self.database[j + 1] = self.database[j + 1], self.database[j]
        return self.database

    def sort_food_database_by_vitb(self):

        n = len(self.database)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.database[j][4] > self.database[j + 1][4]:
                    self.database[j], self.database[j + 1] = self.database[j + 1], self.database[j]
        return self.database

    def sort_food_database_by_vitc(self):

        n = len(self.database)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.database[j][5] > self.database[j + 1][5]:
                    self.database[j], self.database[j + 1] = self.database[j + 1], self.database[j]
        return self.database

"""
Expanded Food Database for Ne Yenir?
Comprehensive food database with international and Turkish cuisine
"""

def get_expanded_food_database():
    """Return expanded food database with much more variety"""
    from main import Food
    
    expanded_foods = [
        # Turkish Cuisine - Expanded
        Food(1, "Adana Kebab", "Turkish", ["spicy", "smoky", "salty"], 8, "tender", "grilled", 
             ["lamb", "spices"], [], "mid-range", "hot"),
        Food(2, "İskender Kebab", "Turkish", ["savory", "rich", "salty"], 7, "tender", "grilled",
             ["lamb", "yogurt", "tomato"], [], "mid-range", "hot"),
        Food(3, "Döner Kebab", "Turkish", ["savory", "spicy"], 6, "tender", "grilled",
             ["lamb", "beef", "spices"], [], "budget", "hot"),
        Food(4, "Şiş Kebab", "Turkish", ["smoky", "savory"], 7, "tender", "grilled",
             ["lamb", "vegetables"], [], "mid-range", "hot"),
        Food(5, "Köfte", "Turkish", ["savory", "rich"], 6, "tender", "grilled",
             ["ground meat", "spices"], [], "budget", "hot"),
        Food(6, "Manti", "Turkish", ["savory", "rich"], 6, "tender", "boiled",
             ["beef", "dough", "yogurt"], [], "mid-range", "hot"),
        Food(7, "Lahmacun", "Turkish", ["spicy", "savory"], 7, "crispy", "baked",
             ["lamb", "vegetables", "spices"], [], "budget", "hot"),
        Food(8, "Pide", "Turkish", ["savory", "rich"], 6, "crispy", "baked",
             ["cheese", "meat", "vegetables"], [], "budget", "hot"),
        Food(9, "Çiğ Köfte", "Turkish", ["spicy", "tangy"], 8, "chewy", "raw",
             ["bulgur", "spices", "vegetables"], ["vegan"], "budget", "room-temp"),
        Food(10, "Dolma", "Turkish", ["savory", "herbal"], 5, "tender", "steamed",
              ["grape leaves", "rice", "herbs"], ["vegetarian"], "budget", "warm"),
        Food(11, "Sarma", "Turkish", ["savory", "tangy"], 6, "tender", "boiled",
              ["cabbage", "rice", "meat"], [], "budget", "hot"),
        Food(12, "Karnıyarık", "Turkish", ["savory", "rich"], 7, "tender", "baked",
              ["eggplant", "ground meat"], [], "mid-range", "hot"),
        Food(13, "İmam Bayıldı", "Turkish", ["savory", "rich"], 6, "tender", "baked",
              ["eggplant", "onion", "olive oil"], ["vegetarian"], "mid-range", "hot"),
        Food(14, "Menemen", "Turkish", ["savory", "fresh"], 5, "creamy", "stirred",
              ["eggs", "tomatoes", "peppers"], ["vegetarian"], "budget", "hot"),
        Food(15, "Balık Ekmek", "Turkish", ["fresh", "savory"], 6, "tender", "grilled",
              ["fish", "bread", "vegetables"], [], "budget", "hot"),
        Food(16, "Midye Dolma", "Turkish", ["briny", "savory"], 6, "tender", "steamed",
              ["mussels", "rice", "spices"], [], "budget", "room-temp"),
        Food(17, "Börek", "Turkish", ["savory", "rich"], 6, "crispy", "baked",
              ["phyllo", "cheese", "spinach"], ["vegetarian"], "budget", "hot"),
        Food(18, "Mantı", "Turkish", ["savory", "rich"], 6, "tender", "boiled",
              ["dough", "meat", "yogurt"], [], "mid-range", "hot"),
        Food(19, "Pilav", "Turkish", ["savory", "aromatic"], 4, "fluffy", "boiled",
              ["rice", "butter", "spices"], ["vegetarian"], "budget", "hot"),
        Food(20, "Baklava", "Turkish", ["sweet", "rich"], 8, "crispy", "baked",
              ["phyllo", "nuts", "honey"], ["vegetarian"], "mid-range", "room-temp"),
        Food(21, "Künefe", "Turkish", ["sweet", "creamy"], 9, "crispy", "baked",
              ["shredded pastry", "cheese", "syrup"], ["vegetarian"], "mid-range", "hot"),
        Food(22, "Lokum", "Turkish", ["sweet", "perfumed"], 7, "chewy", "raw",
              ["sugar", "starch", "flavoring"], ["vegetarian"], "budget", "room-temp"),

        # Mediterranean Cuisine
        Food(23, "Greek Salad", "Greek", ["fresh", "tangy", "salty"], 5, "crispy", "raw",
             ["tomatoes", "olives", "feta"], ["vegetarian"], "budget", "cold"),
        Food(24, "Moussaka", "Greek", ["rich", "savory"], 8, "creamy", "baked",
             ["eggplant", "meat", "bechamel"], [], "mid-range", "hot"),
        Food(25, "Souvlaki", "Greek", ["smoky", "savory"], 7, "tender", "grilled",
             ["pork", "chicken", "herbs"], [], "mid-range", "hot"),
        Food(26, "Spanakopita", "Greek", ["savory", "rich"], 6, "crispy", "baked",
             ["spinach", "feta", "phyllo"], ["vegetarian"], "mid-range", "hot"),
        Food(27, "Hummus", "Lebanese", ["creamy", "nutty"], 4, "creamy", "raw",
             ["chickpeas", "tahini", "lemon"], ["vegan"], "budget", "room-temp"),
        Food(28, "Tabbouleh", "Lebanese", ["fresh", "tangy"], 5, "crispy", "raw",
             ["parsley", "bulgur", "lemon"], ["vegan"], "budget", "cold"),
        Food(29, "Falafel", "Lebanese", ["savory", "crispy"], 6, "crispy", "fried",
             ["chickpeas", "herbs", "spices"], ["vegan"], "budget", "hot"),

        # Italian Cuisine - Expanded
        Food(30, "Margherita Pizza", "Italian", ["savory", "fresh"], 6, "crispy", "baked",
             ["tomato", "mozzarella", "basil"], ["vegetarian"], "budget", "hot"),
        Food(31, "Carbonara", "Italian", ["rich", "creamy"], 8, "creamy", "stirred",
             ["pasta", "eggs", "pancetta"], [], "mid-range", "hot"),
        Food(32, "Bolognese", "Italian", ["rich", "savory"], 7, "tender", "braised",
             ["pasta", "meat", "tomato"], [], "mid-range", "hot"),
        Food(33, "Risotto Milanese", "Italian", ["rich", "creamy"], 7, "creamy", "stirred",
             ["rice", "saffron", "parmesan"], ["vegetarian"], "mid-range", "hot"),
        Food(34, "Osso Buco", "Italian", ["rich", "tender"], 9, "tender", "braised",
             ["veal", "vegetables", "wine"], [], "premium", "hot"),
        Food(35, "Tiramisu", "Italian", ["sweet", "rich"], 8, "creamy", "raw",
             ["mascarpone", "coffee", "cocoa"], ["vegetarian"], "mid-range", "cold"),
        Food(36, "Bruschetta", "Italian", ["fresh", "savory"], 5, "crispy", "toasted",
             ["bread", "tomatoes", "basil"], ["vegetarian"], "budget", "warm"),
        Food(37, "Lasagna", "Italian", ["rich", "savory"], 8, "tender", "baked",
             ["pasta", "meat", "cheese"], [], "mid-range", "hot"),
        Food(38, "Prosciutto e Melone", "Italian", ["salty", "sweet"], 6, "tender", "raw",
             ["ham", "melon"], [], "mid-range", "cold"),

        # French Cuisine - Expanded
        Food(39, "Coq au Vin", "French", ["rich", "savory", "complex"], 8, "tender", "braised",
             ["chicken", "wine", "herbs"], [], "premium", "hot"),
        Food(40, "Beef Bourguignon", "French", ["rich", "deep"], 9, "tender", "braised",
             ["beef", "wine", "vegetables"], [], "premium", "hot"),
        Food(41, "Ratatouille", "French", ["fresh", "herbal"], 6, "tender", "stewed",
             ["vegetables", "herbs"], ["vegan"], "mid-range", "hot"),
        Food(42, "French Onion Soup", "French", ["savory", "rich"], 7, "tender", "simmered",
             ["onions", "cheese", "broth"], ["vegetarian"], "mid-range", "hot"),
        Food(43, "Bouillabaisse", "French", ["complex", "briny"], 8, "tender", "simmered",
             ["seafood", "saffron", "herbs"], [], "premium", "hot"),
        Food(44, "Escargots", "French", ["rich", "garlicky"], 7, "tender", "baked",
             ["snails", "garlic", "butter"], [], "premium", "hot"),
        Food(45, "Crème Brûlée", "French", ["sweet", "rich"], 8, "creamy", "baked",
             ["cream", "vanilla", "sugar"], ["vegetarian"], "mid-range", "cold"),
        Food(46, "Foie Gras", "French", ["rich", "buttery"], 10, "creamy", "pan-fried",
             ["duck liver"], [], "premium", "hot"),

        # Japanese Cuisine - Expanded
        Food(47, "Sushi Omakase", "Japanese", ["fresh", "umami", "delicate"], 8, "tender", "raw",
             ["fish", "rice", "seaweed"], [], "premium", "cold"),
        Food(48, "Ramen", "Japanese", ["rich", "umami"], 8, "chewy", "boiled",
             ["noodles", "broth", "pork"], [], "budget", "hot"),
        Food(49, "Tempura", "Japanese", ["crispy", "light"], 6, "crispy", "fried",
             ["seafood", "vegetables", "batter"], [], "mid-range", "hot"),
        Food(50, "Sashimi", "Japanese", ["fresh", "clean"], 8, "tender", "raw",
             ["raw fish"], [], "premium", "cold"),
        Food(51, "Yakitori", "Japanese", ["smoky", "savory"], 7, "tender", "grilled",
             ["chicken", "sauce"], [], "mid-range", "hot"),
        Food(52, "Miso Soup", "Japanese", ["umami", "light"], 4, "liquid", "simmered",
             ["miso", "tofu", "seaweed"], ["vegetarian"], "budget", "hot"),
        Food(53, "Gyoza", "Japanese", ["savory", "crispy"], 6, "crispy", "pan-fried",
             ["pork", "vegetables", "wrapper"], [], "budget", "hot"),

        # Chinese Cuisine
        Food(54, "Peking Duck", "Chinese", ["rich", "crispy"], 8, "crispy", "roasted",
             ["duck", "pancakes", "sauce"], [], "premium", "hot"),
        Food(55, "Kung Pao Chicken", "Chinese", ["spicy", "savory"], 7, "tender", "stir-fried",
             ["chicken", "peanuts", "chili"], [], "mid-range", "hot"),
        Food(56, "Sweet and Sour Pork", "Chinese", ["sweet", "tangy"], 6, "crispy", "fried",
             ["pork", "vegetables", "sauce"], [], "mid-range", "hot"),
        Food(57, "Mapo Tofu", "Chinese", ["spicy", "numbing"], 8, "soft", "braised",
             ["tofu", "ground pork", "chili"], [], "mid-range", "hot"),
        Food(58, "Dim Sum", "Chinese", ["savory", "delicate"], 6, "tender", "steamed",
             ["various fillings", "wrappers"], [], "mid-range", "warm"),

        # Indian Cuisine
        Food(59, "Butter Chicken", "Indian", ["rich", "spicy"], 8, "creamy", "simmered",
             ["chicken", "tomato", "cream"], [], "mid-range", "hot"),
        Food(60, "Biryani", "Indian", ["aromatic", "spicy"], 7, "fluffy", "steamed",
             ["rice", "meat", "spices"], [], "mid-range", "hot"),
        Food(61, "Tikka Masala", "Indian", ["spicy", "creamy"], 8, "tender", "simmered",
             ["chicken", "tomato", "spices"], [], "mid-range", "hot"),
        Food(62, "Samosas", "Indian", ["crispy", "spicy"], 6, "crispy", "fried",
             ["pastry", "vegetables", "spices"], ["vegetarian"], "budget", "hot"),
        Food(63, "Dal Makhani", "Indian", ["rich", "creamy"], 7, "creamy", "simmered",
             ["lentils", "butter", "cream"], ["vegetarian"], "mid-range", "hot"),

        # Mexican Cuisine
        Food(64, "Tacos al Pastor", "Mexican", ["spicy", "savory"], 7, "tender", "grilled",
             ["pork", "pineapple", "chili"], [], "budget", "hot"),
        Food(65, "Guacamole", "Mexican", ["fresh", "creamy"], 5, "creamy", "raw",
             ["avocado", "lime", "cilantro"], ["vegan"], "budget", "room-temp"),
        Food(66, "Enchiladas", "Mexican", ["spicy", "rich"], 7, "tender", "baked",
             ["tortillas", "meat", "sauce"], [], "mid-range", "hot"),
        Food(67, "Chiles Rellenos", "Mexican", ["spicy", "rich"], 8, "crispy", "fried",
             ["peppers", "cheese", "batter"], ["vegetarian"], "mid-range", "hot"),
        Food(68, "Mole Poblano", "Mexican", ["complex", "rich"], 9, "thick", "simmered",
             ["chicken", "chocolate", "spices"], [], "premium", "hot"),

        # American Cuisine
        Food(69, "BBQ Ribs", "American", ["smoky", "sweet"], 8, "tender", "smoked",
             ["pork ribs", "sauce"], [], "mid-range", "hot"),
        Food(70, "Caesar Salad", "American", ["fresh", "salty", "tangy"], 5, "crispy", "raw",
             ["lettuce", "cheese", "croutons"], ["vegetarian"], "budget", "cold"),
        Food(71, "Clam Chowder", "American", ["creamy", "briny"], 7, "creamy", "simmered",
             ["clams", "potatoes", "cream"], [], "mid-range", "hot"),
        Food(72, "Buffalo Wings", "American", ["spicy", "tangy"], 8, "crispy", "fried",
             ["chicken wings", "hot sauce"], [], "budget", "hot"),
        Food(73, "Apple Pie", "American", ["sweet", "cinnamon"], 7, "tender", "baked",
             ["apples", "pastry", "spices"], ["vegetarian"], "mid-range", "warm"),

        # British Cuisine
        Food(74, "Fish and Chips", "British", ["crispy", "savory"], 6, "crispy", "fried",
             ["fish", "potatoes"], [], "budget", "hot"),
        Food(75, "Beef Wellington", "British", ["rich", "savory", "umami"], 9, "tender", "roasted",
             ["beef", "mushroom", "pastry"], [], "premium", "hot"),
        Food(76, "Shepherd's Pie", "British", ["rich", "savory"], 7, "creamy", "baked",
             ["lamb", "vegetables", "potato"], [], "mid-range", "hot"),
        Food(77, "Bangers and Mash", "British", ["savory", "rich"], 6, "creamy", "boiled",
             ["sausages", "potatoes"], [], "budget", "hot"),

        # Spanish Cuisine
        Food(78, "Paella", "Spanish", ["savory", "aromatic"], 8, "tender", "steamed",
             ["rice", "saffron", "seafood"], [], "premium", "hot"),
        Food(79, "Tapas Platter", "Spanish", ["varied", "savory"], 6, "mixed", "mixed",
             ["olives", "cheese", "ham"], [], "mid-range", "room-temp"),
        Food(80, "Gazpacho", "Spanish", ["fresh", "tangy"], 5, "liquid", "raw",
             ["tomatoes", "vegetables"], ["vegan"], "budget", "cold"),
        Food(81, "Churros", "Spanish", ["sweet", "crispy"], 7, "crispy", "fried",
             ["dough", "sugar", "chocolate"], ["vegetarian"], "budget", "hot"),

        # Desserts and Sweets
        Food(82, "Chocolate Lava Cake", "International", ["sweet", "rich"], 9, "creamy", "baked",
              ["chocolate", "butter", "eggs"], ["vegetarian"], "mid-range", "hot"),
        Food(83, "Cheesecake", "International", ["sweet", "creamy"], 8, "creamy", "baked",
              ["cream cheese", "graham crackers"], ["vegetarian"], "mid-range", "cold"),
        Food(84, "Ice Cream", "International", ["sweet", "cold"], 7, "creamy", "frozen",
              ["cream", "sugar", "flavoring"], ["vegetarian"], "budget", "cold"),
        Food(85, "Chocolate Mousse", "French", ["sweet", "rich"], 8, "airy", "whipped",
              ["chocolate", "cream", "eggs"], ["vegetarian"], "mid-range", "cold"),

        # Breakfast Items
        Food(86, "Turkish Breakfast", "Turkish", ["varied", "fresh"], 6, "mixed", "mixed",
              ["cheese", "olives", "tomatoes"], ["vegetarian"], "mid-range", "room-temp"),
        Food(87, "Pancakes", "American", ["sweet", "fluffy"], 6, "fluffy", "pan-fried",
              ["flour", "eggs", "milk"], ["vegetarian"], "budget", "hot"),
        Food(88, "French Toast", "French", ["sweet", "rich"], 7, "tender", "pan-fried",
              ["bread", "eggs", "cream"], ["vegetarian"], "budget", "hot"),
        Food(89, "Benedict Eggs", "American", ["rich", "creamy"], 8, "creamy", "poached",
              ["eggs", "ham", "hollandaise"], [], "mid-range", "hot"),

        # Seafood Specialties
        Food(90, "Grilled Salmon", "International", ["rich", "smoky"], 6, "tender", "grilled",
             ["salmon", "herbs"], [], "premium", "hot"),
        Food(91, "Oysters", "French", ["briny", "fresh", "mineral"], 7, "tender", "raw",
             ["oysters"], [], "premium", "cold"),
        Food(92, "Lobster Thermidor", "French", ["rich", "luxurious"], 9, "tender", "baked",
             ["lobster", "cream", "cheese"], [], "premium", "hot"),
        Food(93, "Fish Tacos", "Mexican", ["fresh", "spicy"], 6, "tender", "grilled",
             ["fish", "tortillas", "cabbage"], [], "budget", "hot"),
        Food(94, "Shrimp Scampi", "Italian", ["garlicky", "buttery"], 7, "tender", "sautéed",
             ["shrimp", "garlic", "butter"], [], "mid-range", "hot"),

        # Vegetarian Specialties
        Food(95, "Mushroom Risotto", "Italian", ["rich", "earthy", "creamy"], 7, "creamy", "stirred",
             ["rice", "mushrooms", "cheese"], ["vegetarian"], "mid-range", "hot"),
        Food(96, "Caprese Salad", "Italian", ["fresh", "creamy"], 5, "tender", "raw",
             ["tomatoes", "mozzarella", "basil"], ["vegetarian"], "budget", "room-temp"),
        Food(97, "Quinoa Salad", "International", ["fresh", "nutty"], 5, "tender", "boiled",
             ["quinoa", "vegetables", "herbs"], ["vegan"], "budget", "room-temp"),
        Food(98, "Stuffed Bell Peppers", "International", ["savory", "hearty"], 6, "tender", "baked",
             ["peppers", "rice", "vegetables"], ["vegetarian"], "mid-range", "hot"),
        Food(99, "Vegetable Curry", "Indian", ["spicy", "aromatic"], 7, "tender", "simmered",
             ["mixed vegetables", "spices"], ["vegan"], "mid-range", "hot"),
        Food(100, "Avocado Toast", "International", ["fresh", "creamy"], 5, "creamy", "toasted",
              ["avocado", "bread", "toppings"], ["vegetarian"], "budget", "warm"),
    ]
    
    return expanded_foods

def get_expanded_alcohol_database():
    """Return expanded alcohol database with much more variety"""
    from main import Alcohol
    
    expanded_alcohols = [
        # Turkish Alcohols - Expanded
        Alcohol(1, "Rakı (Yeni Rakı)", "spirits", "anise", 45.0, ["anise", "herbal"], "full", 1, 2, 0, "mid-range", "Turkey", None),
        Alcohol(2, "Rakı (Tekirdağ)", "spirits", "anise", 45.0, ["anise", "smooth"], "full", 1, 2, 0, "mid-range", "Turkey", None),
        Alcohol(3, "Turkish Red Wine (Kalecik Karası)", "wine", "red", 13.5, ["fruity", "earthy"], "medium", 3, 6, 6, "mid-range", "Turkey", 2020),
        Alcohol(4, "Turkish White Wine (Narince)", "wine", "white", 12.5, ["floral", "crisp"], "light", 2, 7, 1, "mid-range", "Turkey", 2021),
        Alcohol(5, "Turkish Rosé (Öküzgözü)", "wine", "rosé", 12.0, ["berry", "fresh"], "light", 4, 6, 2, "mid-range", "Turkey", 2022),
        Alcohol(6, "Efes Pilsener", "beer", "lager", 5.0, ["crisp", "malty"], "light", 3, 5, 0, "budget", "Turkey", None),
        Alcohol(7, "Bomonti Filtresiz", "beer", "wheat", 4.9, ["cloudy", "citrus"], "light", 2, 6, 0, "budget", "Turkey", None),

        # Wine Collection - Expanded
        Alcohol(8, "Cabernet Sauvignon (Bordeaux)", "wine", "red", 14.0, ["dark fruit", "oak", "tannins"], "full", 2, 5, 8, "premium", "France", 2019),
        Alcohol(9, "Chardonnay (Burgundy)", "wine", "white", 13.0, ["citrus", "oak", "butter"], "medium", 4, 7, 2, "premium", "France", 2021),
        Alcohol(10, "Pinot Noir (Oregon)", "wine", "red", 12.5, ["red fruit", "earthy"], "light", 3, 6, 4, "premium", "USA", 2020),
        Alcohol(11, "Sauvignon Blanc (Marlborough)", "wine", "white", 12.0, ["citrus", "grass", "mineral"], "light", 2, 8, 1, "mid-range", "New Zealand", 2022),
        Alcohol(12, "Champagne (Dom Pérignon)", "wine", "sparkling", 12.5, ["citrus", "yeast", "mineral"], "light", 3, 8, 2, "premium", "France", 2018),
        Alcohol(13, "Prosecco", "wine", "sparkling", 11.0, ["apple", "pear", "floral"], "light", 5, 7, 1, "mid-range", "Italy", 2022),
        Alcohol(14, "Riesling (Mosel)", "wine", "white", 8.5, ["peach", "mineral", "sweet"], "light", 7, 9, 1, "premium", "Germany", 2021),
        Alcohol(15, "Malbec (Mendoza)", "wine", "red", 14.5, ["plum", "spice", "full"], "full", 2, 5, 7, "mid-range", "Argentina", 2020),
        Alcohol(16, "Chianti Classico", "wine", "red", 13.5, ["cherry", "herbs", "mineral"], "medium", 3, 6, 6, "mid-range", "Italy", 2019),
        Alcohol(17, "Barolo", "wine", "red", 14.0, ["rose", "tar", "powerful"], "full", 1, 6, 9, "premium", "Italy", 2018),
        Alcohol(18, "Sancerre", "wine", "white", 12.5, ["citrus", "mineral", "crisp"], "light", 2, 8, 1, "premium", "France", 2022),
        Alcohol(19, "Port Wine (Vintage)", "wine", "fortified", 20.0, ["sweet", "rich", "dark fruit"], "full", 8, 4, 7, "premium", "Portugal", None),
        Alcohol(20, "Moscato d'Asti", "wine", "sweet", 5.5, ["peach", "honey", "floral"], "light", 9, 6, 1, "mid-range", "Italy", 2022),

        # Beer Collection - Expanded
        Alcohol(21, "IPA (American)", "beer", "ale", 6.5, ["hoppy", "bitter", "citrus"], "medium", 2, 4, 0, "budget", "USA", None),
        Alcohol(22, "Pilsner (Czech)", "beer", "lager", 4.8, ["crisp", "light", "malty"], "light", 3, 5, 0, "budget", "Czech Republic", None),
        Alcohol(23, "Stout (Irish)", "beer", "ale", 5.5, ["roasted", "chocolate", "coffee"], "full", 1, 3, 0, "mid-range", "Ireland", None),
        Alcohol(24, "Wheat Beer (German)", "beer", "wheat", 5.2, ["citrus", "spice", "smooth"], "light", 4, 5, 0, "budget", "Germany", None),
        Alcohol(25, "Belgian Dubbel", "beer", "ale", 7.0, ["caramel", "spice", "rich"], "medium", 5, 4, 0, "mid-range", "Belgium", None),
        Alcohol(26, "Lager (Mexican)", "beer", "lager", 4.6, ["light", "crisp", "lime"], "light", 2, 6, 0, "budget", "Mexico", None),
        Alcohol(27, "Porter", "beer", "ale", 5.8, ["chocolate", "coffee", "smooth"], "medium", 2, 4, 0, "mid-range", "England", None),
        Alcohol(28, "Saison", "beer", "ale", 6.5, ["spicy", "fruity", "dry"], "light", 3, 6, 0, "mid-range", "Belgium", None),

        # Spirits Collection - Expanded  
        Alcohol(29, "Single Malt Whiskey (Islay)", "spirits", "whiskey", 40.0, ["smoky", "peaty", "maritime"], "full", 1, 3, 0, "premium", "Scotland", None),
        Alcohol(30, "Bourbon Whiskey", "spirits", "whiskey", 40.0, ["vanilla", "caramel", "oak"], "full", 4, 3, 0, "mid-range", "USA", None),
        Alcohol(31, "Japanese Whisky", "spirits", "whiskey", 43.0, ["delicate", "floral", "honey"], "medium", 3, 4, 0, "premium", "Japan", None),
        Alcohol(32, "Cognac VSOP", "spirits", "brandy", 40.0, ["fruit", "oak", "smooth"], "full", 4, 3, 0, "premium", "France", None),
        Alcohol(33, "Tequila Reposado", "spirits", "tequila", 38.0, ["agave", "oak", "spice"], "medium", 2, 4, 0, "mid-range", "Mexico", None),
        Alcohol(34, "Vodka Premium", "spirits", "vodka", 40.0, ["clean", "neutral"], "light", 1, 1, 0, "premium", "Russia", None),
        Alcohol(35, "London Dry Gin", "spirits", "gin", 40.0, ["juniper", "citrus", "botanical"], "medium", 1, 5, 0, "mid-range", "England", None),
        Alcohol(36, "Rum Aged", "spirits", "rum", 40.0, ["caramel", "spice", "tropical"], "full", 5, 3, 0, "mid-range", "Caribbean", None),
        Alcohol(37, "Mezcal", "spirits", "mezcal", 40.0, ["smoky", "earthy", "agave"], "full", 1, 4, 0, "premium", "Mexico", None),

        # Cocktails Collection - Expanded
        Alcohol(38, "Gin & Tonic", "cocktail", "gin-based", 8.0, ["juniper", "citrus", "bitter"], "light", 3, 6, 0, "mid-range", "International", None),
        Alcohol(39, "Manhattan", "cocktail", "whiskey-based", 25.0, ["sweet", "bitter", "strong"], "full", 6, 4, 0, "premium", "USA", None),
        Alcohol(40, "Mojito", "cocktail", "rum-based", 10.0, ["mint", "lime", "sweet"], "light", 7, 7, 0, "mid-range", "Cuba", None),
        Alcohol(41, "Old Fashioned", "cocktail", "whiskey-based", 30.0, ["bitter", "sweet", "strong"], "full", 5, 3, 0, "premium", "USA", None),
        Alcohol(42, "Margarita", "cocktail", "tequila-based", 15.0, ["lime", "salt", "agave"], "medium", 4, 7, 0, "mid-range", "Mexico", None),
        Alcohol(43, "Negroni", "cocktail", "gin-based", 20.0, ["bitter", "herbal", "complex"], "medium", 4, 5, 0, "premium", "Italy", None),
        Alcohol(44, "Pina Colada", "cocktail", "rum-based", 12.0, ["coconut", "pineapple", "sweet"], "medium", 8, 3, 0, "mid-range", "Puerto Rico", None),
        Alcohol(45, "Bloody Mary", "cocktail", "vodka-based", 8.0, ["savory", "spicy", "tomato"], "medium", 1, 6, 0, "mid-range", "USA", None),
        Alcohol(46, "Cosmopolitan", "cocktail", "vodka-based", 15.0, ["cranberry", "lime", "sweet"], "light", 6, 6, 0, "mid-range", "USA", None),
        Alcohol(47, "Whiskey Sour", "cocktail", "whiskey-based", 18.0, ["sour", "sweet", "frothy"], "medium", 5, 7, 0, "mid-range", "USA", None),
        Alcohol(48, "Daiquiri", "cocktail", "rum-based", 15.0, ["lime", "sweet", "clean"], "light", 5, 7, 0, "mid-range", "Cuba", None),
        Alcohol(49, "Aperol Spritz", "cocktail", "aperitif", 8.0, ["bitter", "orange", "bubbly"], "light", 5, 6, 0, "budget", "Italy", None),

        # Sake Collection
        Alcohol(50, "Junmai Sake", "sake", "pure rice", 15.5, ["rice", "floral", "clean"], "light", 4, 5, 0, "premium", "Japan", None),
        Alcohol(51, "Junmai Daiginjo", "sake", "premium", 16.0, ["elegant", "fruity", "refined"], "light", 3, 6, 0, "premium", "Japan", None),
        Alcohol(52, "Nigori Sake", "sake", "unfiltered", 15.0, ["creamy", "sweet", "rice"], "medium", 6, 4, 0, "mid-range", "Japan", None),

        # Specialty & Regional
        Alcohol(53, "Grappa", "spirits", "grape brandy", 40.0, ["grape", "strong", "warming"], "full", 1, 4, 0, "premium", "Italy", None),
        Alcohol(54, "Ouzo", "spirits", "anise", 40.0, ["anise", "Mediterranean"], "full", 2, 3, 0, "mid-range", "Greece", None),
        Alcohol(55, "Soju", "spirits", "rice spirit", 20.0, ["clean", "light", "smooth"], "light", 2, 2, 0, "budget", "Korea", None),
        Alcohol(56, "Cachaca", "spirits", "sugarcane", 40.0, ["sugarcane", "grassy", "tropical"], "medium", 3, 4, 0, "mid-range", "Brazil", None),
        Alcohol(57, "Pisco", "spirits", "grape brandy", 40.0, ["floral", "grape", "smooth"], "medium", 2, 5, 0, "mid-range", "Peru", None),
        Alcohol(58, "Absinthe", "spirits", "herbal", 68.0, ["anise", "wormwood", "strong"], "full", 1, 2, 0, "premium", "France", None),

        # Low Alcohol & Aperitifs
        Alcohol(59, "Vermouth Rosso", "fortified", "sweet", 15.0, ["herbal", "sweet", "complex"], "medium", 7, 4, 0, "mid-range", "Italy", None),
        Alcohol(60, "Vermouth Dry", "fortified", "dry", 15.0, ["herbal", "dry", "complex"], "light", 2, 6, 0, "mid-range", "France", None),
        Alcohol(61, "Campari", "aperitif", "bitter", 25.0, ["bitter", "herbal", "red"], "medium", 3, 5, 0, "mid-range", "Italy", None),
        Alcohol(62, "Aperol", "aperitif", "bitter", 11.0, ["orange", "bitter", "light"], "light", 5, 6, 0, "budget", "Italy", None),
        Alcohol(63, "Sherry (Fino)", "wine", "fortified", 15.0, ["dry", "nutty", "saline"], "light", 1, 7, 0, "mid-range", "Spain", None),
        Alcohol(64, "Madeira", "wine", "fortified", 19.0, ["nutty", "caramel", "oxidized"], "full", 6, 6, 0, "premium", "Portugal", None),

        # Non-Alcoholic Alternatives
        Alcohol(65, "Kombucha", "fermented", "tea-based", 0.5, ["tangy", "probiotic", "fizzy"], "light", 3, 6, 0, "budget", "International", None),
        Alcohol(66, "Mocktail Virgin Mojito", "mocktail", "mint-based", 0.0, ["mint", "lime", "refreshing"], "light", 6, 7, 0, "budget", "International", None),
        Alcohol(67, "Craft Ginger Beer", "soft drink", "ginger", 0.0, ["spicy", "ginger", "fizzy"], "medium", 4, 6, 0, "budget", "International", None),
    ]
    
    return expanded_alcohols

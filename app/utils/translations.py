"""
Çeviri sözlükleri ve Jinja2 filtreleri
"""

# Çeviri sözlükleri
FLAVOR_TRANSLATIONS = {
    "spicy": "baharatlı", "sweet": "tatlı", "salty": "tuzlu", "sour": "ekşi",
    "bitter": "acı", "umami": "umami", "rich": "zengin", "fresh": "taze",
    "smoky": "dumanlı", "savory": "lezzetli", "acidic": "asitli", "mineral": "mineral",
    "fruity": "meyveli", "floral": "çiçeksi", "earthy": "toprak", "creamy": "kremsi",
    "crispy": "gevrek", "briny": "tuzlu", "delicate": "narin", "complex": "karmaşık",
    "herbal": "bitkisel", "citrus": "narenciye", "dark fruit": "koyu meyve", 
    "red fruit": "kırmızı meyve", "oak": "meşe", "tannins": "tanen",
    "butter": "tereyağı", "grass": "çimen", "yeast": "maya", "hoppy": "şerbetçiotu",
    "malty": "maltlı", "roasted": "kavrulmuş", "chocolate": "çikolata", 
    "coffee": "kahve", "vanilla": "vanilya", "juniper": "ardıç", "mint": "nane",
    "lime": "limon", "rice": "pirinç", "clean": "temiz", "anise": "anason",
    "tangy": "buruk", "perfumed": "kokulu", "nutty": "fındıksı", "deep": "derin",
    "garlicky": "sarımsaksı", "aromatic": "aromatik", "cinnamon": "tarçınlı",
    "varied": "çeşitli", "cold": "soğuk", "fluffy": "kabarık", "luxurious": "lüks",
    "buttery": "tereyağımsı", "hearty": "doyurucu"
}

PRICE_TRANSLATIONS = {
    "budget": "ekonomik",
    "mid-range": "orta",
    "premium": "premium"
}

BODY_TRANSLATIONS = {
    "light": "hafif",
    "medium": "orta",
    "full": "dolgun"
}

TYPE_TRANSLATIONS = {
    "wine": "şarap",
    "beer": "bira",
    "spirits": "alkollü içki",
    "cocktail": "kokteyl",
    "sake": "sake"
}

SUBTYPE_TRANSLATIONS = {
    "red": "kırmızı",
    "white": "beyaz",
    "sparkling": "köpüklü",
    "rosé": "roze",
    "dessert": "tatlı",
    "fortified": "takviyeli",
    "ale": "ale",
    "lager": "lager",
    "stout": "stout",
    "ipa": "IPA",
    "pilsner": "pilsner",
    "wheat beer": "buğday birası",
    "whiskey": "viski",
    "gin": "cin",
    "vodka": "votka",
    "rum": "rom",
    "tequila": "tekila",
    "brandy": "kanyak",
    "cognac": "kanyak",
    "anise": "anason",
    "gin-based": "cin bazlı",
    "whiskey-based": "viski bazlı",
    "rum-based": "rom bazlı",
    "pure rice": "saf pirinç"
}

REGION_TRANSLATIONS = {
    "turkey": "Türkiye",
    "france": "Fransa",
    "italy": "İtalya",
    "spain": "İspanya",
    "portugal": "Portekiz",
    "germany": "Almanya",
    "usa": "ABD",
    "united states": "ABD",
    "new zealand": "Yeni Zelanda",
    "australia": "Avustralya",
    "chile": "Şili",
    "argentina": "Arjantin",
    "south africa": "Güney Afrika",
    "japan": "Japonya",
    "china": "Çin",
    "scotland": "İskoçya",
    "ireland": "İrlanda",
    "mexico": "Meksika",
    "cuba": "Küba",
    "jamaica": "Jamaika",
    "international": "Uluslararası",
    "czech republic": "Çek Cumhuriyeti",
    "england": "İngiltere",
    "uk": "Birleşik Krallık"
}

CUISINE_TRANSLATIONS = {
    "turkish": "Türk",
    "french": "Fransız",
    "italian": "İtalyan",
    "japanese": "Japon",
    "chinese": "Çin",
    "american": "Amerikan",
    "mexican": "Meksika",
    "indian": "Hint",
    "thai": "Tayland",
    "greek": "Yunan",
    "spanish": "İspanyol",
    "british": "İngiliz",
    "german": "Alman",
    "korean": "Kore",
    "vietnamese": "Vietnam",
    "lebanese": "Lübnan",
    "moroccan": "Fas",
    "brazilian": "Brezilya",
    "argentinian": "Arjantin",
    "international": "Uluslararası",
    "mediterranean": "Akdeniz",
    "middle eastern": "Orta Doğu",
    "asian": "Asya"
}

def register_filters(app):
    """Jinja2 filtrelerini kaydet"""
    @app.template_filter('translate_flavor')
    def translate_flavor(flavor):
        """Lezzet notalarını Türkçeye çevir"""
        return FLAVOR_TRANSLATIONS.get(flavor.lower(), flavor)

    @app.template_filter('translate_price')
    def translate_price(price):
        """Fiyat aralığını Türkçeye çevir"""
        return PRICE_TRANSLATIONS.get(price.lower(), price)

    @app.template_filter('translate_body')
    def translate_body(body):
        """Gövde türünü Türkçeye çevir"""
        return BODY_TRANSLATIONS.get(body.lower(), body)

    @app.template_filter('translate_type')
    def translate_type(alcohol_type):
        """Alkol türünü Türkçeye çevir"""
        return TYPE_TRANSLATIONS.get(alcohol_type.lower(), alcohol_type)

    @app.template_filter('translate_subtype')
    def translate_subtype(subtype):
        """Alkol alt türünü Türkçeye çevir"""
        return SUBTYPE_TRANSLATIONS.get(subtype.lower(), subtype)

    @app.template_filter('translate_region')
    def translate_region(region):
        """Bölge/ülke ismini Türkçeye çevir"""
        return REGION_TRANSLATIONS.get(region.lower(), region)

    @app.template_filter('translate_cuisine')
    def translate_cuisine(cuisine):
        """Şöğün türünü Türkçeye çevir"""
        return CUISINE_TRANSLATIONS.get(cuisine.lower(), cuisine)


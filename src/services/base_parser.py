import aiohttp

class BaseParser:
    BASE_URL: str = ""
    TOKEN_PATH: str = ""
    CITY_PATH: str = ""
    CATEGORY_PATH: str = ""
    HEADERS: dict = {}
    
    def __init__(self, base_url: str, token_path: str, city_path: str, category_path: str) -> None:
        self.BASE_URL = base_url
        self.TOKEN_PATH = token_path
        self.CITY_PATH = city_path
        self.CITY_PATH = city_path
        self.CATEGORY_PATH = category_path

    def set_headers(self) -> None:
        pass

    def get_token(self) -> str:
           return ""

    def get_cities_list(self) -> list[str]:
        return []

    def get_categories_list(self) -> list[str]:
        return []

    def get_products_by_category(self, category_id: int) -> list:
        return []

    def update_products_info(self) -> None:
        cities = get_cities_by_store_name("some store name")
        categories = get_categories_by_store("some store name")
        products_by_cities = []
        for city in cities:
            products_by_cities.append(get_products(categories, city))


            
        # нужно сходить в базу за данными по продуктам в магазине
        # пройтись по каждой категории и с агрегировать продукты отнсительно словаря из бд для данного магазина
        # внести полученные данные в бд

        # На каждый обход создавать сессию, мб передавать её из точки входа
        # На каждый обход получать новый токен
        # Нужен какой-то дата класс для агрегации, мб использовать pydentic
        #
        #
        pass




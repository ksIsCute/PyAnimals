import requests

__version__ = '0.1.0'
        
class animal:
    animals = ["dog", "cat", "raccoon", "panda", "kangaroo", "koala", "fox", "bird"]
    
    def __check_animal(animal):
        if animal.lower() not in animals:
            raise AttributeError("The animal given doesnt exist! Make sure the animal you want an fact of is in the respected queries!")
            
    def __get_animal(animal):
        self.__check_animal(animal)
        
        link = requests.get(f"https://some-random-api.ml/animal/{animal}")
        json = link.json()
        return json
        
    def fact(animal):
        return self.__get_animal(animal)["fact"]
    
    def picture(animal: str):
        return self.__get_animal(animal)['image']

import requests

__version__ = '0.1.0'

class animal:
    def fact(animal):
        if animal.lower() not in ["dog", "cat", "raccoon", "panda", "kangaroo", "koala", "fox", "bird"]:
            raise AttributeError("The animal given doesnt exist! Make sure the animal you want an fact of is in the respected queries!")
        
        animallink = requests.get(f"https://some-random-api.ml/animal/{animal}")
        animaljson = animallink.json()
        return animaljson['fact']
    def picture(animal: str):
        if animal.lower() not in ["dog", "cat", "raccoon", "panda", "kangaroo", "koala", "fox", "bird"]:
            raise AttributeError("The animal given doesnt exist! Make sure the animal you want an image of is in the respected queries!")
        animallink = requests.get(f"https://some-random-api.ml/animal/{animal}")
        animaljson = animallink.json()
        return animaljson['image']

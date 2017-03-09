import requests
from pprint import pprint
def main():
    response = requests.get("http://localhost:5000/universities")
    universities = response.json()
    pprint(universities)

if __name__ == '__main__':
    main()

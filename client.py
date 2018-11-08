import requests

inputs = {
    "a": [2, 4],
    "b": [5, 6],
}

r = requests.post("vcm-7311.vm.duke.edu:5000/distance", json = inputs) # maybe no 5000

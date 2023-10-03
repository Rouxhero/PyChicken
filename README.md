#PyChicken
Little WebFramework With CherryPy

# Author
Rouxhero


# Installation

## Requirements
Run this command on root:
`pip3 install -r requirements.txt`

# How to use
Nothing more than this :
`python3 -B main.py`

> The option `-B` avoid the generation of all \__pycache__ directory


## Dev
# Request TODO
### Add Route

Open [app/route/web.py](app/route/web.py) and add routes here : 
```py
# ...


web_routes = [
    Route('/', 'GET', indexController,'index'),
    Route('/about', 'GET', indexController,'about_page'),
    # Add your routes here
]

# You can also create an other list
my_routes = [
    # also Add your routes here
]

# But add it to web_routes !
web_routes += my_routes
```

from controller.controller_player import add_new_player
from model.player import Players
from view.cli.view_menu import menu_navigation

menu = []
while menu != [5]:
    menu_navigation(menu)

print("Au revoir !")

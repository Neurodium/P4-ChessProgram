from view.cli.view_tournament import tournament_menu, tournament_menu_back, tournament_menu_create

def menu_navigation(list):
    if list == []:
        start_menu(list)
    elif list == [1]:
        tournament_menu(list)
    elif list == [1, 1]:
        tournament_menu_create(list)
    elif list == [1, 4]:
        tournament_menu_back(list)


"""Menu de départ"""


def start_menu(list):
    menu0 = input("""                                          =||=
                         o   |\ ,'`. /||\ ,'`. /|    o
 _   _   _   |\__      /\^/\ | `'`'`' || `'`'`' |  /\^/\   |\__     _   _   _
| |_| |_| | /   o\__  |  /  ) \      /  \      /  |  /  ) /   o\__ | |_| |_| |
 \       / |    ___=' | /  /   |    |    |    |   | /  / |    ___=' \       /
  |     |  |    \      Y  /    |    |    |    |    Y  /  |    \      |     |
  |     |   \    \     |  |    |    |    |    |    |  |   \    \     |     |
  |     |    >    \    |  |    |    |    |    |    |  |    >    \    |     |
 /       \  /      \  /    \  /      \  /      \  /    \  /      \  /       |
|_________||________||______||________||________||______||________||_________|
    __         __       __       __        __       __       __         __
   (  )       (  )     (  )     (  )      (  )     (  )     (  )       (  )
    ><         ><       ><       ><        ><       ><       ><         ><
   |  |       |  |     |  |     |  |      |  |     |  |     |  |       |  |
  /    \     /    \   /    \   /    \    /    \   /    \   /    \     /    |
 |______|   |______| |______| |______|  |______| |______| |______|   |______|

                    CHESS TOUNRNAMENT V1.0

Que souhaitez-vous faire ?
1. Créer/Modifier/Consulter les tournois
2. Créer/Modifier/Consulter les joureurs
3. Afficher un rapport
4. Sauvegarder/Charger
5. Quitter
 
            """)
    list.append(int(menu0))
    return list




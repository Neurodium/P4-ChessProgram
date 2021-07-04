

"""Menu de départ"""


def menu_start(list):
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
2. Créer/Modifier/Consulter les joueurs
3. Afficher un rapport
4. Sauvegarder/Charger
5. Quitter
 
""")
    list.append(int(menu0))
    return list




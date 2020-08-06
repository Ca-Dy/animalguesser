#Devineur d'animaux
import webbrowser
#Règles
print("les règles du jeu sont simples: y = oui | n = non")
def choix_(a):
    b = input(a)
    if b == "y":
        return True
    else:
        return False
def fin():
    print("merci d'avoir joué")
#Fonctions
def poilu():
    if choix_("ton animal a t-il des poils?  ") == True:
        return True
    else:
        return False

def os():
    if choix_("ton animal préfère t-il les os?  ") == True:
        return True
    else:
        return False

def poisson():
    if choix_("ton animal aime t-il le lait et le poisson?  ") == True:
        return True
    else:
        return False

def plumes():
    if choix_("ton animal a t-il des plumes?  ") == True:
        return True
    else:
        return False

def parrot():
    if choix_("ton animal répète-il ce que tu dis?  ") == True:
        return True
    else:
        return False

#MainLoop
if poilu() == True:
    if os() == True:
        print("ton animal est un chien!")
        if choix_("veux tu savoir ce qu'est un chien?  ") == True:
            try:
                webbrowser.open("https://fr.wikipedia.org/wiki/Chien")
                fin()
                quit()
            except:
                print("le module webbrowser n'est pas installé -_-")
                fin()
                quit()
        else:
            fin()
            quit()
    elif poisson() == True:
        print("ton animal est un chat")
        if choix_("veux tu savoir ce qu'est un chat?  ") == True:
            try:
                webbrowser.open("https://fr.wikipedia.org/wiki/Chat")
                fin()
                quit()
            except:
                print("le module webbrowser n'est pas installé -_-")
                fin()
                quit()
        else:
            fin()
            quit()
elif plumes() == True:
    if parrot() == True:
        print("ton animal est un perroquet")
        if choix_("veux tu savoir ce qu'est un perroquet?  ") == True:
            try:
                webbrowser.open("https://fr.wikipedia.org/wiki/Perroquet")
                fin()
                quit()
            except:
                print("le module webbrowser n'est pas installé -_-")
                fin()
                quit()
        else:
            fin()
            quit()
    else:
        print("je n'ai pas trouvé")
        fin()
        quit()
else:
        print("je n'ai pas trouvé")
        fin()
        quit()

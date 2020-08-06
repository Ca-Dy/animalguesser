#Devineur d'animaux entre chat, chien et perroquet
#CABELLO Dylan 
try:
    import webbrowser
except ModuleNotFoundError:
    print("Impossible d'importer le module webbrowser")
    webbrowser = None
#Règles
print("les règles du jeu sont simples: y = oui | n = non")
def choix_(a):
    b = input(a)
    return b == "y"

def fin():
    print("merci d'avoir joué")
#Fonctions
def poilu():
    return bool(choix_("ton animal a t-il des poils?  "))

def os():
    return bool(choix_("ton animal préfère t-il les os?  "))

def poisson():
    return bool(choix_("ton animal aime t-il le lait et le poisson?  "))

def plumes():
    return bool(choix_("ton animal a t-il des plumes?  "))
def parrot():
    return bool(choix_("ton animal répète-il ce que tu dis?  ")) 

#MainLoop
if poilu():
    if os():
        print("ton animal est un chien!")
        if webbrowser and choix_("veux tu savoir ce qu'est un chien?  "):
            webbrowser.open("https://fr.wikipedia.org/wiki/Chien")
    elif poisson():
        print("ton animal est un chat")
        if webbrowser and choix_("veux tu savoir ce qu'est un chat?  "):
            webbrowser.open("https://fr.wikipedia.org/wiki/Chat")
elif plumes():
    if parrot():
        print("ton animal est un perroquet")
        if webbrowser and choix_("veux tu savoir ce qu'est un perroquet?  "):
            webbrowser.open("https://fr.wikipedia.org/wiki/Perroquet")
else:
    print("je n'ai pas trouvé")
fin()
quit()

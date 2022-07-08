#Forum en ligne de patisserie: Gateau
#les utilisateurs doivent:
    #s'inscrire
    #parler de gateau preferes
    #repondre a des messages dans des fils existants

#fil de discussion: titre, date de creation, collection de post
#post: texte, utilisateur qui publie, date de publication, a un fichier attaché
#utilisateur: s'inscrit, parle de gateau prefere, repondre à des message de discussion, attacher des fichiers à leur posts,
#il y a plusieurs types de fichier / image
#utilisateur moderateur: modifier un post, supprimer ceux qui ne parlent pas de gateau

class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def SePresenter(self):
        pass

class Utilisateur(Personne):
    def __init__(self, identifiant, mot_de_pass):
        super(Utilisateur, self).__init__(nom, age)
        self.identifiant = identifiant
        self.mot_de_pass = mot_de_pass

    def Sinscrire(self):
        self.identifiant = input("Entrer votre identifiant: ")
        self.mot_de_pass = input("Entrer votre mot de pass")

    def RepondreAuMessage(self):
        pass

class Moderateur(Utilisateur):
    pass

class Fichier():
    pass






class Post():
    def __init__(self, contenu_message, date_de_publication, fichier_attache):
        self.contenu_message = contenu_message
        self.date_de_publication = date_de_publication
        self.fichier_attache = fichier_attache



    def EstPublie(self):
        pass






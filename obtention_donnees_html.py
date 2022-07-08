#Récupérer du titre de la page HTML
soup.title
#<title><Les chiens les plus mignons></title>

#Récupération de la chaîne de caractères du titre HTML
soup.title.string

#Trouver tous les éléments avec la balise <a>
soup.find_all('a')

#Trouver les éléments avec l'id du "lien1"
soup.find(id="lien1")

#Trouver tous les éléments p avec la cmasse "title"
soup.find_all("p", class_="title")
git init - permet d'initialiser le répertoire sur la machine local
git remote add origin git@github.com:xxxx/yyy.git - permet de créer la liaison avec github

git add fihcier.extension - ajoute le fichier dans la staging area
git commit -m - ajoute un commentaire
git push -u origin main - pousse vers le serveur github


# Création de la nouvelle branche
git branch une_branche

# On se place sur la nouvelle branche
git checkout une_branche

# Une fois fait on pousse cette nouvelle branche sur notre dépôt distant
git push -u origin une_branche

# Notre branche faite, on peut créer notre nouveau fichier texte
nano fichier_2.txt

# On le remplit avec du texte au choix, puis on l'ajoute au prochain commit
git add fichier_2.txt

# On commit puis on push
git commit -m "ajout de fichier_2.txt sur une nouvelle branche"

# Toujours sur la branche
git push
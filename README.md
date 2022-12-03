# Projet_python_final
Projet python de fin de semestre pour le cours de python for Data Analysis

Vous trouverez dans ce dépôt l'intégralité des travaux que nous avons réalisés sur le dataset Drug consumption (quantified) 
https://archive.ics.uci.edu/ml/datasets/Drug+consumption+%28quantified%29

Notre problématique de notre étude est la suivante : Comment assurer la prédiction du risque de consommation de drogues d'un individu lambda selon les variables explicatives présentes ?

Dans le fichier Projet_Python2023, nous avons réalisé les étapes liées à l'appropriation des données, ayant permis de mettre en avant plusieurs visualisations afin de comprendre le dataset dans son ensemble et de définir différentes méthodes à suivre pour mieux approcher le sujet. La première a donc été de créer 3 nouveaux datasets qui représentent les 3 grandes classes de drogues dangereuses (hallucinogènes, stimulants ,dépresseurs).

Par la suite, les différentes phases de data preprocessing et de data scaling ont été exécutées et ont permis dans un premier temps de définir l'ensemble des variabes explicatives à garder et de pouvoir tester dans un second temps les différents modèles (Regression Logistique, KNN , Random Forest).
Cela nous permet donc d'identifier le meilleur modèle de prédiction pour les 3 datasets. 

Au final, les modèles KNN et Random Forest se sont avérés être les plus performants sur l'ensemble des datasets. En analysant les résultats sortis par le module lazy predict sur les datasets notre choix s'est porté sur le modèle KNN.

Dans le fichier final_model, nous avons créé les modèles KNN finaux en utilisant le module pipeline et nous les avons enfin exporté en format pickle. 
Cela nous permet donc de créer une API Flask au sein duquel l'utilisateur retrouvera un formulaire d'informations à remplir afin de recevoir les résultats de prédiction issues de nos modèles.

Enfin, l'utilisateur a à sa disposition un dashboard qui met en avant différentes visualisations dynamiques liées au dataset.



# Travaux Pratiques de cryptographie
## Exercice 1 : Découverte des fonctions de hachage (MD5 et SHA-1)
### 1.2 Travail à réaliser
#### Question 1.1
Les deux types de hash (MD5 et SHA-1) n'ont aucune ressemblance visuelle alors que les entrées sont différentes que d'un seul caractère.
Ces fonctions sont extrêmement sensibles aux petites modifications, c'est ce qu'on appelle l'effet avalanche.
#### Question 1.2
Peu importe la taille de l'entrée, MD5 renvoie toujours 128 bits et SHA-1 renvoie 160 bits. Les fonctions de hachages compressent les données en une sortie de taille fixe.
#### Question 1.3
Si on modifie le texte, le hash sera complètement différent. Comme vu dans la question 1.1, c'est l'effet avalanche.
#### Question 1.4
MD5 et SHA-1 sont considérés comme non sécurisés à cause de vulnérabilités comme :
- les collisions : deux entrées différentes peuvent produire le même hash.
- les attaques par force brute : il est possible de retrouver l'entrée originale à partir du hash.
Aujourd'hui on peut trouver des alternatives comme SHA-256.
#### Question 1.5
Une fonction de hachage salée ajoute une valeur aléatoire (le sel) à l'entrée avant de la hacher. Elle empêche les attaques par tables de hachage précalculées (rainbow tables).
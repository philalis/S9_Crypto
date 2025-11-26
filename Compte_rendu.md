# Rapport TP1 Cryptographie

## Exercice 1
### Question 1.1
...
### Question 1.5
Une fonction de hachage salée ajoute, à la fin du texte à hacher, des caractères.  
Le but est que plusieurs textes identiques aient des haches différents.  
C'est utilisé par exemples pour la gestion de mot de passe, où l'on stocke le hache du mot de passe ainsi que le sel utilisé.


## Exercice 2

### Q 2.1
certificat github.com :  
- Émetteur : Sectigo ECC Domain Validation Secure Server CA
- Sujet : github.com
- Période de validité (Not Before / Not After) :  
  Not Before : Wed, 05 Feb 2025 00:00:00 GMT  
  Not After : Thu, 05 Feb 2026 23:59:59 GMT 
- Clé publique et algorithme associé
  - Public key : 04:20:34:5C:46:FF:2C:CB:F8:24:9A:AE:F0:BB:2F:77:A9:1F:97:21:36:71:BA:C2:26:18:C5:1E:43:FD:9D:49:E0:CC:46:9C:85:FC:29:B4:F9:7C:28:0B:A3:2C:C7:5C:BF:6F:E7:46:DD:04:8A:BA:CB:80:2D:37:88:0D:EE:06:D6
  - Algorithme : Elliptic Curve

### Q2.2



    



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
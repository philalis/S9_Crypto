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
## Exercice 2 : Analyse d'un certificat numérique
### 2.2 Travail à réaliser
#### Question 2.1
certificat github.com :  
- Émetteur : Sectigo ECC Domain Validation Secure Server CA
- Sujet : github.com
- Période de validité (Not Before / Not After) :  
  Not Before : Wed, 05 Feb 2025 00:00:00 GMT  
  Not After : Thu, 05 Feb 2026 23:59:59 GMT 
- Clé publique et algorithme associé
  - Public key : 04:20:34:5C:46:FF:2C:CB:F8:24:9A:AE:F0:BB:2F:77:A9:1F:97:21:36:71:BA:C2:26:18:C5:1E:43:FD:9D:49:E0:CC:46:9C:85:FC:29:B4:F9:7C:28:0B:A3:2C:C7:5C:BF:6F:E7:46:DD:04:8A:BA:CB:80:2D:37:88:0D:EE:06:D6
  - Algorithme : Elliptic Curve
#### Question 2.2
Une autorité de certification (CA) est une entité de confiance qui émet des certificats numériques. Elle vérifie l'identité des entités (personnes, organisations, sites web) avant de leur délivrer un certificat. Le rôle principal d'une CA est d'assurer la sécurité des communications en ligne en garantissant que les parties impliquées sont bien celles qu'elles prétendent être. Dans une KPI, le CA vérifie l'identité des utilisateurs et des appareils avant de leur attribuer des certificats numériques, ce qui permet d'établir des connexions sécurisées au sein de l'organisation.
#### Question 2.3
La chaîne de certification est une hiérarchie de certificats numériques qui permet de vérifier l'authenticité d'un certificat donné. Elle commence par le certificat de l'entité finale (par exemple, un site web) et remonte jusqu'à une autorité de certification racine de confiance. Chaque certificat dans la chaîne est signé par l'autorité de certification qui l'a émis, créant ainsi une relation de confiance entre les certificats. Lorsqu'un navigateur ou une application reçoit un certificat, il peut suivre cette chaîne pour s'assurer que le certificat est valide et digne de confiance.
#### Question 2.4
Lorsqu'un certificat est révoqué, cela signifie qu'il n'est plus considéré comme valide avant sa date d'expiration. Les raisons courantes de révocation incluent la compromission de la clé privée associée au certificat, des erreurs dans les informations du certificat, ou si l'entité à laquelle le certificat a été délivré n'est plus digne de confiance. La révocation est généralement gérée par l'autorité de certification qui a émis le certificat, et les informations sur les certificats révoqués sont publiées dans des listes de révocation de certificats (CRL) ou via le protocole OCSP (Online Certificate Status Protocol).
#### Question 2.5
Les extensions de certificat sont des champs supplémentaires dans un certificat numérique qui fournissent des informations supplémentaires sur le certificat ou imposent des contraintes sur son utilisation. Elles peuvent inclure des informations telles que les usages autorisés du certificat (par exemple, authentification de serveur, signature de code), les politiques de certification, les identifiants alternatifs du sujet, et d'autres données pertinentes. Les extensions permettent de personnaliser les certificats pour répondre à des besoins spécifiques et d'améliorer la sécurité et la gestion des certificats.
#### Question 2.6
Un certificat auto-signé est un certificat numérique qui est signé par la même entité qui l'a émis, plutôt que par une autorité de certification (CA) de confiance. Cela signifie que l'entité qui utilise le certificat est responsable de sa propre validation. Les certificats auto-signés sont souvent utilisés pour des tests internes, des environnements de développement, ou des applications où la confiance externe n'est pas nécessaire. Cependant, ils ne sont pas considérés comme fiables pour les communications publiques, car ils ne bénéficient pas de la validation d'une CA reconnue.
## Exercice 3 : Cryptanalyse du chiffre de Vigenère
### 3.4 Travail à réaliser
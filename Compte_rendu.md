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
### Question 3.1 
On trouve un indice de cohérence de 0.0457.  
On peut en déduire qu'il ne s'agit pas d'un cryptage par code de César, sinon l'IC aurait été proche de 0.0778 (référence pour un texte en français).
### Question 3.2
On trouve que la longueur de la clé serait de 21 (IC le plus proche de la valeur de référence).  
En regardant les valeurs d'ICs pour les longueurs 3 et 7, on peut supposer que la clé est de longueur 7 (3 à un mauvais IC, et 7 à un IC proche de celui de référence).
### Question 3.3 
Pour une clé de 7 caractères, on trouve `ENSEAIS` comme clé.
### Question 3.4
Message décodé : 
``FELICITATIONS POUR AVOIR TROUVE LA CLE DE CHIFFREMENT VOUS AVEZ REUSSI CET EXERCICE DE CRYPTOGRAPHIE FELICITATIONS ENCORE UNE FOIS POUR VOTRE TRAVAIL REMARQUABLE VOUS AVEZ FAIT PREUVE DE PERSEVERANCE ET DE LOGIQUE POUR DECODER CE MESSAGE SECRET BRAVO POUR VOTRE DETERMINATION LA CRYPTOGRAPHIE EST UN ART ANCIEN QUI REMONTE A L ANTIQUITE FELICITATIONS VOUS MAITRISEZ MAINTENANT LES BASES DU CHIFFREMENT DE VIGENERE CE SYSTEME A ETE INVENTE AU SEIZIEME SIECLE BRAVO POUR AVOIR PERCE CE MYSTERE LA CRYPTANALYSE DEMANDE DE LA PATIENCE FELICITATIONS VOUS AVEZ LES COMPETENCES NECESSAIRES POUR CONTINUER DANS CETTE VOIE BRAVO ENCORE``
### Question 3.5
L'indice de coïncidence est un bon outils pour attaquer un texte, car cela utilise les "faiblesses" (ou les habitudes) des langues. Cette attaque s'appuie sur le fait que certaines lettres sont plus utilisées que les autres.
### Question 3.6
La méthode de Kasiski constiste à rechercher des répétitions dans le texte codé. Il est alors très probable que les répétitions viennent de répétitions dans le texte non codé, espacées d'un multiple de la clé.
On en déduit alors la longeur de la clé.
On utilise ensuite l'IC pour connaitre les valeurs dans la clé.
### Question 3.7
Pour avoir un "One time pad" qui garantit la confidentialité des données, il faut un pad de la longueur du texte à transmettre.
### Question 3.8
L'inconvénient est que cette clé est très longue.
### Question 3.9 
On ne peut réemettre un message avec la même clé, sinon on pourrait faire une attaque avec les méthodes précédentes.  
(Cela revient à avoir un texte initial plus long, avec la clé qui se répète.)

## Exercice 4 : Exploration de la blockchain Bitcoin
### 4.4 Questions
#### Question 4.1
Les éléments principaux d'un bloc Bitcoin sont :
- En-tête du bloc (Block Header) : contient des informations telles que le hash du bloc précédent, le hash du Merkle root, le timestamp, la difficulté de la preuve de travail, et le nonce.
- Transactions : une liste de toutes les transactions incluses dans le bloc.
- Taille du bloc : la taille totale du bloc en octets.
#### Question 4.2
La taille moyenne d'un bloc Bitcoin est d'environ 1 Mo (mégaoctet). Cependant, avec l'implémentation de SegWit (Segregated Witness), la taille effective peut être plus grande en fonction de la manière dont les transactions sont structurées.
#### Question 4.3
En moyenne un bloc peut contenir entre 2000 et 3000 transactions, mais ce nombre peut varier en fonction de la taille des transactions individuelles.
#### Question 4.4
Champs présents dans l'en-tête d'un bloc Bitcoin :
- Version : indique la version du protocole Bitcoin utilisée.
- Hash du bloc précédent : référence au bloc précédent dans la chaîne.
- Merkle Root : le hash racine de l'arbre de Merkle des transactions dans le bloc.
- Timestamp : l'heure à laquelle le bloc a été miné.
- Bits : la difficulté de la preuve de travail.
- Nonce : un nombre utilisé pour la preuve de travail.
#### Question 4.5
Le rôle du champ "Previous Block Hash" est de lier chaque bloc au bloc précédent dans la chaîne de blocs (blockchain). Cela crée une structure en chaîne où chaque bloc dépend du précédent, assurant ainsi l'intégrité et la sécurité de la blockchain. Si un bloc est modifié, le hash du bloc change, ce qui invalide tous les blocs suivants, rendant toute tentative de falsification facilement détectable.
#### Question 4.6
Le champ "Nonce" est un nombre arbitraire utilisé dans le processus de preuve de travail (Proof of Work) pour miner un bloc. Les mineurs ajustent le nonce pour trouver un hash du bloc qui satisfait les conditions de difficulté spécifiées (c'est-à-dire, un hash inférieur à une certaine valeur cible). Le nonce est essentiel pour permettre aux mineurs de varier le hash du bloc jusqu'à ce qu'ils trouvent une solution valide, ce qui garantit la sécurité et la décentralisation du réseau Bitcoin.
#### Question 4.7
Etapes de création d'un nouveau bloc Bitcoin :
1. Collecte des transactions : les mineurs rassemblent les transactions non confirmées dans un pool de transactions.
2. Construction du bloc : les mineurs créent un nouveau bloc en incluant les transactions sélectionnées et en préparant l'en-tête du bloc.
3. Calcul du Merkle Root : les mineurs calculent le Merkle root des transactions incluses dans le bloc.
4. Preuve de travail : les mineurs ajustent le nonce et recalculent le hash du bloc jusqu'à ce qu'ils trouvent un hash qui satisfait les conditions de difficulté.
5. Diffusion du bloc : une fois qu'un mineur trouve un bloc valide, il le diffuse au réseau.
6. Validation par les nœuds : les autres nœuds du réseau vérifient le bloc et l'ajoutent à leur copie de la blockchain.
7. Récompense du mineur : le mineur qui a trouvé le bloc valide reçoit une récompense en bitcoins et les frais de transaction associés.
#### Question 4.8
Le minage dans le réseau Bitcoin est le processus par lequel de nouveaux blocs sont ajoutés à la blockchain. Les mineurs utilisent la puissance de calcul pour résoudre des problèmes mathématiques complexes (preuve de travail) afin de trouver un hash valide pour un nouveau bloc. Ce processus sécurise le réseau en rendant difficile la modification des blocs existants, car cela nécessiterait de recalculer les preuves de travail pour tous les blocs suivants. Le minage permet également de valider les transactions et d'émettre de nouveaux bitcoins en récompense aux mineurs pour leurs efforts.
#### Question 4.9
La difficulté de minage dans le réseau Bitcoin est ajustée toutes les 2016 blocs (environ toutes les deux semaines) pour maintenir un temps moyen de création de bloc d'environ 10 minutes. Si les blocs sont minés plus rapidement que prévu, la difficulté augmente, rendant le minage plus difficile. Inversement, si les blocs sont minés plus lentement, la difficulté diminue. Cet ajustement automatique garantit que la production de nouveaux blocs reste stable malgré les variations de la puissance de calcul du réseau.
#### Question 4.10
Le hash d'un bloc valide doit contenir un certain nombre de zéros au début, en fonction de la difficulté actuelle du réseau. Par exemple, si la difficulté est élevée, le hash doit commencer par plusieurs zéros, ce qui rend la recherche d'un hash valide plus difficile. Le nombre exact de zéros requis varie en fonction de la difficulté, mais l'objectif est de s'assurer que le hash est inférieur à une valeur cible spécifique définie par le protocole Bitcoin.
#### Question 4.11
La première récompense pour le minage d'un bloc Bitcoin, connue sous le nom de "block reward", était de 50 bitcoins par bloc. Cependant, cette récompense est réduite de moitié tous les 210 000 blocs (environ tous les quatre ans) dans un processus appelé "halving".
#### Question 4.12
La particularité du bloc genesis (le premier bloc de la blockchain Bitcoin) est qu'il a été créé par le créateur de Bitcoin, Satoshi Nakamoto, le 3 janvier 2009. Ce bloc ne fait pas référence à un bloc précédent, car il est le premier de la chaîne. De plus, le bloc genesis contient un message caché dans son coinbase (la première transaction du bloc) qui fait référence à un article de journal intitulé "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks", soulignant la motivation derrière la création de Bitcoin en réponse à la crise financière de 2008.
#### Question 4.13
Le message inscrit dans le bloc genesis est : "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks". Ce message fait référence à un article de journal publié le jour de la création du bloc genesis, soulignant la situation économique de l'époque et la motivation derrière la création de Bitcoin en tant que système financier alternatif.
#### Question 4.14
Le premier halving a eu lieu sur le bloc 210 000, qui a été miné le 28 novembre 2012. 
#### Question 4.15
Lors de ce halving, la récompense pour le minage d'un bloc est passée de 50 bitcoins à 25 bitcoins.
#### Question 4.16
Un halving se produit tous les 210 000 blocs.
#### Question 4.17
A l'aide de la question précédente et sachant qu'un bloc est créé environ toutes les 10 minutes, un halving a lieu environ tous les 4 ans.
#### Question 4.18
A ce jour, il y a eu 4 halvings dans l'histoire de Bitcoin :
1. Premier halving : 28 novembre 2012 (bloc 210 000)
2. Deuxième halving : 9 juillet 2016 (bloc 420 000)
3. Troisième halving : 11 mai 2020 (bloc 630 000)
4. Quatrième halving : 5 novembre 2024 (bloc 840 000)
#### Question 4.19
La récompense actuelle pour le minage d'un bloc Bitcoin, après le quatrième halving, est de 6,25 bitcoins par bloc.
#### Question 4.20
Le dernier bitcoin devrait être miné aux alentours de l'année 2140. Cela est dû au fait que la récompense de minage diminue de moitié tous les 210 000 blocs, et qu'il y a une limite maximale de 21 millions de bitcoins qui peuvent être créés.
#### Question 4.21
Calcul du nombre total maximal de bitcoins qui seront créés :
- Récompense initiale : 50 BTC
- Nombre de halvings : 33 (car 2^33 * 50 BTC = 21 000 000 BTC)
- Série géométrique :
  Total BTC = 50 + 25 + 12.5 + 6.25 + ... jusqu'à 33 termes ;
  Total BTC = 50 * (1 - (1/2)^33) / (1 - 1/2) ;
  Total BTC = 50 * (1 - 1/8589934592) / (1/2) ;
  Total BTC ≈ 21 000 000 BTC ;
Donc, le nombre total maximal de bitcoins qui seront créés est de 21 millions de bitcoins.
#### Question 4.22
Le temps moyen ciblé entre deux blocs dans le réseau Bitcoin est de 10 minutes.
#### Question 4.23
Le protocole Bitcoin ajuste la difficulté de minage toutes les 2016 blocs (environ toutes les deux semaines) pour maintenir un temps moyen de création de bloc d'environ 10 minutes. Si les blocs sont minés plus rapidement que prévu, la difficulté augmente, rendant le minage plus difficile. Inversement, si les blocs sont minés plus lentement, la difficulté diminue. Cet ajustement automatique garantit que la production de nouveaux blocs reste stable malgré les variations de la puissance de calcul du réseau.
#### Question 4.24
La difficulté est ajustée toutes les 2016 blocs pour maintenir un temps moyen de création de bloc d'environ 10 minutes. Si les blocs sont minés plus rapidement que prévu, la difficulté augmente, rendant le minage plus difficile. Inversement, si les blocs sont minés plus lentement, la difficulté diminue. Cet ajustement automatique garantit que la production de nouveaux blocs reste stable malgré les variations de la puissance de calcul du réseau.
#### Question 4.25
Si la puissance de calcul du réseau double, la difficulté de minage augmentera lors du prochain ajustement pour maintenir le temps moyen de création de bloc à environ 10 minutes. Cela rendra le minage plus difficile, car les mineurs devront effectuer plus de calculs pour trouver un hash valide.
#### Question 4.26

# Création d’un serveur LDAP

- Pourquoi est-il pertinent d'attacher des conteneurs à plusieurs réseaux ?

Attacher des conteneurs à plusieurs réseaux est pertinent pour faciliter la communication entre différents services tout en maintenant une isolation entre eux. Cela permet de créer des environnements où certains conteneurs ont des interactions spécifiques avec certains réseaux, 
tout en restant indépendants des autres réseaux. 

- Pourquoi certains ports ne sont pas ouvrable depuis votre utilisateur ?

Les ports inférieurs à 1024 sont des ports réservés pour les services système. L'ouverture de ces ports nécessite des privilèges élevés ou des permissions spécifiques que ne possède pas un utilisateur standard.

# Création d’une application web

- Sur quel couches du modèle OSI peut agir Traefik ?

Traefik agit sur les couches 3 et 4 du modèle OSI. Il fonctionne en tant que proxy inversé.

- Qu'est qu'une ingress (vous pouvez faire le lien avec une ingress Kubernetes), un middleware et un plugin Traefik ?

Une ingress est une configuration qui permet de gérer le trafic entrant dans un cluster. Elle agit comme une porte d'entrée pour le trafic HTTP/HTTPS externe et route ce trafic vers les services appropriés à l'intérieur du cluster. C'est similaire à la notion d'ingress dans Kubernetes, où elle définit les règles pour acheminer le trafic vers les services.

Un middleware est une fonctionnalité de Traefik utilisée pour effectuer des opérations spécifiques sur la requête HTTP entrante ou la réponse. Par exemple, le middleware peut être utilisé pour effectuer une authentification, un chiffrement, la modification d'en-têtes HTTP, etc.

Un plugin Traefik est une extension qui ajoute des fonctionnalités supplémentaires à Traefik. Les plugins peuvent être utilisés pour étendre les fonctionnalités de base de Traefik, comme l'intégration avec d'autres outils, la mise en œuvre de nouvelles fonctionnalités, etc.

- Quelles expressions d'ingress permettent de capter:
1. mondomaine.com/api/* et mondomaine2.fr/api/*
2. tondomaine.com/api/* 

mondomaine.com/api/* et mondomaine2.fr/api/* peuvent être capturés en utilisant des règles d'ingress qui spécifient les domaines à router vers le même service en fonction du chemin /api/* comme par exemple :

```yaml
http:
  routers:
    router1:
      rule: "Host(`mondomaine.com`) || Host(`mondomaine2.fr`) && PathPrefix(`/api`)"
      # Configuration pour rediriger vers le service approprié
```

tondomaine.com/api/* peut être capturé avec une règle d'ingress dédiée spécifiant le domaine à router vers un service particulier en fonction du chemin /api/* cvomme par exemple :

```yaml
http:
  routers:
    router2:
      rule: "Host(`tondomaine.com`) && PathPrefix(`/api`)"
      # Configuration pour rediriger vers le service approprié
```

- Quel peut être l'interet d'utiliser une passerelle HTTP/HTTPS ?

Les passerelles HTTP/HTTPS jouent un rôle crucial dans la gestion et la sécurisation du trafic web. Voici les avantages clés :

Sécurité : Les passerelles HTTP/HTTPS agissent comme une couche de sécurité en permettant le chiffrement du trafic. Elles utilisent des certificats SSL/TLS pour chiffrer les données lors de la transmission sur Internet, assurant ainsi la confidentialité et l'intégrité des données sensibles.

Contrôle d'accès et authentification : Elles fournissent des fonctionnalités pour contrôler l'accès aux ressources web. Elles peuvent mettre en place des mécanismes d'authentification, d'autorisation et de gestion des identités pour restreindre l'accès aux utilisateurs autorisés.

Routage intelligent : Les passerelles peuvent router le trafic vers différents serveurs ou services en fonction de règles prédéfinies, optimisant ainsi les performances et la disponibilité des services.

Répartition de charge : Elles permettent de répartir la charge entre plusieurs serveurs ou instances, équilibrant ainsi la charge pour éviter la surcharge d'un seul serveur et garantir des performances optimales.

Gestion des API : Elles offrent des fonctionnalités avancées pour gérer les API, telles que la transformation des requêtes, la validation des entrées, la gestion des versions, etc.

Surveillance et journalisation : Elles fournissent des fonctionnalités de surveillance du trafic et de journalisation détaillée, permettant de suivre et d'analyser le trafic web pour des raisons de sécurité, de débogage ou de performance.

# Sécurisation du site de test

- Quel élément peut utiliser une application WEB derrière cette passerelle pour déterminer quel employé à envoyer la requête HTTP ?

Pour déterminer quel employé envoie la requête HTTP, une application web derrière la passerelle peut utiliser plusieurs éléments pour identifier l'utilisateur :

Cookies : Les cookies peuvent stocker des informations d'identification de session ou des jetons d'authentification.

En-têtes HTTP : Des en-têtes personnalisés peuvent être utilisés pour transmettre des informations d'identification ou des jetons d'authentification.

Certificats SSL : Dans certains cas, des certificats SSL peuvent être utilisés pour identifier l'utilisateur.

- Comment ajouterez-vous le fameux cadenas vert à ce domaine (Vous pouvez expliquer plusieurs solutions) ?

Pour ajouter le symbole du cadenas vert (signifiant une connexion sécurisée) à un domaine, plusieurs approches sont possibles :

Certificats SSL/TLS : En configurant et en appliquant un certificat SSL/TLS valide sur le serveur web, le cadenas vert peut être affiché pour indiquer que la connexion est sécurisée.

Utilisation de Let's Encrypt : Il est possible de configurer Let's Encrypt pour obtenir des certificats SSL gratuits et les appliquer au domaine.

Configuration de la passerelle : En utilisant la configuration de la passerelle (comme Traefik), il faut spécifier les certificats SSL à utiliser pour les routes spécifiques, permettant ainsi d'afficher le cadenas vert.

- Combien de réseaux docker utilisez-vous et pourquoi ?

Le nombre de réseaux Docker dépend de l'architecture de l'application et des besoins de segmentation du réseau. On peut utiliser plusieurs réseaux Docker pour :

Isoler les services : On peut placer des conteneurs liés à des fonctionnalités similaires dans un réseau spécifique pour limiter la communication non nécessaire entre les services.

Sécurité : La segmentation du réseau peut améliorer la sécurité en limitant la surface d'attaque. Par exemple, les services exposés publiquement peuvent être placés dans un réseau distinct des services internes.

Gestion de trafic : Plusieurs réseaux peuvent être utilisés pour contrôler le flux de trafic entre les différents services, permettant ainsi de définir des politiques de routage précises.
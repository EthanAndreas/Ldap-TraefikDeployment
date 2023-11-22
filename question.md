# Création d’un serveur LDAP

- Attacher des conteneurs à plusieurs réseaux est pertinent pour faciliter la communication entre différents services tout en maintenant une isolation entre eux. Cela permet de créer des environnements où certains conteneurs ont des interactions spécifiques avec certains réseaux, 
tout en restant indépendants des autres réseaux. 

- Les ports inférieurs à 1024 sont des ports réservés pour les services système. L'ouverture de ces ports nécessite des privilèges élevés ou des permissions spécifiques que ne possède pas un utilisateur standard.
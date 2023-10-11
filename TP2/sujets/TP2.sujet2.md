@author scholet @date 10 oct 2023

# 2. Cas pratique : créer les abonnements d'EDF

## 2.1 Note

En entreprise (cela va bien sûr dépendre de plusieurs facteurs), on ne vous adressera probablement jamais ce type de demande :
> _"Crééz une fonction python qui prend en paramètre une consommation électrique et qui renvoie le montant de la facture associé."_

Ce qu'on pourra éventuellement vous demander prendra la forme de cas pratiques ou d'études. Ce sera à vous, compte tenu de vos connaissances et de vos compétences, de déterminer si le langage Python pourra vous aider à venir à bout d'une mission. Dans l'exemple ci-dessous, l'énoncé est en ce sens volontairement concis.

## 2.2 Une mission originale

Pour ce cas pratique, vous prenez la casquette d'un expert en consommation d'énergie. Un client (professionnel ; disons EDF Guadeloupe) fait appel à vous pour concevoir les formules d'abonnement qui lui feront gagner le maximum d'argent. 

EDF souhaite proposer deux abonnements à des tarifs différents à ses clients. Le premier sera un abonnement simple. Le second sera un peu plus élaboré, et qui tire profit du fait que la journée, la demande est plus forte, alors que la nuit, elle l'est moins. 

L'idée de base, comme pour les billets d'avion et les actions en bourse, serait de vendre plus cher quand la demande est plus forte, et de vendre moins cher quand la demande est plus basse. Cependant, l'électricité est produite à un coût constant autour de 10.0001 ct€/kWh.

Le client vous indique (sans davantage de détails) que la région PACA a une consommation électrique comparable à celle de la Guadeloupe, en particulier en 2022.

**Votre mission est de proposer des tarifs pour faire en sorte que la facture moyenne de l'option base couvre au moins 99% du coût de revient de l'électricité.**
 

# Disclaimer

L'auteur de ces exercices n'a aucun lien avec EDF/EDF Guadeloupe et n'a pas été autorisé ou encouragé à produire ce sujet par eux. Le sujet a un unique objectif pédagogique pour l'enseignement de Python. Toute ressemblance avec des situations réelles serait purement fortuite.
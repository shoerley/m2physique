

# Complétez avec les valeurs correctes
ABO_HPHC = 10
ABO_BASE = 9
TARIF_CONSO_BASE_CTEKWH = 14.7412
TARIF_CONSO_HP_CTEKWH = 15.7412
TARIF_CONSO_HC_CTEKWH = 13.7412


def calculer_prix_hphc(conso):
	# Supprimez le "pass" si vous implémentez cette fonction
	pass

	# Calculez le tarif des consommations en HP et en HC
	# tarif_hp = ...
	# tarif_hc = ...

	# retournez le montant de la facture, conso et abonnement inclus
	# return ...

def calculer_prix_conso_base(conso):
	# On DIVISE par 100 parce que le tarif est donné en centimes
	return ABO_BASE + conso * TARIF_CONSO_BASE_CTEKWH / 100


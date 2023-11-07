
def days_in_month(month, year=2024):
	# Exo 2.
	# Année de référence, connue pour être valablement une année bissextile
	# Une année quelconque "year" est bissextile ssi la différence entre cette année et l'année de référence est divisible par 4
	valid_bissextile_year = 2024
	is_year_bissextile = abs(valid_bissextile_year - year) % 4 == 0

	# Dès lors, on sait si l'année passé en paramètre est bissextile ou non. A noter que ce n'est pas du python ...
	# ... mais de la logique, voir le a. dans le sujet du TP0.

	# Les mois à 31 jours sont les mois 1, 3, 5, 7, 8, 10, 12
	# Le mois 2 a 29 jour si année bissextile, 28 sinon
	# Les autres mois ont 30 jours
	months_31 = [1, 3, 5, 7, 8, 10, 12]

	if month == 0:
		print(f"Le mois {month} n'existe pas. ")
		return None

	if month == 2:
		if is_year_bissextile:
			return 29
		else:
			return 28

	if month in months_31:
		return 31
	else:
		return 30

def seconds_to_hms(input_seconds):
	if input_seconds < 0:
		return None

	hours = input_seconds // (60 * 60)  		# 3600 secondes dans une heure
	minutes = (input_seconds % 3600) // 60	# 60 minutes dans ce qu'il reste d'heures
	seconds = input_seconds % 60  			# Ce qu'il reste de secondes


	# On demandait un formattage précis : HH:mm:ss, donc 5:18:56 n'est pas valide, en revanche 05:18:56 l'est
	hms = f"{format_number(hours)}:{format_number(minutes)}:{format_number(seconds)}"

	print(f"{input_seconds} secondes correspondent à {hms}")

def format_number(number):
	# Ajouter un 0 devant le nombre quand il n'est pas écrit sur deux caractères
	if number < 10:
		return "0" + str(number)
	return str(number)


def run_days_in_month():
	# Test de la fonction pour s'assurer que les résultats sont cohérents pour deux années test
	for month in range(1, 13):
		year = 2024
		nb_days = days_in_month(month, year=year)
		print(f"Le mois {month} en {year} possède {nb_days} jours")

	for month in range(1, 13):
		year = 2023
		nb_days = days_in_month(month, year=year)
		print(f"Le mois {month} en {year} possède {nb_days} jours")

def run_seconds_to_hms():
	# Il est primordial de tester avec des valeurs dont vous pourrez contrôler le résultat

	seconds_to_hms(60*60)					# 1 heure
	seconds_to_hms(60*60*5 + 60*18 + 56)	# 5h + 18min + 56sec

	s = int(input("Quel nombre de secondes voulez vous convertir ? :"))
	seconds_to_hms(s)


run_seconds_to_hms()
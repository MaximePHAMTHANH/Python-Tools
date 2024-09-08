import webbrowser

def extract_and_add_unique_lines(text_file, noms_file):
    # Lire les lignes de text.txt
    with open(text_file, 'r') as file:
        lines = file.readlines()

    # Lire les lignes existantes dans noms.txt
    try:
        with open(noms_file, 'r') as noms_file_obj:
            existing_lines = set(line.strip() for line in noms_file_obj)
    except FileNotFoundError:
        # Si noms.txt n'existe pas encore, on initialise une liste vide
        existing_lines = set()

    # Parcourir les lignes pour trouver celles après chaque "Avatar"
    new_lines = []
    for i in range(len(lines)):
        if lines[i].strip().startswith("Avatar"):
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                # Ajouter la ligne si elle n'existe pas déjà
                if next_line not in existing_lines:
                    new_lines.append(next_line)
                    existing_lines.add(next_line)

    # Si de nouvelles lignes ont été trouvées, on les ajoute à noms.txt
    if new_lines:
        with open(noms_file, 'a') as noms_file_obj:
            for line in new_lines:
                noms_file_obj.write(line + '\n')

    # Afficher les nouvelles lignes ajoutées
    if new_lines:
        print("Lignes ajoutées à noms.txt :")
        for line in new_lines:
            url=(""+line).replace(" ", "")
            print(url)
            webbrowser.open(url)
    else:
        print("Aucune nouvelle ligne à ajouter.")

# Utilisation de la fonction
extract_and_add_unique_lines("text.txt", "noms.txt")


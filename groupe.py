import random

# 1. Préparation des listes
# Background : A à V (22 personnes)
background_info = [chr(i) for i in range(ord('A'), ord('V') + 1)]

# Sans background : w à A14 (18 personnes)
sans_background = ['w', 'x', 'y', 'z'] + [f'A{i}' for i in range(1, 15)]

# Mélange aléatoire
random.shuffle(background_info)
random.shuffle(sans_background)

print("--- RÉPARTITION DES 10 GROUPES (40 PERSONNES) ---\n")

# 2. Formation des 8 premiers groupes (2 Info + 2 Débutants)
for i in range(1, 9):
    membres = [background_info.pop() for _ in range(2)] + [sans_background.pop() for _ in range(2)]
    print(f"Groupe {i:02d} (2+2) : {', '.join(membres)}")

# 3. Formation des 2 derniers groupes (3 Info + 1 Débutant)
for i in range(9, 11):
    membres = [background_info.pop() for _ in range(3)] + [sans_background.pop() for _ in range(1)]
    print(f"Groupe {i:02d} (3+1) : {', '.join(membres)}")


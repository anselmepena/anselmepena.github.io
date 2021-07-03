def trouve_radical(infinitif: str) -> str:
    """
    Renvoie le radical du infinitif pour le conjuguer au futur

    """
    radical = ""
    if infinitif[-2:] == "er":
        irréguliers_er =         ['aller', 'envoyer', 'renvoyer']
        radical_irréguliers_er = ['ir'   , 'enverr' , 'renverr' ]
        if infinitif in irréguliers_er:
            radical = radical_irréguliers_er[irréguliers_er.index(infinitif)]
            return radical
        if infinitif[-3] == 'y':
            if infinitif[-4] == 'a':
                radical = infinitif
                return radical
            radical = infinitif[:-3] + 'i' + infinitif[-2:]
            return radical
        if infinitif[-4:] == "eler" or infinitif[-4:] == "eter":
            irréguliers_eler_eter = ['acheter', 'celer', 'ciseler' , 'démanteler', 'écarteler',
                                     'fureter', 'geler', 'marteler', 'modeler'  ,  'peler'    ]
            if infinitif in irréguliers_eler_eter:
                radical = infinitif[:-4] + "è" + infinitif[-3:]
                return radical
            else:
                radical = infinitif[:-2] + infinitif[-3] + infinitif[-2:]
                return radical
        radical = infinitif
        return radical

    if infinitif[-2:] == "ir" and infinitif[-3] != "o":
        irréguliers_ir =         ["tenir",  "obtenir" , "venir" , "devenir" ,  "prévenir" , "souvenir" , "cueillir"]
        radical_irréguliers_ir = ["tiendr", "obtiendr", "viendr", "deviendr",  "préviendr", "souviendr", "cueiller"]
        if infinitif in irréguliers_ir:
            radical = radical_irréguliers_ir[irréguliers_ir.index(infinitif)]
            return radical
        verbe_ir_perde_i = ["acquérir", "courir", "mourir"]
        if infinitif in verbe_ir_perde_i:
            if infinitif[-4] == "é":
                infinitif = infinitif[:-4] + "e" + infinitif[-3:]
            radical = infinitif[:-2] + "r"
            return radical
        radical = infinitif
        return radical
    
    
    verbe_oir =         ["avoir", "pouvoir", "voir", "recevoir", "savoir", "asseoir", "devoir", "vouloir", "valoir"]
    radical_verbe_oir = ["aur"  , "pourr"  , "verr", "recevr"  , "saur"  , "assoir" , "devr"  , "voudr"  , "vaudr" ]
    
    if infinitif in verbe_oir:
            radical = radical_verbe_oir[verbe_oir.index(infinitif)]
            return radical

    verbe_irrégulier =         ["faire", "être"]
    radical_verbe_irrégulier = ["fer"  , "ser" ]
    if infinitif in verbe_irrégulier:
            radical = radical_verbe_irrégulier[verbe_irrégulier.index(infinitif)]
            return radical
    
    if infinitif[-1] == "e":
        radical = infinitif[:-1]
        return radical
    
def est_pronominal(verbe):
    return verbe[:3] == "se "

terminaisons = ["ai", "as", "a", "ons", "ez", "ont"]
pronoms_personnels = ["Je", "Tu", "Il/Elle/On", "Nous", "Vous", "Ils/Elles"]
pronoms_réfléchis = ["me", "te", "se", "nous", "vous", "se"]

print("Entrez le verbe à conjuguer :",end=" ")
verbe = input().lower()

pronominal = est_pronominal(verbe)

if pronominal:
    radical = trouve_radical(verbe[3:])
else:
    radical = trouve_radical(verbe)

voyelles = "aeiouy"
if radical[0] in voyelles and pronominal == False:
    pronoms_personnels[0] = "J'"
if radical[0] in voyelles:
    for pronom in pronoms_réfléchis:
        if pronom[-1] == "e":
            pronoms_réfléchis[pronoms_réfléchis.index(pronom)] = pronom[0] + "'"

for i in range(6):
    pronom = pronoms_personnels[i]
    terminaison = terminaisons[i]
    pronom_refléchi = ""
    if pronominal: pronom_refléchi = pronoms_réfléchis[i]
    verbe_conjugé = radical + terminaison
    print(pronom, pronom_refléchi, verbe_conjugé, sep=" ")
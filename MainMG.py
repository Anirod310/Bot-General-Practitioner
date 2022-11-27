import csv

#C:/Users/bouse/Desktop/Programmation/Python/GitHub/Projets/3MédecinGénéraliste/BDD MédecinG.csv
#x

def read_file():
    f = open (r"C:/Users/bouse/Desktop/Programmation/Python/GitHub/Projets/3MédecinGénéraliste/BDD MédecinG.csv")
    Reader = csv.reader(f)
    liste = []
    for row in Reader:
        liste.append(row)
    return liste
bdd = read_file()

def matching(answ):
    counter = [0] * (len(bdd[0])-1)
    match_counter = 0
    for elem in answ:
        answer = elem.split()
        for word in answer:
            for i in range(1,11):
                for j in range(1,len(bdd[0])):
                    if bdd[i][j] == word:
                        counter[j-1] += 1
                        match_counter += 1
    if match_counter == 0:
        print(answer)
    return counter

def diagnostic(list_counter):
    most_symptoms = 0
    sickness_index = 0
    for elem in list_counter:
        if elem > most_symptoms:
            most_symptoms = elem
            sickness_index = list_counter.index(elem)
    return sickness_index

def results(n):
    print(f"Votre maladie probable : {bdd[0][n+1]}")
    treatment_index = 1
    for i in range(23,28):
        if bdd[i][n+1] != "None":
            print(f"examen médical {treatment_index} : {bdd[i][n+1]}")
            treatment_index += 1



def main():
    liste = []
    liste.append(input("Hey, je suis la pour vous aider ! Expliquez moi pourquoi vous etes ici : "))
    liste.append(input("Très bien... Avez-vous ressenti autre chose? Ou vous est-il arrivé autre chose depuis? : "))
    liste.append(input("J'ai tout bien pris ! Et sinon, quelle est votre tempéature au thermomètre? : "))
    liste.append(input("Et vos selles? Ont-elles quelque-chose de particulier à citer? : "))
    liste.append(input("Avez-vous constaté une perte de poids depuis? : "))
    liste.append(input("Très bien... Et pour finir, avez-vous un traitement quelconque? Ou prenez-vous des médicaments? : "))
    liste.append(input("Et enfin, avez-vous des allergies ? : "))
    symptoms_counter = matching(liste)
    sickness_index = diagnostic(symptoms_counter)
    results(sickness_index)
    
main()

def main ():
    note1 = int(input('Entrez la première note : '))
    note2 = int(input ('Entrez la deuxième note : '))
    note3 = int(input('Entrez la troisème note : '))

    result = (note1 + note2 + note3)/3
    print('La moyenne de l\'élève est ' + str(result))



if __name__ == "__main__":
    main()
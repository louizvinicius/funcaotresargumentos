nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

def cal_notas(nota1,nota2,nota3):
    media = (nota1+nota2+nota3) / 3
    print("**********\nMedia referente as tres provas: {:.1f}\n**********\n".format(media))

cal_notas(nota1,nota2,nota3)

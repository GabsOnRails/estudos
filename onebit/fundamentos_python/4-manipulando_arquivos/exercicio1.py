# Exercício desenvolvido pelo instrutor e algumas adições que fiz.

'''
Escreva um programa Python para ler as primeiras 'n' linhas de um arquivo.
1-> O nome do arquivo e a quantidade de linhas devem ser passadas via parâmetro na função.
'''
divisoria = "-"
linhas = int(input("Quantas linhas deseja ler: "))
print(divisoria*40)

def file_read_from_line(fname, nlines):
        from itertools import islice # -> método que fatia as strings
        with open(fname, encoding="utf-8") as f:
                for line in islice(f, nlines):
                        print(line)

file_read_from_line('dados/texto.txt',linhas)
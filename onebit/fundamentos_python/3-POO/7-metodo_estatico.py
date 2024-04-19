'''
1 -> Pode acessar a classe, mas não alterar
2 -> Não utiliza o parâmetro da classe
3 -> Usamos o decorator @staticmethod para criar um método estático
'''

class Course:
    def __init__(self,nome,trilha):
        self.nome = nome
        self.trilha = trilha

    @staticmethod
    def cursos_trilha(trilha):
        if trilha == "Python Iniciante":
            cursos = ["Dominando Python", "Módulos e PIP", "POO"]
        elif trilha == "Python Automação":
            cursos = ["Automação de tarefas", "Web Scraping", "ChatBot"]
        else:
            print("A definir..")
        return cursos
    
print(Course.cursos_trilha("Python Automação"))





# O método super é utilizado para não reescrever os atributos da classe pai. Ou seja, não duplicar o código.

class Phone():
    def __init__(self,brand,model_name,price): 
        self._brand = brand # -> Atributos protegidos só podem ser acessados pela classe e sub classe
        self._model_name = model_name
        self._price = price

    def __str__(self):
        return f"{self._brand} - {self._model_name}"

    @staticmethod
    def make_a_call(phone_num):
        print(f"Ligando para {phone_num}")

class Smart_Phone(Phone):
        def __init__(self, brand, model_name, price, ram, internal_memory,back_camera):
             super().__init__(brand, model_name, price)

             self.ram = ram # -> atributos da sub classe
             self.internal_memory = internal_memory
             self.back_camera = back_camera   

moto = Phone("Moto","G-50", 3000)
print(moto)
moto.make_a_call('11 98205-4879')
print(f"Valor do {moto._brand} {moto._model_name} é {moto._price}")
print(vars(moto))

iphone = Smart_Phone("Iphone","13",9000,"8 GB","256 GB","32 MP")
print(iphone)
iphone.make_a_call("21 98456-7829")
print(f"Valor do {iphone._brand} {iphone._model_name} é {iphone._price}")
print(vars(iphone))
 
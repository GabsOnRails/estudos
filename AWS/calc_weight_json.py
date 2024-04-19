'''
Programa usado para analisar os dados JSON e calular o peso dos aminoaciados, baseado no módulo de Python daAWS re/Start.
'''
import jsonFileHandler

data= jsonFileHandler.readJsonFile('/home/felipe/portifolio/Projetos/AWS/insulin.json')
if data != "" :
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))

    # Calculando o peso molecular da insulina
    # Getting a list of the amino acid (AA) weights Obtendo uma lista do peso dos aminoacidos (AA)
    aaWeights = data['weights']
    # Contando o numero de cada aminoacido
    aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in
                       ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W',
                        'Y']})
    # Multiplicando a conta pelo peso
    molecularWeightInsulin = sum({x: (aaCountInsulin[x] * aaWeights[x]) for x in
                                  ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
                                   'V', 'W', 'Y']}.values())
    print("The rough molecular weight of insulin: " +
          str(molecularWeightInsulin))
    print("Percent error: " + str(
        ((molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual) * 100))
else:
    print("Error. Exiting program")

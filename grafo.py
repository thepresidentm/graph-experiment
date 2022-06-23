import networkx as nx
import matplotlib.pyplot as plt

datos = {
    'rosario': {'petroleo':{'weight':6},'tacuba':{'weight':4}},
    'petroleo': {'marzo':{'weight':2},'raza':{'weight':2},'politecnico':{'weight':1}},
    'marzo': {'martin':{'weight':2},'raza':{'weight':2},'indios':{'weight':1}},
    'raza': {'consulado':{'weight':3}},
    'martin':{'consulado':{'weight':3}},
    'consulado':{'oceania':{'weight':3},'morelos':{'weight':2}},
    'oceania': {'azteca':{'weight':11},'pantitlan':{'weight':3},'lazaro':{'weight':3}},
    'pantitlan': {'paz':{'weight':9},'jamaica':{'weight':5},'lazaro':{'weight':6}},
    'morelos': {'lazaro':{'weight':1},'candelaria':{'weight':1}},
    'lazaro': {'candelaria':{'weight':1}},
    'jamaica': {'candelaria':{'weight':2},'anita':{'weight':1}},
    'anita': {'atlalilco':{'weight':6}},
    'atlalilco': {'constitucion':{'weight':4},'tlahuac':{'weight':11},'ermita':{'weight':2}},
    'ermita': {'tasqueña':{'weight':2},'zapata':{'weight':3},'chabacano':{'weight':6}},
    'chabacano': {'anita':{'weight':2},'jamaica':{'weight':1},'pino':{'weight':2}},
    'pino': {'candelaria':{'weight':2}},
    'zapata': {'universidad':{'weight':5},'mixcoac':{'weight':3},'medico':{'weight':4}},
    'mixcoac': {'barranca':{'weight':2}},
    'tacubaya': {'mixcoac':{'weight':3},'observatorio':{'weight':1}},
    'tacuba': {'tacubaya':{'weight':5},'caminos':{'weight':2}},
    'medico': {'chabacano':{'weight':2},'tacubaya':{'weight':3}},
    'balderas': {'medico':{'weight':3},'tacubaya':{'weight':6}},
    'agua': {'pino':{'weight':2},'balderas':{'weight':1},'chabacano':{'weight':3}},
    'hidalgo': {'balderas':{'weight':2},'tacuba':{'weight':7}},
    'guerrero': {'hidalgo':{'weight':1},'buenavista':{'weight':1},'raza':{'weight':2}},
    'garibaldi':{'guerrero':{'weight':1},'morelos':{'weight':3},'artes':{'weight':1}},
    'artes': {'hidalgo':{'weight':1},'agua':{'weight':2},'pino':{'weight':3}}
}

G = nx.from_dict_of_dicts(datos)

nx.draw(G, with_labels=True)
plt.show() 
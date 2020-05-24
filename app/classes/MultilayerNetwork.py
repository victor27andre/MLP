# -*- coding: utf-8 -*-
import numpy as np

#Classe abstrata que representa uma rede multicamada

class MultilayerNetwork(object):
    def __init__(self, input_quantity = 80):
        self.dataset = {"input": np.array([]), "output": np.array([])} #data set que vai ser treinado
        self.hidden_layer_weights = np.array([]) #pesos da camada oculta
        self.input_quantity = input_quantity #quantidade de entradas
        self.hidden_layer_quantity = self.input_quantity #a quantidade de camadas ocultas
        self.weights_quantity = self.input_quantity #quantidades de pesos
        self.weights = np.array([]) # pesos
        self.epoch_quantity = 100000 #epocas
        self.learning_rate = 0.1 #taxa de aprendizagem
        self.momentum = 1
        self.error_rate = None
    
    #Seta os dados de entrada para o treinamento        
    def setDatasetInput(self, data):
        self.dataset["input"] = np.array(data)

    #Seta os dados de saida para o treinamento
    def setDatasetOutput(self, data):
        self.dataset["output"] = np.array(data)

    #Gera os pesos automaticamente
    def generateWeights(self):
        self.hidden_layer_weights = 2 * np.random.random((self.weights_quantity,self.hidden_layer_quantity)) - 1
        self.weights = 2 * np.random.random((self.weights_quantity, 1)) - 1

    #A função de ativação não é definida aqui
    def activationFunction(self, sum):
        pass

    def trainer(self):
        pass

    def test(self, data):
        pass

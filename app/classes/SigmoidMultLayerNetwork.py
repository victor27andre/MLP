# -*- coding: utf-8 -*-

import numpy as np
import ast
import json

from MultilayerNetwork import MultilayerNetwork

#Classe com a rede multicamada com a função sigmoid
class SigmoidMultLayerNetwork(MultilayerNetwork):

    #Função sigmoid (usada na ativação dos neuronios)
    def sigmoid(self, sum):
        return 1 / (1 + np.exp(-sum))

    #Derivada da função sigmoid, utilizada na descida de gradiente
    #descida de gradiente é processo, resumidamente, que elimina o crescimento da
    #taxa de erro
    def sigmoidDerivative(self, sigmoid_result):
        return sigmoid_result * (1 - sigmoid_result)

    #Esse metodo é o da classe MultilayerNetwor que está sendo sobrescrito
    def activationFunction(self, sum):
        return self.sigmoid(sum)

    #Essa função é de treinamento, que realiza o feedforward, descida de gradiente
    #e o backpropagation
    def trainer(self, output_console):

        #gera os pesos aleatórios
        self.generateWeights()
        for epoch in range(self.epoch_quantity):

            input_layer = self.dataset["input"]
            synapse_input_hidden_layer = np.dot(input_layer, self.hidden_layer_weights)
            output_hidden_layer = self.sigmoid(synapse_input_hidden_layer)

            synapse_output_hidden_layer_wieghts = np.dot(output_hidden_layer, self.weights)
            output_layer = self.sigmoid(synapse_output_hidden_layer_wieghts)

            output_error = self.dataset["output"] - output_layer
            output_error_median = np.mean(np.abs(output_error))

            if(epoch % 100 == 0):
                output_console.appendPlainText("Epoca: " + str(epoch) + "\nPorcentagem de erro: " + str(output_error_median) + "\n")

            derivadaSaida = self.sigmoidDerivative(output_layer)
            deltaSaida = output_error * derivadaSaida #delta = erro + derivada do resultado da função self.sigmoid()

            weightsTransposta = self.weights.T
            deltaSaidaXPeso = deltaSaida.dot(weightsTransposta)
            deltaoutput_hidden_layer = deltaSaidaXPeso * self.sigmoidDerivative(output_hidden_layer)

            output_hidden_layerTransposta = output_hidden_layer.T
            pesosNovo1 = output_hidden_layerTransposta.dot(deltaSaida)
            self.weights = (self.weights * self.momentum) + (pesosNovo1 * self.learning_rate)

            input_layerTransposta = input_layer.T
            pesosNovo0 = input_layerTransposta.dot(deltaoutput_hidden_layer)
            self.hidden_layer_weights = (self.hidden_layer_weights * self.momentum) + (pesosNovo0 * self.learning_rate)

        output_console.appendPlainText("Pesos da camada de entrada: ")
        output_console.appendPlainText(np.array2string(self.weights) + "\n")

        output_console.appendPlainText("Pesos das camadas ocultas: ")
        output_console.appendPlainText(np.array2string(self.hidden_layer_weights) + "\n")

        output_console.appendPlainText("Porcentagem de erro: " + str(output_error_median) + "\n")

    #Essa função realiza a classificação
    def test(self, input_data):
        input_data = np.array([input_data])
        sum_synapse_input = np.dot(input_data, self.hidden_layer_weights)
        result_ssi = self.activationFunction(sum_synapse_input)
        sum_synapse_hidden = np.dot(result_ssi,  self.weights)
        result_ssh = self.activationFunction(sum_synapse_hidden)
        return result_ssh
        
    #Essa função salva os pesos dentro de um arquivo json que sera usado na classe principal
    def saveData(self, src_file):
        weights = {
            'hidden_layer': self.hidden_layer_weights.tolist(),
            'input_layer': self.weights.tolist()
        }
        weights_json = json.dumps(weights)
        
        try:
            file_loaded = open("weight.json", "w")
            file_loaded.write(str(weights_json))
            file_loaded.close()

        except Exception as e:
           print("Erro: " + e.message)
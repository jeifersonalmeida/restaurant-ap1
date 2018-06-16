import re

class Client():
    def __init__(self):
        self._firsName = ""
        self._email = ""
        self._evaluation = ""
        self._autoClassification = "Indeterminado"
        self._stars = 0

    def setFirstName(self, name):
        if(name.isalpha()):
            self._firsName = name
            return True
        else:
            return False

    def getFirstName(self):
        return self._firsName

    def setEmail(self, email):
        if not(re.match("[^@]+@[^@]+\.[^@]+", email)):
            return False
        self._email = email
        return True

    def getEmail(self):
        return self._email

    def setEvaluation(self, evaluation):
        self._evaluation = evaluation
        self.setClassification(evaluation)
        return True

    def getEvaluation(self):
        return self._evaluation

    def setClassification(self, evaluation):
        #sumario contendo os adjetivos de classificação com seus respectivos pesos
        sumario = {"horrível": -3, "pessimo": -2, "ruim": -1, "bom": 1, "excelente": 2, "otimo": 3}

        #lista para armazenar os pesos dos adjetivos encontrados na avaliação do cliente
        lstEvaluations = []

        #"purificar" a string de avaliação do cliente
        evaluation = re.sub(u'[^a-zA-Z0-9: ]', ' ', evaluation)

        #separar as palavras em elementos e converter para uma lista
        evaluation = evaluation.split(" ")

        #alimentar a <lstEvaluations>
        for classification in sumario:
            qtt = evaluation.count(classification)
            if(qtt):
                lstEvaluations.append(sumario[classification])

        #gerar a classificação automatica a partir da media dos pesos
        if(len(lstEvaluations) == 0):
            self._autoClassification = "Indeterminado"
        else:
            #media dos pesos
            media = sum(lstEvaluations)/len(lstEvaluations)
            if(media == 0.0):
                self._autoClassification = "Indeterminado"
            elif(media > 0.0):
                self._autoClassification = "Positiva"
            else:
                self._autoClassification = "Negativa"

    def getClassification(self):
        return self._autoClassification

    def setStars(self, stars):
        if(stars < 0 or stars > 5):
            return False
        self._stars = stars
        return True

    def getStars(self):
        return self._stars
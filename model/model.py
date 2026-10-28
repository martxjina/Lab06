from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO
        strumenti = []
        cursore = get_connection.cursor()
        cursore.execute("select * from strumento")
        righe = cursore.fetchall()

        for riga in righe:
            strumento = Strumento(codice=riga[0],
                                  tipo = riga[1],
                                  marca = riga[2],
                                  anno_acquisto= int(riga[3]),
                                  valore=float(riga[4]),
                                  disponibile=riga[5])
            strumenti.append(strumento)

        return strumenti


    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
        cursore = get_connection.cursor()
        cursore.execute("select * from strumento where tipo = ?", (tipo,))
        righe = cursore.fetchall()

        strumenti_di_un_certo_tipo = []

        for riga in righe:
            strumento = Strumento(codice=riga[0],
                                  tipo = riga[1],
                                  marca = riga[2],
                                  anno_acquisto= int(riga[3]),
                                  valore=float(riga[4]),
                                  disponibile=riga[5])
            strumenti_di_un_certo_tipo.append(strumento)

        return strumenti_di_un_certo_tipo




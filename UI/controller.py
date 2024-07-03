import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def fillDD(self):
        for r in self._model.avvistamenti:
            if r.datetime.year not in self._model.anni:
                self._model.anni.append(r.datetime.year)
            if r.shape not in self._model.forme:
                self._model.forme.append(r.shape)
        self._model.anni.sort()
        for a in self._model.anni:
            self._view.ddyear.options.append(ft.dropdown.Option(a))
        for s in self._model.forme:
            self._view.ddshape.options.append(ft.dropdown.Option(s))
    def handle_graph(self, e):
        a = self._view.ddyear.value
        f = self._view.ddshape.value
        self._model.creaGrafo(a,f)
        self._view.txt_result.controls.append(ft.Text(f"Numero di vertici: {self._model.grafo.number_of_nodes()}, "
                                                      f"Numero di archi: {self._model.grafo.number_of_edges()}"))
        for nodo in self._model.grafo.nodes:
            somma = 0
            for n in self._model.grafo.neighbors(nodo):
                somma += int(self._model.grafo[nodo][n]["weight"])
            self._view.txt_result.controls.append(ft.Text(f"Nodo: {self._model.stateMap[nodo].__str__()}, "
                                                          f"somma pesi su archi: {somma}"))
        self._view.update_page()

    def handle_path(self, e):
        dmax, percorso = self._model.cercaPercorso()
        self._view.txtOut2.controls.append(
            ft.Text(f"Il percorso ha distanza massimo --> {dmax},"))
        for n in range(len(percorso)-1):
            print(self._model.grafo[percorso[n]][percorso[n+1]])
            peso = self._model.grafo[percorso[n]][percorso[n+1]]["weight"]
            distanza = self._model.distMap[(percorso[n],percorso[n+1])]
            self._view.txtOut2.controls.append(ft.Text(f"{self._model.stateMap[percorso[n]].__str__()} --> {self._model.stateMap[percorso[n+1]].__str__()},"
                                                      f"peso: {peso}, distanza: {distanza}"))
        self._view.update_page()

    #     def handle_analisi(self,e):
    #         numeroMinimo = self._view.txtCompagnie.value
    #         try:
    #             nm = int(numeroMinimo)
    #         except:
    #             self._view.create_alert("inserire un numero intero!!")
    #             return
    #         if nm < 0 or nm > 13:
    #             self._view.create_alert("Inserire un valore tra 0 e 13.")
    #             return  #
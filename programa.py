class programa: 

    def crear_nom(nom, cognoms):
        """ Concatenar nom i cognoms """
        nom_complet = nom + " " + cognoms
        return nom_complet
        
    def saludar(quiEts): 
        """ Saludar en català """
        salutacio = f"Hola, {quiEts}, que tinguis un bon dia."
        return salutacio


elMeuNom = programa.crear_nom("maria", "merino")
programa.saludar(elMeuNom)
print(elMeuNom)

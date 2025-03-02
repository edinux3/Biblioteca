class Libro:
    def __init__(self):
        self.libros = []

    def agregar(self, titulo, autor, isbn):
        libro = {
            'titulo': titulo,
            'autor': autor,
            'isbn': isbn,
            'disponible': True
        }
        self.libros.append(libro)
        print(f"Libro '{titulo}' agregado exitosamente.")

    def prestar(self, isbn):
        for libro in self.libros:
            if libro['isbn'] == isbn:
                if libro['disponible']:
                    libro['disponible'] = False
                    print(f"Libro '{libro['titulo']}' prestado exitosamente.")
                else:
                    print(f"El libro '{libro['titulo']}' ya está prestado.")
                return
        print("Libro no encontrado.")

    def devolver(self, isbn):
        for libro in self.libros:
            if libro['isbn'] == isbn:
                if not libro['disponible']:
                    libro['disponible'] = True
                    print(f"Libro '{libro['titulo']}' devuelto exitosamente.")
                else:
                    print(f"El libro '{libro['titulo']}' ya está disponible.")
                return
        print("Libro no encontrado.")

    def mostrar(self):
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return
        
        print("\nListado de libros:")
        for libro in self.libros:
            estado = "disponible" if libro['disponible'] else "prestado"
            print(f"Título: {libro['titulo']}")
            print(f"Autor: {libro['autor']}")
            print(f"ISBN: {libro['isbn']}")
            print(f"Estado: {estado}")
            print("-" * 30)

    def buscar(self, isbn):
        for libro in self.libros:
            if libro['isbn'] == isbn:
                estado = "disponible" if libro['disponible'] else "prestado"
                print("\nInformación del libro:")
                print(f"Título: {libro['titulo']}")
                print(f"Autor: {libro['autor']}")
                print(f"ISBN: {libro['isbn']}")
                print(f"Estado: {estado}")
                return
        print("Libro no encontrado.")

def main():
    biblioteca = Libro()
    
    while True:
        print("\nBienvenido al Sistema de Gestión de Biblioteca")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar")
        print("6. Salir")
        
        try:
            opcion = int(input("\nSeleccione una opción: "))
            
            if opcion == 1:
                titulo = input("Ingrese el título del libro: ")
                autor = input("Ingrese el autor del libro: ")
                isbn = input("Ingrese el ISBN del libro: ")
                biblioteca.agregar(titulo, autor, isbn)
                
            elif opcion == 2:
                isbn = input("Ingrese el ISBN del libro a prestar: ")
                biblioteca.prestar(isbn)
                
            elif opcion == 3:
                isbn = input("Ingrese el ISBN del libro a devolver: ")
                biblioteca.devolver(isbn)
                
            elif opcion == 4:
                biblioteca.mostrar()
                
            elif opcion == 5:
                isbn = input("Ingrese el ISBN del libro a buscar: ")
                biblioteca.buscar(isbn)
                
            elif opcion == 6:
                print("¡Gracias por usar el Sistema de Gestión de Biblioteca!")
                break
                
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
                
        except ValueError:
            print("Error: Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()
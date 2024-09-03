import java.util.Scanner; // Importa la clase Scanner para leer la entrada del usuario

public class Conversordenumeros {
    // Convierte un número de base 8, 10 o 16 a base 10
    public static int baseAdecimal(String numero, int base) {
        return Integer.parseInt(numero, base); // Convierte el número dado de la base especificada a base 10
    }

    // Convierte un número de base 10 a otra base (8, 10 o 16)
    public static String decimalAbase(int decimal, int base) {
        return Integer.toString(decimal, base).toUpperCase(); // Convierte el número dado en base 10 a la base especificada
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); // Crea un objeto Scanner para leer la entrada del usuario
        String opcion; // Declara una variable para almacenar la opción seleccionada por el usuario

        do {
            // Muestra el menú de opciones al usuario
            System.out.println("Seleccione una opción:");
            System.out.println("1. Convertir de base 8 a base 10");
            System.out.println("2. Convertir de base 10 a base 8");
            System.out.println("3. Convertir de base 16 a base 10");
            System.out.println("4. Convertir de base 10 a base 16");
            System.out.println("5. Salir");

            opcion = scanner.nextLine(); // Lee la opción seleccionada por el usuario

            switch (opcion) {
                case "1":
                    System.out.print("Ingrese un número en base 8: ");
                    String numeroOctal = scanner.nextLine(); // Lee el número en base 8 ingresado por el usuario
                    int numeroDecimal = baseAdecimal(numeroOctal, 8); // Convierte el número de base 8 a base 10
                    System.out.println("El número " + numeroOctal + " en base 8 es igual a " + numeroDecimal + " en base 10.");
                    break;

                case "2":
                    System.out.print("Ingrese un número en base 10: ");
                    int numeroDecimalInput = scanner.nextInt(); // Lee el número en base 10 ingresado por el usuario
                    scanner.nextLine(); // Consume la nueva línea dejada por nextInt
                    String numeroOctalResult = decimalAbase(numeroDecimalInput, 8); // Convierte el número de base 10 a base 8
                    System.out.println("El número " + numeroDecimalInput + " en base 10 es igual a " + numeroOctalResult + " en base 8.");
                    break;

                case "3":
                    System.out.print("Ingrese un número en base 16: ");
                    String numeroHex = scanner.nextLine().toUpperCase(); // Lee el número en base 16 ingresado por el usuario
                    int numeroDecimalHex = baseAdecimal(numeroHex, 16); // Convierte el número de base 16 a base 10
                    System.out.println("El número " + numeroHex + " en base 16 es igual a " + numeroDecimalHex + " en base 10.");
                    break;

                case "4":
                    System.out.print("Ingrese un número en base 10: ");
                    int numeroDecimalInputHex = scanner.nextInt(); // Lee el número en base 10 ingresado por el usuario
                    scanner.nextLine(); // Consume la nueva línea dejada por nextInt
                    String numeroHexResult = decimalAbase(numeroDecimalInputHex, 16); // Convierte el número de base 10 a base 16
                    System.out.println("El número " + numeroDecimalInputHex + " en base 10 es igual a " + numeroHexResult + " en base 16.");
                    break;

                case "5":
                    System.out.println("Saliendo del programa."); // Mensaje indicando que el programa va a finalizar
                    break;

                default:
                    System.out.println("Opción no válida. Por favor, ingrese una opción entre 1 y 5."); // Mensaje de error si la opción no es válida
            }

            System.out.println(); // Línea en blanco para separar iteraciones
        } while (!opcion.equals("5")); // Repite el bucle hasta que el usuario seleccione la opción de salir

        scanner.close(); // Cierra el objeto Scanner para liberar recursos
    }
}

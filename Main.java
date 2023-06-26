public class Main {
    public static void main(String[] args) { //DEBUGGEAR
        PlanDePagos plan = new PlanDePagos();
        Ejecutar ejecutar = new Ejecutar(plan);
        ejecutar.correr();
        ejecutar.imprimirInformacion();
    }
}
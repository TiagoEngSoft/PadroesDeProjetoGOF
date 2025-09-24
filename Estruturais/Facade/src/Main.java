import HomeTheaterFacade;

public class Main {
    public static void main(String[] args) {
        HomeTheaterFacade homeTheater = new HomeTheaterFacade();

        System.out.println("Ligando o sistema:");
        homeTheater.ligarSistema();

        System.out.println("\nDesligando o sistema:");
        homeTheater.desligarSistema();
    }
}

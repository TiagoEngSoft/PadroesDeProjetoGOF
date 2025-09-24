import comandos.*;
import dispositivos.*;

public class Main {
    public static void main(String[] args) {
        ControleRemoto controle = new ControleRemoto();

        Luz luz = new Luz();
        TV tv = new TV();

        Comando ligarLuz = new LigarLuz(luz);
        Comando desligarLuz = new DesligarLuz(luz);
        Comando ligarTV = new LigarTV(tv);
        Comando desligarTV = new DesligarTV(tv);

        System.out.println("▶️ Ligando a luz:");
        controle.setComando(ligarLuz);
        controle.pressionarBotao();

        System.out.println("\n⏹️ Desligando a luz:");
        controle.setComando(desligarLuz);
        controle.pressionarBotao();

        System.out.println("\n▶️ Ligando a TV:");
        controle.setComando(ligarTV);
        controle.pressionarBotao();

        System.out.println("\n⏹️ Desligando a TV:");
        controle.setComando(desligarTV);
        controle.pressionarBotao();
    }
}

package app;

import dispositivos.*;
import controles.*;

public class Main {
    public static void main(String[] args) {
        Dispositivo tv = new TV();
        Dispositivo radio = new Radio();

        ControleRemoto controleTV = new ControleSimples(tv);
        ControleRemoto controleRadio = new ControleAvancado(radio);

        System.out.println("--- Controle Simples com TV ---");
        controleTV.ligar();
        controleTV.desligar();

        System.out.println("\n--- Controle Avançado com Rádio ---");
        controleRadio.ligar();
        controleRadio.desligar();

        System.out.println("\n--- Usando alternar no controle avançado ---");
        ControleAvancado controleAvancadoRadio = new ControleAvancado(radio);
        controleAvancadoRadio.alternar();
        controleAvancadoRadio.alternar();
    }
}

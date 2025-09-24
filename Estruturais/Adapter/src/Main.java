package app;

import interfaces.Cordeiro;
import interfaces.Lobo;
import animais.CordeiroReal;
import animais.LoboReal;
import adapter.LoboEmPeleDeCordeiro;
import adapter.CordeiroEmPeleDeLobo;

public class Main {
    public static void main(String[] args) {

        System.out.println("=== 🐺 Lobo em pele de cordeiro ===");
        Lobo loboReal = new LoboReal();
        Cordeiro loboDisfarçado = new LoboEmPeleDeCordeiro(loboReal);
        loboDisfarçado.balir();

        System.out.println("\n=== 🐑 Cordeiro em pele de lobo ===");
        Cordeiro cordeiroReal = new CordeiroReal();
        Lobo cordeiroDisfarçado = new CordeiroEmPeleDeLobo(cordeiroReal);
        cordeiroDisfarçado.uivar();
        cordeiroDisfarçado.atacar();
    }
}

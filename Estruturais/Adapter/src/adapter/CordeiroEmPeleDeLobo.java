package adapter;

import interfaces.Cordeiro;
import interfaces.Lobo;

public class CordeiroEmPeleDeLobo implements Lobo {
    private Cordeiro cordeiro;

    public CordeiroEmPeleDeLobo(Cordeiro cordeiro) {
        this.cordeiro = cordeiro;
    }

    @Override
    public void uivar() {
        System.out.println("😅 Auuu... (mas é só um cordeiro tentando)");
    }

    @Override
    public void atacar() {
        System.out.println("🐑 Tentando atacar... mas só sabe balir:");
        cordeiro.balir();
    }
}

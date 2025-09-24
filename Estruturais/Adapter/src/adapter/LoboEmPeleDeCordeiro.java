package adapter;

import interfaces.Cordeiro;
import interfaces.Lobo;

public class LoboEmPeleDeCordeiro implements Cordeiro {
    private Lobo lobo;

    public LoboEmPeleDeCordeiro(Lobo lobo) {
        this.lobo = lobo;
    }

    @Override
    public void balir() {
        System.out.println("😇 Meeee... (parece dócil, mas...)");
        lobo.uivar();
        lobo.atacar();
    }
}

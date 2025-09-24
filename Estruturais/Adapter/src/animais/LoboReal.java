package animais;

import interfaces.Lobo;

public class LoboReal implements Lobo {
    @Override
    public void uivar() {
        System.out.println("🐺 Auuuuuuuu!");
    }

    @Override
    public void atacar() {
        System.out.println("⚠️ O lobo ataca ferozmente!");
    }
}

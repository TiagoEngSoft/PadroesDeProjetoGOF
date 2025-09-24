package animais;

import interfaces.Cordeiro;

public class CordeiroReal implements Cordeiro {
    @Override
    public void balir() {
        System.out.println("🐑 Meeeeeee!");
    }
}

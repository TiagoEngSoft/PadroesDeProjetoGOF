package comandos;

import dispositivos.TV;

public class DesligarTV implements Comando {
    private TV tv;

    public DesligarTV(TV tv) {
        this.tv = tv;
    }

    public void executar() {
        tv.desligar();
    }
}

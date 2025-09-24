package comandos;

import dispositivos.TV;

public class LigarTV implements Comando {
    private TV tv;

    public LigarTV(TV tv) {
        this.tv = tv;
    }

    public void executar() {
        tv.ligar();
    }
}

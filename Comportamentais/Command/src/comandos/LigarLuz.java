package comandos;

import dispositivos.Luz;

public class LigarLuz implements Comando {
    private Luz luz;

    public LigarLuz(Luz luz) {
        this.luz = luz;
    }

    public void executar() {
        luz.ligar();
    }
}

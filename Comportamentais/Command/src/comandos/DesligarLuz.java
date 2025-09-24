package comandos;

import dispositivos.Luz;

public class DesligarLuz implements Comando {
    private Luz luz;

    public DesligarLuz(Luz luz) {
        this.luz = luz;
    }

    public void executar() {
        luz.desligar();
    }
}

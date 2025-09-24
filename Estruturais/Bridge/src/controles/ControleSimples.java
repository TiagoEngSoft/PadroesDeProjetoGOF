package controles;

import dispositivos.Dispositivo;

public class ControleSimples extends ControleRemoto {
    public ControleSimples(Dispositivo dispositivo) {
        super(dispositivo);
    }

    public void ligar() {
        dispositivo.ligar();
    }

    public void desligar() {
        dispositivo.desligar();
    }
}

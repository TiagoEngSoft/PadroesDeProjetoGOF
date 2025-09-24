package controles;

import dispositivos.Dispositivo;

public class ControleAvancado extends ControleRemoto {
    public ControleAvancado(Dispositivo dispositivo) {
        super(dispositivo);
    }

    public void ligar() {
        dispositivo.ligar();
        System.out.println("Controle avançado: dispositivo ligado com recursos extras.");
    }

    public void desligar() {
        dispositivo.desligar();
        System.out.println("Controle avançado: dispositivo desligado com recursos extras.");
    }

    public void alternar() {
        if (dispositivo.isLigado()) {
            desligar();
        } else {
            ligar();
        }
    }
}

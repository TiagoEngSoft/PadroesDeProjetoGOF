package dispositivos;

public class Radio implements Dispositivo {
    private boolean ligado = false;

    public void ligar() {
        ligado = true;
        System.out.println("Rádio ligado.");
    }

    public void desligar() {
        ligado = false;
        System.out.println("Rádio desligado.");
    }

    public boolean isLigado() {
        return ligado;
    }
}

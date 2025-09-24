package dispositivos;

public class TV implements Dispositivo {
    private boolean ligado = false;

    public void ligar() {
        ligado = true;
        System.out.println("TV ligada.");
    }

    public void desligar() {
        ligado = false;
        System.out.println("TV desligada.");
    }

    public boolean isLigado() {
        return ligado;
    }
}

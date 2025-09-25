package observer;

public class TemperatureDisplay implements Observer {
    private String nome;

    public TemperatureDisplay(String nome) {
        this.nome = nome;
    }

    @Override
    public void atualizar(float temperatura) {
        System.out.println("📺 [" + nome + "] Temperatura atualizada: " + temperatura + "°C");
    }
}

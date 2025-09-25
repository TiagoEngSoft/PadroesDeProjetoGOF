import observer.*;

public class Main {
    public static void main(String[] args) {
        WeatherStation estacao = new WeatherStation();

        TemperatureDisplay tela1 = new TemperatureDisplay("Tela 1");
        TemperatureDisplay tela2 = new TemperatureDisplay("Tela 2");

        estacao.registrarObserver(tela1);
        estacao.registrarObserver(tela2);

        estacao.setTemperatura(25.0f);
        estacao.setTemperatura(30.5f);

        estacao.removerObserver(tela2);
        estacao.setTemperatura(27.0f);
    }
}

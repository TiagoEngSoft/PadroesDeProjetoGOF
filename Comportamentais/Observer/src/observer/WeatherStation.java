package observer;

import java.util.ArrayList;
import java.util.List;

public class WeatherStation implements Subject {
    private List<Observer> observers = new ArrayList<>();
    private float temperatura;

    @Override
    public void registrarObserver(Observer o) {
        observers.add(o);
    }

    @Override
    public void removerObserver(Observer o) {
        observers.remove(o);
    }

    @Override
    public void notificarObservers() {
        for (Observer o : observers) {
            o.atualizar(temperatura);
        }
    }

    public void setTemperatura(float novaTemperatura) {
        System.out.println("\n🌡️ Temperatura alterada para: " + novaTemperatura + "°C");
        this.temperatura = novaTemperatura;
        notificarObservers();
    }
}

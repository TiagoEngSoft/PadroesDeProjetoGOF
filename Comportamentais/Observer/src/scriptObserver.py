import os

# Conteúdo dos arquivos Java

subject_java = '''\
package observer;

public interface Subject {
    void registrarObserver(Observer o);
    void removerObserver(Observer o);
    void notificarObservers();
}
'''

observer_java = '''\
package observer;

public interface Observer {
    void atualizar(float temperatura);
}
'''

weather_station_java = '''\
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
        System.out.println("\\n🌡️ Temperatura alterada para: " + novaTemperatura + "°C");
        this.temperatura = novaTemperatura;
        notificarObservers();
    }
}
'''

temperature_display_java = '''\
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
'''

main_java = '''\
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
'''

# Mapeamento dos arquivos a serem criados
arquivos = {
    'observer/Subject.java': subject_java,
    'observer/Observer.java': observer_java,
    'observer/WeatherStation.java': weather_station_java,
    'observer/TemperatureDisplay.java': temperature_display_java,
    'Main.java': main_java,
}


def criar_projeto(path_base):
    print(f"\n🔧 Criando projeto Observer em: {path_base}\n")

    for caminho_relativo, conteudo in arquivos.items():
        caminho_completo = os.path.join(path_base, caminho_relativo)
        pasta = os.path.dirname(caminho_completo)

        os.makedirs(pasta, exist_ok=True)
        with open(caminho_completo, 'w', encoding='utf-8') as f:
            f.write(conteudo)

        print(f"✅ Criado: {caminho_relativo}")

    print("\n📦 Projeto Observer Java criado com sucesso!")
    print(f"📁 Local: {os.path.abspath(path_base)}")
    print("\nPressione ENTER para sair...")
    input()


# Execução principal
if __name__ == "__main__":
    print("🛠️  Criador de Projeto Java - Padrão Observer\n")
    path = input("📂 Digite o caminho onde o projeto deve ser salvo: ").strip()

    if not path:
        print("❌ Caminho inválido. Encerrando.")
    else:
        criar_projeto(path)

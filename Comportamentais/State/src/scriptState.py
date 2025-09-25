import os

# Conteúdo dos arquivos Java

state_java = '''\
package state;

public interface State {
    void pressionarBotao(PlayerContext context);
}
'''

playing_state_java = '''\
package state;

public class PlayingState implements State {
    @Override
    public void pressionarBotao(PlayerContext context) {
        System.out.println("⏸️ Pausando música...");
        context.setState(new PausedState());
    }
}
'''

paused_state_java = '''\
package state;

public class PausedState implements State {
    @Override
    public void pressionarBotao(PlayerContext context) {
        System.out.println("▶️ Retomando música...");
        context.setState(new PlayingState());
    }
}
'''

player_context_java = '''\
package state;

public class PlayerContext {
    private State estadoAtual;

    public PlayerContext() {
        // Começa em modo pausado
        this.estadoAtual = new PausedState();
    }

    public void setState(State novoEstado) {
        this.estadoAtual = novoEstado;
    }

    public void pressionarBotao() {
        estadoAtual.pressionarBotao(this);
    }
}
'''

main_java = '''\
import state.*;

public class Main {
    public static void main(String[] args) {
        PlayerContext player = new PlayerContext();

        System.out.println("🎵 Simulador de botão Play/Pause:\n");

        player.pressionarBotao(); // Deve iniciar reprodução
        player.pressionarBotao(); // Deve pausar
        player.pressionarBotao(); // Deve reproduzir
    }
}
'''

# Mapeamento de arquivos
arquivos = {
    'state/State.java': state_java,
    'state/PlayingState.java': playing_state_java,
    'state/PausedState.java': paused_state_java,
    'state/PlayerContext.java': player_context_java,
    'Main.java': main_java,
}


def criar_projeto(path_base):
    print(f"\n🛠️ Criando projeto State em: {path_base}\n")

    for caminho_relativo, conteudo in arquivos.items():
        caminho_completo = os.path.join(path_base, caminho_relativo)
        pasta = os.path.dirname(caminho_completo)

        os.makedirs(pasta, exist_ok=True)
        with open(caminho_completo, 'w', encoding='utf-8') as f:
            f.write(conteudo)

        print(f"✅ Criado: {caminho_relativo}")

    print("\n📦 Projeto Java com padrão State criado com sucesso!")
    print(f"📁 Local: {os.path.abspath(path_base)}")
    print("\nPressione ENTER para sair...")
    input()


if __name__ == "__main__":
    print("🔁 Criador de Projeto Java - Padrão State\n")
    path = input("📂 Digite o caminho onde o projeto deve ser salvo: ").strip()

    if not path:
        print("❌ Caminho inválido. Encerrando.")
    else:
        criar_projeto(path)

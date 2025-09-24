from pathlib import Path

# Função para gerar os arquivos do projeto Facade
def criar_projeto_facade(caminho_base):
    caminho_base = Path(caminho_base)
    src = caminho_base / "src"
    sistema = src / "sistema"
    app = src / "app"

    # Criando as pastas
    sistema.mkdir(parents=True, exist_ok=True)
    app.mkdir(parents=True, exist_ok=True)

    # Arquivos do sistema (subsistemas)
    (sistema / "SistemaAudio.java").write_text(
        '''package sistema;

public class SistemaAudio {
    public void ligarAudio() {
        System.out.println("Áudio ligado.");
    }

    public void desligarAudio() {
        System.out.println("Áudio desligado.");
    }
}
''')

    (sistema / "SistemaVideo.java").write_text(
        '''package sistema;

public class SistemaVideo {
    public void ligarVideo() {
        System.out.println("Vídeo ligado.");
    }

    public void desligarVideo() {
        System.out.println("Vídeo desligado.");
    }
}
''')

    (sistema / "SistemaRede.java").write_text(
        '''package sistema;

public class SistemaRede {
    public void conectarInternet() {
        System.out.println("Internet conectada.");
    }

    public void desconectarInternet() {
        System.out.println("Internet desconectada.");
    }
}
''')

    # Classe Facade
    (src / "HomeTheaterFacade.java").write_text(
        '''import sistema.SistemaAudio;
import sistema.SistemaVideo;
import sistema.SistemaRede;

public class HomeTheaterFacade {
    private SistemaAudio audio;
    private SistemaVideo video;
    private SistemaRede rede;

    public HomeTheaterFacade() {
        audio = new SistemaAudio();
        video = new SistemaVideo();
        rede = new SistemaRede();
    }

    public void ligarSistema() {
        audio.ligarAudio();
        video.ligarVideo();
        rede.conectarInternet();
        System.out.println("Sistema de Home Theater pronto para uso!");
    }

    public void desligarSistema() {
        audio.desligarAudio();
        video.desligarVideo();
        rede.desconectarInternet();
        System.out.println("Sistema de Home Theater desligado.");
    }
}
''')

    # Classe Main
    (app / "Main.java").write_text(
        '''import HomeTheaterFacade;

public class Main {
    public static void main(String[] args) {
        HomeTheaterFacade homeTheater = new HomeTheaterFacade();

        System.out.println("Ligando o sistema:");
        homeTheater.ligarSistema();

        System.out.println("\\nDesligando o sistema:");
        homeTheater.desligarSistema();
    }
}
''')

    return f"Projeto Facade criado em: {caminho_base.resolve()}"

# Executar criação do projeto
caminho_projeto = input("Digite o caminho onde deseja criar o projeto Facade: ").strip()
resumo = criar_projeto_facade(caminho_projeto)
input(f"\n✅ {resumo}\n\nPressione ENTER para encerrar...")

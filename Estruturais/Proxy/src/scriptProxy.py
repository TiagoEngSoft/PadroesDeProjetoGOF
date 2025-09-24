import os

def criar_estrutura_proxy(path):
    if not os.path.exists(path):
        os.makedirs(path)

    estrutura = {
        "src/proxy": {
            "Video.java": '''public interface Video {
    void reproduzir();
}
''',

            "VideoReal.java": '''public class VideoReal implements Video {
    private String nomeArquivo;

    public VideoReal(String nomeArquivo) {
        this.nomeArquivo = nomeArquivo;
        carregarDoDisco(nomeArquivo);
    }

    private void carregarDoDisco(String nome) {
        System.out.println("🔄 Carregando vídeo: " + nome);
    }

    public void reproduzir() {
        System.out.println("▶️ Reproduzindo vídeo: " + nomeArquivo);
    }
}
''',

            "VideoProxy.java": '''public class VideoProxy implements Video {
    private String nomeArquivo;
    private VideoReal videoReal;

    public VideoProxy(String nomeArquivo) {
        this.nomeArquivo = nomeArquivo;
    }

    public void reproduzir() {
        if (videoReal == null) {
            videoReal = new VideoReal(nomeArquivo); // Carrega somente na primeira vez
        }
        videoReal.reproduzir();
    }
}
'''
        },
        "src/app": {
            "Main.java": '''import proxy.Video;
import proxy.VideoProxy;

public class Main {
    public static void main(String[] args) {
        Video video = new VideoProxy("filme-super-hd.mp4");

        System.out.println("🎬 Primeiro acesso:");
        video.reproduzir(); // Aqui o vídeo é carregado e reproduzido

        System.out.println("\\n⏯️ Segundo acesso:");
        video.reproduzir(); // Aqui só é reproduzido (sem carregar novamente)
    }
}
'''
        }
    }

    for pasta, arquivos in estrutura.items():
        pasta_path = os.path.join(path, pasta)
        os.makedirs(pasta_path, exist_ok=True)
        for nome_arquivo, conteudo in arquivos.items():
            with open(os.path.join(pasta_path, nome_arquivo), 'w', encoding='utf-8') as f:
                f.write(conteudo)

    print("\n✅ Projeto Proxy gerado com sucesso!")
    print(f"📁 Local: {os.path.abspath(path)}")
    input("\nPressione ENTER para sair...")

if __name__ == "__main__":
    caminho = input("Digite o caminho onde o projeto deve ser criado: ").strip()
    criar_estrutura_proxy(caminho)

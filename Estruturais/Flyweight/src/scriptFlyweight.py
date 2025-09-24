import os

def criar_projeto_flyweight_emojis(path_base):
    # Criar estrutura de diretórios
    os.makedirs(os.path.join(path_base, "src", "flyweight"), exist_ok=True)
    os.makedirs(os.path.join(path_base, "src", "factory"), exist_ok=True)
    os.makedirs(os.path.join(path_base, "src", "app"), exist_ok=True)

    arquivos = {
        "src/flyweight/EmojiBalao.java": '''\
public class EmojiBalao {
    private final String emoji = "🎈";

    public void desenhar(int x, int y, String cor) {
        System.out.println("Desenhando balão " + emoji +
                           " na posição (" + x + "," + y + ") com a cor " + cor);
    }
}
''',

        "src/factory/EmojiFactory.java": '''\
import java.util.HashMap;

public class EmojiFactory {
    private static final HashMap<String, EmojiBalao> cache = new HashMap<>();

    public static EmojiBalao getBalao(String cor) {
        EmojiBalao balao = cache.get(cor);
        if (balao == null) {
            balao = new EmojiBalao();
            cache.put(cor, balao);
            System.out.println("🎨 Criando novo objeto EmojiBalão para a cor: " + cor);
        }
        return balao;
    }
}
''',

        "src/app/Main.java": '''\
public class Main {
    public static void main(String[] args) {
        String[] cores = { "vermelho", "azul", "verde" };

        for (int i = 0; i < 10; i++) {
            String cor = cores[i % cores.length];
            int x = (int) (Math.random() * 100);
            int y = (int) (Math.random() * 100);

            EmojiBalao balao = EmojiFactory.getBalao(cor);
            balao.desenhar(x, y, cor);
        }
    }
}
'''
    }

    # Criar os arquivos com conteúdo
    for nome_arquivo, conteudo in arquivos.items():
        caminho = os.path.join(path_base, nome_arquivo)
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo)

    print("✅ Projeto Flyweight com Emojis criado com sucesso!")
    print(f"📁 Diretório base: {path_base}")
    input("Pressione ENTER para sair...")

# Execução principal
if __name__ == "__main__":
    path_projeto = input("📂 Informe o caminho onde o projeto deve ser criado: ").strip('"')
    criar_projeto_flyweight_emojis(path_projeto)

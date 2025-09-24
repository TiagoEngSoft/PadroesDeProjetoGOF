import os

# Mapeamento dos arquivos por pacote
estrutura_projeto = {
    "src/cartao/Cartao.java": """package cartao;

public interface Cartao {
    void exibirMensagem();
}
""",
    "src/cartao/CartaoAniversario.java": """package cartao;

public class CartaoAniversario implements Cartao {
    public void exibirMensagem() {
        System.out.println("Feliz Aniversário!");
    }
}
""",
    "src/cartao/CartaoNatal.java": """package cartao;

public class CartaoNatal implements Cartao {
    public void exibirMensagem() {
        System.out.println("Feliz Natal!");
    }
}
""",
    "src/criador/CriadorCartao.java": """package criador;

import cartao.Cartao;

public abstract class CriadorCartao {
    public abstract Cartao criarCartao();

    public void enviarCartao() {
        Cartao cartao = criarCartao();
        cartao.exibirMensagem();
    }
}
""",
    "src/criador/CriadorCartaoAniversario.java": """package criador;

import cartao.Cartao;
import cartao.CartaoAniversario;

public class CriadorCartaoAniversario extends CriadorCartao {
    public Cartao criarCartao() {
        return new CartaoAniversario();
    }
}
""",
    "src/criador/CriadorCartaoNatal.java": """package criador;

import cartao.Cartao;
import cartao.CartaoNatal;

public class CriadorCartaoNatal extends CriadorCartao {
    public Cartao criarCartao() {
        return new CartaoNatal();
    }
}
""",
    "src/app/Main.java": """package app;

import criador.CriadorCartao;
import criador.CriadorCartaoAniversario;
import criador.CriadorCartaoNatal;

public class Main {
    public static void main(String[] args) {
        CriadorCartao criador1 = new CriadorCartaoAniversario();
        CriadorCartao criador2 = new CriadorCartaoNatal();

        criador1.enviarCartao(); // Saída: Feliz Aniversário!
        criador2.enviarCartao(); // Saída: Feliz Natal!
    }
}
"""
}


def criar_estrutura(path):
    print(f"\n📁 Criando estrutura no diretório: {path}")

    for rel_path, conteudo in estrutura_projeto.items():
        full_path = os.path.join(path, rel_path)
        dir_path = os.path.dirname(full_path)

        # Criar diretório, se não existir
        os.makedirs(dir_path, exist_ok=True)

        # Criar o arquivo com conteúdo
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(conteudo)

        print(f"  ✅ {rel_path} criado.")


def main():
    print("=== Gerador de Projeto Java (Factory Method - Clean Code) ===")
    destino = input("Informe o caminho onde deseja criar o projeto: ").strip()

    if not destino:
        print("❌ Caminho inválido.")
        return

    try:
        criar_estrutura(destino)
        print("\n✅ Projeto criado com sucesso!")
        print("\nResumo dos pacotes e arquivos:")
        for caminho in estrutura_projeto:
            print(" -", caminho)
    except Exception as e:
        print("❌ Erro:", e)

    input("\nPressione ENTER para fechar...")


if __name__ == "__main__":
    main()

import os

# Mapeamento: caminho relativo → conteúdo do arquivo
estrutura_projeto = {
    # Interfaces dos cartões
    "src/cartao/CartaoAniversario.java": """package cartao;

public interface CartaoAniversario {
    void exibirMensagem();
}
""",

    "src/cartao/CartaoNatal.java": """package cartao;

public interface CartaoNatal {
    void exibirMensagem();
}
""",

    # Interface da fábrica
    "src/fabrica/FabricaCartao.java": """package fabrica;

import cartao.CartaoAniversario;
import cartao.CartaoNatal;

public interface FabricaCartao {
    CartaoAniversario criarCartaoAniversario();
    CartaoNatal criarCartaoNatal();
}
""",

    # Implementações simples
    "src/simples/CartaoAniversarioSimples.java": """package simples;

import cartao.CartaoAniversario;

public class CartaoAniversarioSimples implements CartaoAniversario {
    public void exibirMensagem() {
        System.out.println("Feliz Aniversário! (Simples)");
    }
}
""",

    "src/simples/CartaoNatalSimples.java": """package simples;

import cartao.CartaoNatal;

public class CartaoNatalSimples implements CartaoNatal {
    public void exibirMensagem() {
        System.out.println("Feliz Natal! (Simples)");
    }
}
""",

    "src/simples/FabricaCartaoSimples.java": """package simples;

import fabrica.FabricaCartao;
import cartao.CartaoAniversario;
import cartao.CartaoNatal;

public class FabricaCartaoSimples implements FabricaCartao {
    public CartaoAniversario criarCartaoAniversario() {
        return new CartaoAniversarioSimples();
    }

    public CartaoNatal criarCartaoNatal() {
        return new CartaoNatalSimples();
    }
}
""",

    # Implementações luxo
    "src/luxo/CartaoAniversarioLuxo.java": """package luxo;

import cartao.CartaoAniversario;

public class CartaoAniversarioLuxo implements CartaoAniversario {
    public void exibirMensagem() {
        System.out.println("Feliz Aniversário! 🎉 (Luxo)");
    }
}
""",

    "src/luxo/CartaoNatalLuxo.java": """package luxo;

import cartao.CartaoNatal;

public class CartaoNatalLuxo implements CartaoNatal {
    public void exibirMensagem() {
        System.out.println("Feliz Natal! 🎄 (Luxo)");
    }
}
""",

    "src/luxo/FabricaCartaoLuxo.java": """package luxo;

import fabrica.FabricaCartao;
import cartao.CartaoAniversario;
import cartao.CartaoNatal;

public class FabricaCartaoLuxo implements FabricaCartao {
    public CartaoAniversario criarCartaoAniversario() {
        return new CartaoAniversarioLuxo();
    }

    public CartaoNatal criarCartaoNatal() {
        return new CartaoNatalLuxo();
    }
}
""",

    # Main
    "src/app/Main.java": """package app;

import fabrica.FabricaCartao;
import simples.FabricaCartaoSimples;
import luxo.FabricaCartaoLuxo;
import cartao.CartaoAniversario;
import cartao.CartaoNatal;

public class Main {
    public static void main(String[] args) {
        System.out.println("Usando Cartões SIMPLES:");
        FabricaCartao fabricaSimples = new FabricaCartaoSimples();
        CartaoAniversario aniversarioSimples = fabricaSimples.criarCartaoAniversario();
        CartaoNatal natalSimples = fabricaSimples.criarCartaoNatal();
        aniversarioSimples.exibirMensagem();
        natalSimples.exibirMensagem();

        System.out.println("\\nUsando Cartões LUXO:");
        FabricaCartao fabricaLuxo = new FabricaCartaoLuxo();
        CartaoAniversario aniversarioLuxo = fabricaLuxo.criarCartaoAniversario();
        CartaoNatal natalLuxo = fabricaLuxo.criarCartaoNatal();
        aniversarioLuxo.exibirMensagem();
        natalLuxo.exibirMensagem();
    }
}
"""
}

def criar_projeto(caminho_base):
    print(f"\n📁 Criando projeto em: {caminho_base}")
    for rel_path, conteudo in estrutura_projeto.items():
        caminho_completo = os.path.join(caminho_base, rel_path)
        pasta = os.path.dirname(caminho_completo)
        os.makedirs(pasta, exist_ok=True)
        with open(caminho_completo, "w", encoding="utf-8") as f:
            f.write(conteudo)
        print(f"  ✅ {rel_path}")

def main():
    print("=== Gerador de Projeto Java (Abstract Factory - Clean Code) ===")
    destino = input("Informe o caminho onde deseja criar o projeto: ").strip()

    if not destino:
        print("❌ Caminho inválido.")
        return

    try:
        criar_projeto(destino)
        print("\n✅ Projeto criado com sucesso!")
        print("\nResumo da estrutura:")
        for caminho in estrutura_projeto:
            print(" -", caminho)
    except Exception as e:
        print("❌ Erro:", e)

    input("\nPressione ENTER para sair...")

if __name__ == "__main__":
    main()

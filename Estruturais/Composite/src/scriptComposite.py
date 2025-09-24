import os

estrutura_projeto = {
    "src/composite/Componente.java": """package composite;

public interface Componente {
    void mostrar(int nivel);
}
""",

    "src/composite/Arquivo.java": """package composite;

public class Arquivo implements Componente {
    private String nome;

    public Arquivo(String nome) {
        this.nome = nome;
    }

    @Override
    public void mostrar(int nivel) {
        System.out.println("  ".repeat(nivel) + "- " + nome);
    }
}
""",

    "src/composite/Pasta.java": """package composite;

import java.util.ArrayList;
import java.util.List;

public class Pasta implements Componente {
    private String nome;
    private List<Componente> filhos = new ArrayList<>();

    public Pasta(String nome) {
        this.nome = nome;
    }

    public void adicionar(Componente c) {
        filhos.add(c);
    }

    public void remover(Componente c) {
        filhos.remove(c);
    }

    @Override
    public void mostrar(int nivel) {
        System.out.println("  ".repeat(nivel) + "+ " + nome);
        for (Componente filho : filhos) {
            filho.mostrar(nivel + 1);
        }
    }
}
""",

    "src/app/Main.java": """package app;

import composite.Componente;
import composite.Arquivo;
import composite.Pasta;

public class Main {
    public static void main(String[] args) {
        // Cria arquivos
        Componente arquivo1 = new Arquivo("arquivo1.txt");
        Componente arquivo2 = new Arquivo("arquivo2.txt");
        Componente arquivo3 = new Arquivo("foto.png");

        // Cria pastas
        Pasta pastaDocumentos = new Pasta("Documentos");
        Pasta pastaImagens = new Pasta("Imagens");
        Pasta pastaRaiz = new Pasta("Raiz");

        // Monta a estrutura
        pastaDocumentos.adicionar(arquivo1);
        pastaDocumentos.adicionar(arquivo2);

        pastaImagens.adicionar(arquivo3);

        pastaRaiz.adicionar(pastaDocumentos);
        pastaRaiz.adicionar(pastaImagens);

        // Mostra a estrutura
        pastaRaiz.mostrar(0);
    }
}
""",
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
    print("=== Gerador de Projeto Java (Composite) ===")
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

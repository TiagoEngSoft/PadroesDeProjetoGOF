import os

# Estrutura de arquivos: caminho relativo → conteúdo
estrutura_projeto = {
    "src/singleton/Configuracao.java": """package singleton;

public class Configuracao {
    private static Configuracao instancia;

    private String ambiente;
    private String versao;

    private Configuracao() {
        // Configurações padrão
        this.ambiente = "PRODUCAO";
        this.versao = "1.0.0";
    }

    public static Configuracao getInstancia() {
        if (instancia == null) {
            instancia = new Configuracao();
        }
        return instancia;
    }

    public String getAmbiente() {
        return ambiente;
    }

    public void setAmbiente(String ambiente) {
        this.ambiente = ambiente;
    }

    public String getVersao() {
        return versao;
    }

    public void setVersao(String versao) {
        this.versao = versao;
    }

    @Override
    public String toString() {
        return "[Ambiente: " + ambiente + ", Versão: " + versao + "]";
    }
}
""",

    "src/app/Main.java": """package app;

import singleton.Configuracao;

public class Main {
    public static void main(String[] args) {
        Configuracao conf1 = Configuracao.getInstancia();
        System.out.println("Configuração Inicial: " + conf1);

        // Alterar configuração
        conf1.setAmbiente("DESENVOLVIMENTO");
        conf1.setVersao("1.1.0");

        Configuracao conf2 = Configuracao.getInstancia();
        System.out.println("Configuração Acessada Novamente: " + conf2);

        if (conf1 == conf2) {
            System.out.println("✅ Mesma instância compartilhada (Singleton)");
        } else {
            System.out.println("❌ Instâncias diferentes (Erro)");
        }
    }
}
"""
}

def criar_projeto(caminho_base):
    print(f"\n📁 Criando projeto Singleton em: {caminho_base}")
    for rel_path, conteudo in estrutura_projeto.items():
        caminho_completo = os.path.join(caminho_base, rel_path)
        os.makedirs(os.path.dirname(caminho_completo), exist_ok=True)
        with open(caminho_completo, "w", encoding="utf-8") as f:
            f.write(conteudo)
        print(f"  ✅ {rel_path}")

def main():
    print("=== Gerador de Projeto Java (Singleton) ===")
    destino = input("Informe o caminho onde deseja criar o projeto: ").strip()
    if not destino:
        print("❌ Caminho inválido.")
        return

    try:
        criar_projeto(destino)
        print("\n✅ Projeto criado com sucesso!")
    except Exception as e:
        print("❌ Erro:", e)

    input("\nPressione ENTER para sair...")

if __name__ == "__main__":
    main()

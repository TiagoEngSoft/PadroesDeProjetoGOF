import os

# Novo conteúdo dos arquivos Java (exemplo de Suporte Técnico)
arquivos = {
    "Chamado.java": '''\
package br.com.empresa.chain;

public class Chamado {
    private String descricao;

    public Chamado(String descricao) {
        this.descricao = descricao;
    }

    public String getDescricao() {
        return descricao;
    }
}
''',

    "responsaveis/Responsavel.java": '''\
package br.com.empresa.chain.responsaveis;

import br.com.empresa.chain.Chamado;

public abstract class Responsavel {
    protected Responsavel proximo;

    public void setProximo(Responsavel proximo) {
        this.proximo = proximo;
    }

    public abstract void tratarChamado(Chamado chamado);
}
''',

    "responsaveis/Atendente.java": '''\
package br.com.empresa.chain.responsaveis;

import br.com.empresa.chain.Chamado;

public class Atendente extends Responsavel {
    @Override
    public void tratarChamado(Chamado chamado) {
        if (chamado.getDescricao().toLowerCase().contains("senha")) {
            System.out.println("Atendente resolveu o problema: " + chamado.getDescricao());
        } else if (proximo != null) {
            proximo.tratarChamado(chamado);
        } else {
            System.out.println("Ninguém conseguiu resolver: " + chamado.getDescricao());
        }
    }
}
''',

    "responsaveis/SuporteTecnico.java": '''\
package br.com.empresa.chain.responsaveis;

import br.com.empresa.chain.Chamado;

public class SuporteTecnico extends Responsavel {
    @Override
    public void tratarChamado(Chamado chamado) {
        if (chamado.getDescricao().toLowerCase().contains("conectar")) {
            System.out.println("Suporte Técnico resolveu o problema: " + chamado.getDescricao());
        } else if (proximo != null) {
            proximo.tratarChamado(chamado);
        } else {
            System.out.println("Ninguém conseguiu resolver: " + chamado.getDescricao());
        }
    }
}
''',

    "responsaveis/Especialista.java": '''\
package br.com.empresa.chain.responsaveis;

import br.com.empresa.chain.Chamado;

public class Especialista extends Responsavel {
    @Override
    public void tratarChamado(Chamado chamado) {
        System.out.println("Especialista resolveu o problema: " + chamado.getDescricao());
    }
}
''',

    "Main.java": '''\
package br.com.empresa.chain;

import br.com.empresa.chain.responsaveis.*;

public class Main {
    public static void main(String[] args) {
        Responsavel atendente = new Atendente();
        Responsavel suporte = new SuporteTecnico();
        Responsavel especialista = new Especialista();

        atendente.setProximo(suporte);
        suporte.setProximo(especialista);

        Chamado chamado1 = new Chamado("Esqueci minha senha");
        Chamado chamado2 = new Chamado("Não consigo conectar ao sistema");
        Chamado chamado3 = new Chamado("Erro crítico no banco de dados");

        System.out.println("Processando chamados...\\n");

        atendente.tratarChamado(chamado1);
        atendente.tratarChamado(chamado2);
        atendente.tratarChamado(chamado3);
    }
}
'''
}

def criar_projeto(path_base):
    nome_projeto = "ChainSuporteTecnico"
    caminho_projeto = os.path.join(path_base, nome_projeto)
    caminho_src = os.path.join(caminho_projeto, "src", "br", "com", "empresa", "chain")
    caminho_responsaveis = os.path.join(caminho_src, "responsaveis")

    try:
        os.makedirs(caminho_responsaveis, exist_ok=True)
        print(f"\n✅ Projeto criado em: {caminho_projeto}\n")

        for nome_arquivo, conteudo in arquivos.items():
            caminho_relativo = os.path.join(caminho_src, nome_arquivo.replace("/", os.sep))
            os.makedirs(os.path.dirname(caminho_relativo), exist_ok=True)
            with open(caminho_relativo, 'w', encoding='utf-8') as f:
                f.write(conteudo)
            print(f"📄 Arquivo criado: {nome_arquivo}")

        # Exibir estrutura
        print("\n📦 Estrutura do projeto:")
        print(f"{nome_projeto}/")
        print(f"  └── src/")
        print(f"      └── br/com/empresa/chain/")
        print(f"          ├── Chamado.java")
        print(f"          ├── Main.java")
        print(f"          └── responsaveis/")
        for nome in arquivos:
            if nome.startswith("responsaveis/"):
                print(f"              └── {nome.split('/')[-1]}")

    except Exception as e:
        print(f"❌ Erro ao criar o projeto: {e}")

if __name__ == "__main__":
    print("=== Gerador de Projeto Java - Suporte Técnico (Chain of Responsibility) ===")
    caminho = input("📁 Digite o caminho onde deseja criar o projeto: ").strip('"')

    if not os.path.exists(caminho):
        print("❌ Caminho não existe.")
    else:
        criar_projeto(caminho)

    input("\nPressione ENTER para sair...")

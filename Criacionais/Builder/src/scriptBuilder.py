import os

# Estrutura de arquivos: caminho relativo → conteúdo
estrutura_projeto = {
    "src/builder/PersonBuilder.java": """package builder;

import modelos.Endereco;
import modelos.Pessoa;

public class PersonBuilder {
    private String nome;
    private int idade;
    private Endereco endereco;

    public PersonBuilder setNome(String nome) {
        this.nome = nome;
        return this;
    }

    public PersonBuilder setIdade(int idade) {
        this.idade = idade;
        return this;
    }

    public PersonBuilder setEndereco(String rua, String cidade) {
        this.endereco = new Endereco(rua, cidade);
        return this;
    }

    public Pessoa build() {
        return new Pessoa(nome, idade, endereco);
    }
}
""",

    "src/modelos/Endereco.java": """package modelos;

public class Endereco {
    private String rua;
    private String cidade;

    public Endereco(String rua, String cidade) {
        this.rua = rua;
        this.cidade = cidade;
    }

    @Override
    public String toString() {
        return rua + ", " + cidade;
    }
}
""",

    "src/modelos/Pessoa.java": """package modelos;

public class Pessoa {
    private String nome;
    private int idade;
    private Endereco endereco;

    public Pessoa(String nome, int idade, Endereco endereco) {
        this.nome = nome;
        this.idade = idade;
        this.endereco = endereco;
    }

    @Override
    public String toString() {
        return nome + " (" + idade + " anos), Endereço: " + endereco;
    }
}
""",

    "src/app/Main.java": """package app;

import builder.PersonBuilder;
import modelos.Pessoa;

public class Main {
    public static void main(String[] args) {
        Pessoa pessoa = new PersonBuilder()
                .setNome("Carlos")
                .setIdade(40)
                .setEndereco("Av. Brasil", "São Paulo")
                .build();

        System.out.println("Pessoa criada via Builder:");
        System.out.println(pessoa);
    }
}
"""
}

def criar_projeto(caminho_base):
    print(f"\n📁 Criando projeto Builder em: {caminho_base}")
    for rel_path, conteudo in estrutura_projeto.items():
        caminho_completo = os.path.join(caminho_base, rel_path)
        os.makedirs(os.path.dirname(caminho_completo), exist_ok=True)
        with open(caminho_completo, "w", encoding="utf-8") as f:
            f.write(conteudo)
        print(f"  ✅ {rel_path}")

def main():
    print("=== Gerador de Projeto Java (Builder) ===")
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

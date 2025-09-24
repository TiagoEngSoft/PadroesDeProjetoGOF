import os

# Estrutura do projeto: caminho relativo → conteúdo do arquivo
estrutura_projeto = {
    "src/prototype/Cartao.java": """package prototype;

public interface Cartao {
    void exibirMensagem();
    Cartao clone();
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

    public Endereco(Endereco outro) {
        this.rua = outro.rua;
        this.cidade = outro.cidade;
    }

    public String getRua() {
        return rua;
    }

    public void setRua(String rua) {
        this.rua = rua;
    }

    public String getCidade() {
        return cidade;
    }

    public void setCidade(String cidade) {
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

    public Pessoa(Pessoa outra) {
        this.nome = outra.nome;
        this.idade = outra.idade;
        this.endereco = new Endereco(outra.endereco);
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public Endereco getEndereco() {
        return endereco;
    }

    public void setEndereco(Endereco endereco) {
        this.endereco = endereco;
    }

    @Override
    public String toString() {
        return nome + " (" + idade + " anos), " + endereco;
    }
}
""",

    "src/modelos/CartaoAniversario.java": """package modelos;

import prototype.Cartao;

public class CartaoAniversario implements Cartao {
    private String mensagem;
    private Pessoa destinatario;

    public CartaoAniversario(String mensagem, Pessoa destinatario) {
        this.mensagem = mensagem;
        this.destinatario = destinatario;
    }

    public CartaoAniversario(CartaoAniversario outro) {
        this.mensagem = outro.mensagem;
        this.destinatario = new Pessoa(outro.destinatario);
    }

    @Override
    public void exibirMensagem() {
        System.out.println("Cartão de Aniversário para " + destinatario + ": " + mensagem);
    }

    @Override
    public Cartao clone() {
        return new CartaoAniversario(this);
    }

    public Pessoa getDestinatario() {
        return destinatario;
    }
}
""",

    "src/app/Main.java": """package app;

import modelos.*;
import prototype.Cartao;

public class Main {
    public static void main(String[] args) {
        Endereco endereco = new Endereco("Rua das Flores", "São Paulo");
        Pessoa joao = new Pessoa("João", 30, endereco);

        Cartao cartaoOriginal = new CartaoAniversario("Feliz aniversário!", joao);

        Cartao cartaoClone = cartaoOriginal.clone();

        System.out.println("Original:");
        cartaoOriginal.exibirMensagem();

        System.out.println("Clone:");
        cartaoClone.exibirMensagem();

        Pessoa pessoaDoClone = ((CartaoAniversario) cartaoClone).getDestinatario();
        pessoaDoClone.setNome("Maria");
        pessoaDoClone.setIdade(25);
        pessoaDoClone.getEndereco().setRua("Avenida Brasil");
        pessoaDoClone.getEndereco().setCidade("Rio de Janeiro");

        System.out.println("\\nApós modificar o clone:");
        System.out.println("Original:");
        cartaoOriginal.exibirMensagem();

        System.out.println("Clone:");
        cartaoClone.exibirMensagem();
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
    print("=== Gerador de Projeto Java (Prototype com Deep Clone) ===")
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

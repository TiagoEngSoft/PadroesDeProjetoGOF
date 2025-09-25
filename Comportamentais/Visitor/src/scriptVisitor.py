import os

def criar_arquivo(caminho, conteudo):
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(conteudo)

def criar_projeto_visitor(base_path):
    # Criar estrutura de pastas
    src_path = os.path.join(base_path, 'src', 'visitor')
    os.makedirs(src_path, exist_ok=True)

    # Conteúdo dos arquivos Java
    elemento = '''package visitor;

// Interface Elemento, aceita visitor
public interface Elemento {
    void aceitar(Visitor visitor);
}
'''

    pessoa = '''package visitor;

public class Pessoa implements Elemento {
    private String nome;
    private int idade;

    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }

    @Override
    public void aceitar(Visitor visitor) {
        visitor.visitarPessoa(this);
    }
}
'''

    empresa = '''package visitor;

public class Empresa implements Elemento {
    private String nome;
    private int funcionarios;

    public Empresa(String nome, int funcionarios) {
        this.nome = nome;
        this.funcionarios = funcionarios;
    }

    public String getNome() {
        return nome;
    }

    public int getFuncionarios() {
        return funcionarios;
    }

    @Override
    public void aceitar(Visitor visitor) {
        visitor.visitarEmpresa(this);
    }
}
'''

    visitor_interface = '''package visitor;

// Interface Visitor declara métodos para visitar cada tipo de elemento
public interface Visitor {
    void visitarPessoa(Pessoa pessoa);
    void visitarEmpresa(Empresa empresa);
}
'''

    visitor_impl = '''package visitor;

public class ImpressaoVisitor implements Visitor {

    @Override
    public void visitarPessoa(Pessoa pessoa) {
        System.out.println("Visitando Pessoa: " + pessoa.getNome() + ", idade: " + pessoa.getIdade());
    }

    @Override
    public void visitarEmpresa(Empresa empresa) {
        System.out.println("Visitando Empresa: " + empresa.getNome() + ", funcionários: " + empresa.getFuncionarios());
    }
}
'''

    main_java = '''import visitor.*;

public class Main {
    public static void main(String[] args) {
        Elemento[] elementos = {
            new Pessoa("Alice", 30),
            new Empresa("OpenAI", 500)
        };

        Visitor visitor = new ImpressaoVisitor();

        for (Elemento e : elementos) {
            e.aceitar(visitor);
        }
    }
}
'''

    # Criar arquivos
    criar_arquivo(os.path.join(src_path, 'Elemento.java'), elemento)
    criar_arquivo(os.path.join(src_path, 'Pessoa.java'), pessoa)
    criar_arquivo(os.path.join(src_path, 'Empresa.java'), empresa)
    criar_arquivo(os.path.join(src_path, 'Visitor.java'), visitor_interface)
    criar_arquivo(os.path.join(src_path, 'ImpressaoVisitor.java'), visitor_impl)
    criar_arquivo(os.path.join(base_path, 'src', 'Main.java'), main_java)

def main():
    print("=== Criador do projeto Visitor em Java ===")
    base_path = input("Informe o caminho onde o projeto será salvo (ex: C:\\Users\\Usuario\\Desktop\\Visitor): ").strip()

    if not base_path:
        print("Caminho inválido. Saindo.")
        return

    try:
        criar_projeto_visitor(base_path)
        print(f"\nProjeto criado com sucesso em: {base_path}\\src")
        print("""
Estrutura gerada:

src/
├── visitor/
│   ├── Elemento.java
│   ├── Pessoa.java
│   ├── Empresa.java
│   ├── Visitor.java
│   └── ImpressaoVisitor.java
└── Main.java

- Elemento.java: interface para elementos que aceitam visitor.
- Pessoa.java e Empresa.java: implementações concretas de Elemento.
- Visitor.java: interface visitor.
- ImpressaoVisitor.java: implementação do visitor que imprime detalhes.
- Main.java: testa o padrão visitor.
""")
    except Exception as e:
        print(f"Erro ao criar o projeto: {e}")

    input("Pressione Enter para fechar o terminal...")

if __name__ == "__main__":
    main()

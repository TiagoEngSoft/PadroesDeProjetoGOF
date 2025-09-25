import os

def criar_arquivo(caminho, conteudo):
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(conteudo)

def criar_projeto_template_method(base_path):
    # Criar estrutura de pastas
    src_path = os.path.join(base_path, 'src', 'template_method')
    os.makedirs(src_path, exist_ok=True)

    # Conteúdo dos arquivos Java
    relatorio = '''package template_method;

// Classe abstrata com o método template
public abstract class Relatorio {

    // Método template: define a sequência de passos
    public final void gerarRelatorio() {
        coletarDados();
        formatarDados();
        imprimirRelatorio();
        salvarRelatorio();
    }

    // Passos que podem variar entre os relatórios
    protected abstract void coletarDados();
    protected abstract void formatarDados();

    // Passos fixos para todos os relatórios
    private void imprimirRelatorio() {
        System.out.println("Imprimindo relatório...");
    }

    private void salvarRelatorio() {
        System.out.println("Salvando relatório no disco.");
    }
}
'''

    relatorio_vendas = '''package template_method;

public class RelatorioVendas extends Relatorio {

    @Override
    protected void coletarDados() {
        System.out.println("Coletando dados de vendas do sistema.");
    }

    @Override
    protected void formatarDados() {
        System.out.println("Formatando dados de vendas para relatório.");
    }
}
'''

    relatorio_estoque = '''package template_method;

public class RelatorioEstoque extends Relatorio {

    @Override
    protected void coletarDados() {
        System.out.println("Coletando dados de estoque do sistema.");
    }

    @Override
    protected void formatarDados() {
        System.out.println("Formatando dados de estoque para relatório.");
    }
}
'''

    main_java = '''import template_method.*;

public class Main {
    public static void main(String[] args) {
        Relatorio relatorioVendas = new RelatorioVendas();
        Relatorio relatorioEstoque = new RelatorioEstoque();

        System.out.println("Gerando relatório de vendas:");
        relatorioVendas.gerarRelatorio();

        System.out.println("\\nGerando relatório de estoque:");
        relatorioEstoque.gerarRelatorio();
    }
}
'''

    # Criar arquivos
    criar_arquivo(os.path.join(src_path, 'Relatorio.java'), relatorio)
    criar_arquivo(os.path.join(src_path, 'RelatorioVendas.java'), relatorio_vendas)
    criar_arquivo(os.path.join(src_path, 'RelatorioEstoque.java'), relatorio_estoque)
    criar_arquivo(os.path.join(base_path, 'src', 'Main.java'), main_java)

def main():
    print("=== Criador do projeto Template Method em Java ===")
    base_path = input("Informe o caminho onde o projeto será salvo (ex: C:\\Users\\Usuario\\Desktop\\TemplateMethod): ").strip()

    if not base_path:
        print("Caminho inválido. Saindo.")
        return

    try:
        criar_projeto_template_method(base_path)
        print(f"\nProjeto criado com sucesso em: {base_path}\\src")
        print("""
Estrutura gerada:

src/
├── template_method/
│   ├── Relatorio.java
│   ├── RelatorioVendas.java
│   └── RelatorioEstoque.java
└── Main.java

- Relatorio.java: classe abstrata com o método template.
- RelatorioVendas.java e RelatorioEstoque.java: implementações específicas.
- Main.java: classe para testar o padrão Template Method.
""")
    except Exception as e:
        print(f"Erro ao criar o projeto: {e}")

    input("Pressione Enter para fechar o terminal...")

if __name__ == "__main__":
    main()

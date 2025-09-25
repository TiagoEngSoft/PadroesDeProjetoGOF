import template_method.*;

public class Main {
    public static void main(String[] args) {
        Relatorio relatorioVendas = new RelatorioVendas();
        Relatorio relatorioEstoque = new RelatorioEstoque();

        System.out.println("Gerando relatório de vendas:");
        relatorioVendas.gerarRelatorio();

        System.out.println("\nGerando relatório de estoque:");
        relatorioEstoque.gerarRelatorio();
    }
}

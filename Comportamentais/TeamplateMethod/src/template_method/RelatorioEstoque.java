package template_method;

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

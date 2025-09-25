package template_method;

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

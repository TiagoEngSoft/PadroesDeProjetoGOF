package template_method;

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

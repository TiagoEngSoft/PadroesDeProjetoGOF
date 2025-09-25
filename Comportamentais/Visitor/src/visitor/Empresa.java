package visitor;

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

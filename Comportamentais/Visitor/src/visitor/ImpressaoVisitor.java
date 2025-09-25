package visitor;

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

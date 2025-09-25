package visitor;

// Interface Visitor declara métodos para visitar cada tipo de elemento
public interface Visitor {
    void visitarPessoa(Pessoa pessoa);
    void visitarEmpresa(Empresa empresa);
}

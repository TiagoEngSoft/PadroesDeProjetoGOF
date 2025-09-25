package visitor;

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

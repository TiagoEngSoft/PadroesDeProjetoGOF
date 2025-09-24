package builder;

import modelos.Endereco;
import modelos.Pessoa;

public class PersonBuilder {
    private String nome;
    private int idade;
    private Endereco endereco;

    public PersonBuilder setNome(String nome) {
        this.nome = nome;
        return this;
    }

    public PersonBuilder setIdade(int idade) {
        this.idade = idade;
        return this;
    }

    public PersonBuilder setEndereco(String rua, String cidade) {
        this.endereco = new Endereco(rua, cidade);
        return this;
    }

    public Pessoa build() {
        return new Pessoa(nome, idade, endereco);
    }
}

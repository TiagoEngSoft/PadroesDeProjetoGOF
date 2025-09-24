package app;

import builder.PersonBuilder;
import modelos.Pessoa;

public class Main {
    public static void main(String[] args) {
        Pessoa pessoa = new PersonBuilder()
                .setNome("Carlos")
                .setIdade(40)
                .setEndereco("Av. Brasil", "São Paulo")
                .build();

        System.out.println("Pessoa criada via Builder:");
        System.out.println(pessoa);
    }
}

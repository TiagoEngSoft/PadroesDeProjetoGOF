package app;

import modelos.*;
import prototype.Cartao;

public class Main {
    public static void main(String[] args) {
        Endereco endereco = new Endereco("Rua das Flores", "São Paulo");
        Pessoa joao = new Pessoa("João", 30, endereco);

        Cartao cartaoOriginal = new CartaoAniversario("Feliz aniversário!", joao);

        Cartao cartaoClone = cartaoOriginal.clone();

        System.out.println("Original:");
        cartaoOriginal.exibirMensagem();

        System.out.println("Clone:");
        cartaoClone.exibirMensagem();

        Pessoa pessoaDoClone = ((CartaoAniversario) cartaoClone).getDestinatario();
        pessoaDoClone.setNome("Maria");
        pessoaDoClone.setIdade(25);
        pessoaDoClone.getEndereco().setRua("Avenida Brasil");
        pessoaDoClone.getEndereco().setCidade("Rio de Janeiro");

        System.out.println("\nApós modificar o clone:");
        System.out.println("Original:");
        cartaoOriginal.exibirMensagem();

        System.out.println("Clone:");
        cartaoClone.exibirMensagem();
    }
}

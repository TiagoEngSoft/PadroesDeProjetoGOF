package modelos;

import prototype.Cartao;

public class CartaoAniversario implements Cartao {
    private String mensagem;
    private Pessoa destinatario;

    public CartaoAniversario(String mensagem, Pessoa destinatario) {
        this.mensagem = mensagem;
        this.destinatario = destinatario;
    }

    public CartaoAniversario(CartaoAniversario outro) {
        this.mensagem = outro.mensagem;
        this.destinatario = new Pessoa(outro.destinatario);
    }

    @Override
    public void exibirMensagem() {
        System.out.println("Cartão de Aniversário para " + destinatario + ": " + mensagem);
    }

    @Override
    public Cartao clone() {
        return new CartaoAniversario(this);
    }

    public Pessoa getDestinatario() {
        return destinatario;
    }
}

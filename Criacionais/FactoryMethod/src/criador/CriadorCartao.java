package criador;

import cartao.Cartao;

public abstract class CriadorCartao {
    public abstract Cartao criarCartao();

    public void enviarCartao() {
        Cartao cartao = criarCartao();
        cartao.exibirMensagem();
    }
}

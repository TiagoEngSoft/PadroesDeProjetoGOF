package simples;

import fabrica.FabricaCartao;
import cartao.CartaoAniversario;
import cartao.CartaoNatal;

public class FabricaCartaoSimples implements FabricaCartao {
    public CartaoAniversario criarCartaoAniversario() {
        return new CartaoAniversarioSimples();
    }

    public CartaoNatal criarCartaoNatal() {
        return new CartaoNatalSimples();
    }
}

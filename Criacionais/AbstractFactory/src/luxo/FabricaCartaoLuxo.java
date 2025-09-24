package luxo;

import fabrica.FabricaCartao;
import cartao.CartaoAniversario;
import cartao.CartaoNatal;

public class FabricaCartaoLuxo implements FabricaCartao {
    public CartaoAniversario criarCartaoAniversario() {
        return new CartaoAniversarioLuxo();
    }

    public CartaoNatal criarCartaoNatal() {
        return new CartaoNatalLuxo();
    }
}

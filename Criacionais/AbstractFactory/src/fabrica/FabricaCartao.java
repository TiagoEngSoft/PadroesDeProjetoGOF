package fabrica;

import cartao.CartaoAniversario;
import cartao.CartaoNatal;

public interface FabricaCartao {
    CartaoAniversario criarCartaoAniversario();
    CartaoNatal criarCartaoNatal();
}

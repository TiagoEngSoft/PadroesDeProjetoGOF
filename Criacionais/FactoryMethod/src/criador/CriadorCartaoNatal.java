package criador;

import cartao.Cartao;
import cartao.CartaoNatal;

public class CriadorCartaoNatal extends CriadorCartao {
    public Cartao criarCartao() {
        return new CartaoNatal();
    }
}

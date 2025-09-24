package criador;

import cartao.Cartao;
import cartao.CartaoAniversario;

public class CriadorCartaoAniversario extends CriadorCartao {
    public Cartao criarCartao() {
        return new CartaoAniversario();
    }
}

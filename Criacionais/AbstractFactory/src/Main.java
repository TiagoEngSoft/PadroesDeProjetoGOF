package app;

import fabrica.FabricaCartao;
import simples.FabricaCartaoSimples;
import luxo.FabricaCartaoLuxo;
import cartao.CartaoAniversario;
import cartao.CartaoNatal;

public class Main {
    public static void main(String[] args) {
        
        System.out.println("Usando Cartões SIMPLES:");
        FabricaCartao fabricaSimples = new FabricaCartaoSimples();
        CartaoAniversario aniversarioSimples = fabricaSimples.criarCartaoAniversario();
        CartaoNatal natalSimples = fabricaSimples.criarCartaoNatal();
        aniversarioSimples.exibirMensagem();
        natalSimples.exibirMensagem();

        System.out.println("\nUsando Cartões LUXO:");
        FabricaCartao fabricaLuxo = new FabricaCartaoLuxo();
        CartaoAniversario aniversarioLuxo = fabricaLuxo.criarCartaoAniversario();
        CartaoNatal natalLuxo = fabricaLuxo.criarCartaoNatal();
        aniversarioLuxo.exibirMensagem();
        natalLuxo.exibirMensagem();
    }
}

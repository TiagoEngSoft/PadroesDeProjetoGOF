package br.com.empresa.chain.responsaveis;

import br.com.empresa.chain.Chamado;

public class Atendente extends Responsavel {
    @Override
    public void tratarChamado(Chamado chamado) {
        if (chamado.getDescricao().toLowerCase().contains("senha")) {
            System.out.println("Atendente resolveu o problema: " + chamado.getDescricao());
        } else if (proximo != null) {
            proximo.tratarChamado(chamado);
        } else {
            System.out.println("Ninguém conseguiu resolver: " + chamado.getDescricao());
        }
    }
}

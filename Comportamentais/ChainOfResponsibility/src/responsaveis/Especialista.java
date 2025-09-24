package br.com.empresa.chain.responsaveis;

import br.com.empresa.chain.Chamado;

public class Especialista extends Responsavel {
    @Override
    public void tratarChamado(Chamado chamado) {
        System.out.println("Especialista resolveu o problema: " + chamado.getDescricao());
    }
}

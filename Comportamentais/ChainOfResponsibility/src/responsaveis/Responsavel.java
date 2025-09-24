package br.com.empresa.chain.responsaveis;

import br.com.empresa.chain.Chamado;

public abstract class Responsavel {
    protected Responsavel proximo;

    public void setProximo(Responsavel proximo) {
        this.proximo = proximo;
    }

    public abstract void tratarChamado(Chamado chamado);
}

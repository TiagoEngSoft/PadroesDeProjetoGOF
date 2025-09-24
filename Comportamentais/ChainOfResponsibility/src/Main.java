package br.com.empresa.chain;

import br.com.empresa.chain.responsaveis.*;

public class Main {
    public static void main(String[] args) {
        Responsavel atendente = new Atendente();
        Responsavel suporte = new SuporteTecnico();
        Responsavel especialista = new Especialista();

        atendente.setProximo(suporte);
        suporte.setProximo(especialista);

        Chamado chamado1 = new Chamado("Esqueci minha senha");
        Chamado chamado2 = new Chamado("Não consigo conectar ao sistema");
        Chamado chamado3 = new Chamado("Erro crítico no banco de dados");

        System.out.println("Processando chamados...\n");

        atendente.tratarChamado(chamado1);
        atendente.tratarChamado(chamado2);
        atendente.tratarChamado(chamado3);
    }
}

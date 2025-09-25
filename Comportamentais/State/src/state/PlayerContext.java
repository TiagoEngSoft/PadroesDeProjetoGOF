package state;

public class PlayerContext {
    private State estadoAtual;

    public PlayerContext() {
        // Começa em modo pausado
        this.estadoAtual = new PausedState();
    }

    public void setState(State novoEstado) {
        this.estadoAtual = novoEstado;
    }

    public void pressionarBotao() {
        estadoAtual.pressionarBotao(this);
    }
}

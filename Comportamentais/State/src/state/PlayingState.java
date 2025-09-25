package state;

public class PlayingState implements State {
    @Override
    public void pressionarBotao(PlayerContext context) {
        System.out.println("⏸️ Pausando música...");
        context.setState(new PausedState());
    }
}

package state;

public class PausedState implements State {
    @Override
    public void pressionarBotao(PlayerContext context) {
        System.out.println("▶️ Retomando música...");
        context.setState(new PlayingState());
    }
}

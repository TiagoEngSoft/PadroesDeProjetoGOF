import state.*;

public class Main {
    public static void main(String[] args) {
        PlayerContext player = new PlayerContext();

        System.out.println("🎵 Simulador de botão Play/Pause:
");

        player.pressionarBotao(); // Deve iniciar reprodução
        player.pressionarBotao(); // Deve pausar
        player.pressionarBotao(); // Deve reproduzir
    }
}

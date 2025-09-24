import sistema.SistemaAudio;
import sistema.SistemaVideo;
import sistema.SistemaRede;

public class HomeTheaterFacade {
    private SistemaAudio audio;
    private SistemaVideo video;
    private SistemaRede rede;

    public HomeTheaterFacade() {
        audio = new SistemaAudio();
        video = new SistemaVideo();
        rede = new SistemaRede();
    }

    public void ligarSistema() {
        audio.ligarAudio();
        video.ligarVideo();
        rede.conectarInternet();
        System.out.println("Sistema de Home Theater pronto para uso!");
    }

    public void desligarSistema() {
        audio.desligarAudio();
        video.desligarVideo();
        rede.desconectarInternet();
        System.out.println("Sistema de Home Theater desligado.");
    }
}

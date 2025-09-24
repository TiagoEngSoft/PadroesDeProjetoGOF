import proxy.Video;
import proxy.VideoProxy;

public class Main {
    public static void main(String[] args) {
        Video video = new VideoProxy("filme-super-hd.mp4");

        System.out.println("🎬 Primeiro acesso:");
        video.reproduzir(); // Aqui o vídeo é carregado e reproduzido

        System.out.println("\n⏯️ Segundo acesso:");
        video.reproduzir(); // Aqui só é reproduzido (sem carregar novamente)
    }
}

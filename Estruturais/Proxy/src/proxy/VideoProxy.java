public class VideoProxy implements Video {
    private String nomeArquivo;
    private VideoReal videoReal;

    public VideoProxy(String nomeArquivo) {
        this.nomeArquivo = nomeArquivo;
    }

    public void reproduzir() {
        if (videoReal == null) {
            videoReal = new VideoReal(nomeArquivo); // Carrega somente na primeira vez
        }
        videoReal.reproduzir();
    }
}

public class VideoReal implements Video {
    private String nomeArquivo;

    public VideoReal(String nomeArquivo) {
        this.nomeArquivo = nomeArquivo;
        carregarDoDisco(nomeArquivo);
    }

    private void carregarDoDisco(String nome) {
        System.out.println("🔄 Carregando vídeo: " + nome);
    }

    public void reproduzir() {
        System.out.println("▶️ Reproduzindo vídeo: " + nomeArquivo);
    }
}

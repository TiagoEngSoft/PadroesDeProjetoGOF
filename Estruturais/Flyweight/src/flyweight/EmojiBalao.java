public class EmojiBalao {
    private final String emoji = "🎈";

    public void desenhar(int x, int y, String cor) {
        System.out.println("Desenhando balão " + emoji +
                           " na posição (" + x + "," + y + ") com a cor " + cor);
    }
}

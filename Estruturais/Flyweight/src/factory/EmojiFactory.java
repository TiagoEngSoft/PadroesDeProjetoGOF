import java.util.HashMap;

public class EmojiFactory {
    private static final HashMap<String, EmojiBalao> cache = new HashMap<>();

    public static EmojiBalao getBalao(String cor) {
        EmojiBalao balao = cache.get(cor);
        if (balao == null) {
            balao = new EmojiBalao();
            cache.put(cor, balao);
            System.out.println("🎨 Criando novo objeto EmojiBalão para a cor: " + cor);
        }
        return balao;
    }
}

import os

estrutura_projeto = {
    # Interfaces
    "src/interfaces/Cordeiro.java": """package interfaces;

public interface Cordeiro {
    void balir();
}
""",
    "src/interfaces/Lobo.java": """package interfaces;

public interface Lobo {
    void uivar();
    void atacar();
}
""",

    # Implementações reais
    "src/animais/CordeiroReal.java": """package animais;

import interfaces.Cordeiro;

public class CordeiroReal implements Cordeiro {
    @Override
    public void balir() {
        System.out.println("🐑 Meeeeeee!");
    }
}
""",
    "src/animais/LoboReal.java": """package animais;

import interfaces.Lobo;

public class LoboReal implements Lobo {
    @Override
    public void uivar() {
        System.out.println("🐺 Auuuuuuuu!");
    }

    @Override
    public void atacar() {
        System.out.println("⚠️ O lobo ataca ferozmente!");
    }
}
""",

    # Adapters
    "src/adapter/LoboEmPeleDeCordeiro.java": """package adapter;

import interfaces.Cordeiro;
import interfaces.Lobo;

public class LoboEmPeleDeCordeiro implements Cordeiro {
    private Lobo lobo;

    public LoboEmPeleDeCordeiro(Lobo lobo) {
        this.lobo = lobo;
    }

    @Override
    public void balir() {
        System.out.println("😇 Meeee... (parece dócil, mas...)");
        lobo.uivar();
        lobo.atacar();
    }
}
""",
    "src/adapter/CordeiroEmPeleDeLobo.java": """package adapter;

import interfaces.Cordeiro;
import interfaces.Lobo;

public class CordeiroEmPeleDeLobo implements Lobo {
    private Cordeiro cordeiro;

    public CordeiroEmPeleDeLobo(Cordeiro cordeiro) {
        this.cordeiro = cordeiro;
    }

    @Override
    public void uivar() {
        System.out.println("😅 Auuu... (mas é só um cordeiro tentando)");
    }

    @Override
    public void atacar() {
        System.out.println("🐑 Tentando atacar... mas só sabe balir:");
        cordeiro.balir();
    }
}
""",

    # Main
    "src/app/Main.java": """package app;

import interfaces.Cordeiro;
import interfaces.Lobo;
import animais.CordeiroReal;
import animais.LoboReal;
import adapter.LoboEmPeleDeCordeiro;
import adapter.CordeiroEmPeleDeLobo;

public class Main {
    public static void main(String[] args) {

        System.out.println("=== 🐺 Lobo em pele de cordeiro ===");
        Lobo loboReal = new LoboReal();
        Cordeiro loboDisfarçado = new LoboEmPeleDeCordeiro(loboReal);
        loboDisfarçado.balir();

        System.out.println("\\n=== 🐑 Cordeiro em pele de lobo ===");
        Cordeiro cordeiroReal = new CordeiroReal();
        Lobo cordeiroDisfarçado = new CordeiroEmPeleDeLobo(cordeiroReal);
        cordeiroDisfarçado.uivar();
        cordeiroDisfarçado.atacar();
    }
}
"""
}

def criar_projeto(caminho_base):
    for caminho, conteudo in estrutura_projeto.items():
        caminho_completo = os.path.join(caminho_base, caminho)
        os.makedirs(os.path.dirname(caminho_completo), exist_ok=True)
        with open(caminho_completo, "w", encoding="utf-8") as f:
            f.write(conteudo)
    print(f"✅ Projeto criado em: {os.path.abspath(caminho_base)}")

if __name__ == "__main__":
    destino = input("📁 Informe o caminho onde deseja criar o projeto (ex: C:/Users/SeuUsuario/Desktop/projeto_adapter): ").strip()
    if destino:
        criar_projeto(destino)
        input("✅ Pressione ENTER para sair...")
    else:
        print("❌ Caminho inválido.")

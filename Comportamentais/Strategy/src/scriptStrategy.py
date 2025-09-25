import os

# Arquivos Java

strategy_java = '''\
package strategy;

public interface DescontoStrategy {
    double calcular(double precoOriginal);
}
'''

desconto_fixo_java = '''\
package strategy;

public class DescontoFixo implements DescontoStrategy {
    private double percentual;

    public DescontoFixo(double percentual) {
        this.percentual = percentual;
    }

    @Override
    public double calcular(double precoOriginal) {
        return precoOriginal * (1 - percentual);
    }
}
'''

sem_desconto_java = '''\
package strategy;

public class SemDesconto implements DescontoStrategy {
    @Override
    public double calcular(double precoOriginal) {
        return precoOriginal; // Sem desconto
    }
}
'''

pedido_java = '''\
package strategy;

public class Pedido {
    private double precoOriginal;
    private DescontoStrategy estrategia;

    public Pedido(double precoOriginal, DescontoStrategy estrategia) {
        this.precoOriginal = precoOriginal;
        this.estrategia = estrategia;
    }

    public double getPrecoFinal() {
        return estrategia.calcular(precoOriginal);
    }

    public void setEstrategia(DescontoStrategy novaEstrategia) {
        this.estrategia = novaEstrategia;
    }
}
'''

main_java = '''\
import strategy.*;

public class Main {
    public static void main(String[] args) {
        Pedido pedido = new Pedido(100.0, new SemDesconto());

        System.out.println("🧾 Preço original: R$100.00");
        System.out.println("🔸 Sem desconto: R$" + pedido.getPrecoFinal());

        pedido.setEstrategia(new DescontoFixo(0.1));
        System.out.println("🔸 Desconto de 10%: R$" + pedido.getPrecoFinal());

        pedido.setEstrategia(new DescontoFixo(0.25));
        System.out.println("🔸 Desconto de 25%: R$" + pedido.getPrecoFinal());
    }
}
'''

# Arquivos a serem criados
arquivos = {
    "strategy/DescontoStrategy.java": strategy_java,
    "strategy/DescontoFixo.java": desconto_fixo_java,
    "strategy/SemDesconto.java": sem_desconto_java,
    "strategy/Pedido.java": pedido_java,
    "Main.java": main_java,
}


def criar_projeto(path_base):
    print(f"\n🛠️ Criando projeto Strategy em: {path_base}\n")

    for caminho_relativo, conteudo in arquivos.items():
        caminho_completo = os.path.join(path_base, caminho_relativo)
        os.makedirs(os.path.dirname(caminho_completo), exist_ok=True)
        with open(caminho_completo, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        print(f"✅ Criado: {caminho_relativo}")

    print("\n📦 Projeto Java com padrão Strategy criado com sucesso!")
    print(f"📁 Local: {os.path.abspath(path_base)}")
    print("\nPressione ENTER para sair...")
    input()


if __name__ == "__main__":
    print("🧠 Criador de Projeto Java - Padrão Strategy\n")
    destino = input("📂 Digite o caminho onde o projeto deve ser salvo: ").strip()

    if not destino:
        print("❌ Caminho inválido.")
    else:
        criar_projeto(destino)

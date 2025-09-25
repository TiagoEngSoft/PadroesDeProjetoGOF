import os

# Conteúdo dos arquivos Java

component_java = '''\
package components;

public interface Component {
    void setMediator(mediator.Mediator mediator);
    String getName();
}
'''

textbox_java = '''\
package components;

import mediator.Mediator;

public class TextBox implements Component {
    private Mediator mediator;
    private String text = "";

    public void setText(String text) {
        this.text = text;
        mediator.notify(this, "textChanged");
    }

    public String getText() {
        return text;
    }

    @Override
    public void setMediator(Mediator mediator) {
        this.mediator = mediator;
    }

    @Override
    public String getName() {
        return "TextBox";
    }
}
'''

checkbox_java = '''\
package components;

import mediator.Mediator;

public class CheckBox implements Component {
    private Mediator mediator;
    private boolean checked = false;

    public void setChecked(boolean checked) {
        this.checked = checked;
        mediator.notify(this, "checkChanged");
    }

    public boolean isChecked() {
        return checked;
    }

    @Override
    public void setMediator(Mediator mediator) {
        this.mediator = mediator;
    }

    @Override
    public String getName() {
        return "CheckBox";
    }
}
'''

button_java = '''\
package components;

import mediator.Mediator;

public class Button implements Component {
    private Mediator mediator;
    private boolean enabled = false;

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
        System.out.println("Botão agora está " + (enabled ? "ATIVADO" : "DESATIVADO"));
    }

    @Override
    public void setMediator(Mediator mediator) {
        this.mediator = mediator;
    }

    @Override
    public String getName() {
        return "Button";
    }
}
'''

mediator_java = '''\
package mediator;

import components.Component;

public interface Mediator {
    void notify(Component sender, String event);
}
'''

form_mediator_java = '''\
package mediator;

import components.Button;
import components.CheckBox;
import components.Component;
import components.TextBox;

public class FormMediator implements Mediator {
    private TextBox textBox;
    private CheckBox checkBox;
    private Button button;

    public void setComponents(TextBox textBox, CheckBox checkBox, Button button) {
        this.textBox = textBox;
        this.checkBox = checkBox;
        this.button = button;

        textBox.setMediator(this);
        checkBox.setMediator(this);
        button.setMediator(this);
    }

    @Override
    public void notify(Component sender, String event) {
        if (event.equals("textChanged") || event.equals("checkChanged")) {
            boolean isEmailValid = textBox.getText().contains("@");
            boolean isChecked = checkBox.isChecked();

            button.setEnabled(isEmailValid && isChecked);
        }
    }
}
'''

main_java = '''\
import components.*;
import mediator.*;

public class Main {
    public static void main(String[] args) {
        // Criando os componentes
        TextBox emailInput = new TextBox();
        CheckBox termsCheck = new CheckBox();
        Button sendButton = new Button();

        // Criando e configurando o Mediador
        FormMediator mediator = new FormMediator();
        mediator.setComponents(emailInput, termsCheck, sendButton);

        // Simulando interações do usuário
        System.out.println("Usuário digita email inválido:");
        emailInput.setText("emailinvalido");

        System.out.println("\\nUsuário aceita os termos:");
        termsCheck.setChecked(true);

        System.out.println("\\nUsuário corrige o email:");
        emailInput.setText("usuario@exemplo.com");

        System.out.println("\\nUsuário desmarca os termos:");
        termsCheck.setChecked(false);
    }
}
'''

# Mapeamento de arquivos para salvar
arquivos = {
    'components/Component.java': component_java,
    'components/TextBox.java': textbox_java,
    'components/CheckBox.java': checkbox_java,
    'components/Button.java': button_java,
    'mediator/Mediator.java': mediator_java,
    'mediator/FormMediator.java': form_mediator_java,
    'Main.java': main_java,
}


def criar_projeto(path_base):
    print(f"\n🔧 Criando projeto em: {path_base}\n")

    for caminho_relativo, conteudo in arquivos.items():
        caminho_completo = os.path.join(path_base, caminho_relativo)
        pasta = os.path.dirname(caminho_completo)

        os.makedirs(pasta, exist_ok=True)
        with open(caminho_completo, 'w', encoding='utf-8') as f:
            f.write(conteudo)

        print(f"✅ Criado: {caminho_relativo}")

    print("\n📦 Projeto Mediator Java criado com sucesso!")
    print(f"\n📁 Estrutura salva em: {os.path.abspath(path_base)}")
    print("\nPressione ENTER para sair...")
    input()


# Execução
if __name__ == "__main__":
    print("🛠️  Criador de Projeto Java - Padrão Mediator\n")
    path = input("📂 Digite o caminho onde o projeto deve ser salvo: ").strip()

    if not path:
        print("❌ Caminho inválido. Encerrando.")
    else:
        criar_projeto(path)

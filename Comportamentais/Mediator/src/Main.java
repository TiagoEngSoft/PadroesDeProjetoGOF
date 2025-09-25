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

        System.out.println("\nUsuário aceita os termos:");
        termsCheck.setChecked(true);

        System.out.println("\nUsuário corrige o email:");
        emailInput.setText("usuario@exemplo.com");

        System.out.println("\nUsuário desmarca os termos:");
        termsCheck.setChecked(false);
    }
}

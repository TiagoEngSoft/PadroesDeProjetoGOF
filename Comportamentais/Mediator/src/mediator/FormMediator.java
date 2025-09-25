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

package mediator;

import components.Component;

public interface Mediator {
    void notify(Component sender, String event);
}

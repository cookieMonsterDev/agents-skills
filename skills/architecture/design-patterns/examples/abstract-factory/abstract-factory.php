<?php
// Abstract Factory pattern in PHP.
//
// Interfaces model products and the factory. Note: with first-class
// callables and arrays, a lighter idiom is an array of closures per family;
// the interface version scales better for large families.

declare(strict_types=1);

interface Button
{
    public function render(): string;
}

interface Checkbox
{
    public function render(): string;
}

final class MacButton implements Button
{
    public function render(): string
    {
        return '( OK )  // rounded macOS button';
    }
}

final class MacCheckbox implements Checkbox
{
    public function render(): string
    {
        return '◉ Remember me  // macOS checkbox';
    }
}

final class WindowsButton implements Button
{
    public function render(): string
    {
        return '[ OK ]  // rectangular Windows button';
    }
}

final class WindowsCheckbox implements Checkbox
{
    public function render(): string
    {
        return '[x] Remember me  // Windows checkbox';
    }
}

/** One creation method per product kind; products are guaranteed to match. */
interface WidgetFactory
{
    public function createButton(): Button;

    public function createCheckbox(): Checkbox;
}

final class MacFactory implements WidgetFactory
{
    public function createButton(): Button
    {
        return new MacButton();
    }

    public function createCheckbox(): Checkbox
    {
        return new MacCheckbox();
    }
}

final class WindowsFactory implements WidgetFactory
{
    public function createButton(): Button
    {
        return new WindowsButton();
    }

    public function createCheckbox(): Checkbox
    {
        return new WindowsCheckbox();
    }
}

/** Client code: depends only on the abstract factory and products. */
function renderDialog(WidgetFactory $factory): void
{
    echo $factory->createButton()->render(), PHP_EOL;
    echo $factory->createCheckbox()->render(), PHP_EOL;
}

foreach (['macOS' => new MacFactory(), 'Windows' => new WindowsFactory()] as $name => $factory) {
    echo "-- $name theme --", PHP_EOL;
    renderDialog($factory);
}

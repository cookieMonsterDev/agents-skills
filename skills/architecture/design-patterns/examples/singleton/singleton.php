<?php
// Singleton pattern in PHP.
//
// The classic form: private constructor, static instance, static accessor.
// Cloning and unserializing are blocked so the invariant holds. Modern PHP
// frameworks (Laravel, Symfony) prefer registering a shared service in the
// DI container — the class stays testable and only the wiring says "one".

declare(strict_types=1);

final class AppConfig
{
    private static ?AppConfig $instance = null;

    /** @var array<string, string> */
    private array $settings;

    private function __construct()
    {
        // Stands in for reading a config file once.
        echo 'Loading configuration (expensive, happens once)', PHP_EOL;
        $this->settings = [
            'app_name' => 'InventoryService',
            'db_url' => 'postgres://localhost/inventory',
            'log_level' => 'INFO',
        ];
    }

    public static function getInstance(): AppConfig
    {
        return self::$instance ??= new self();
    }

    public function get(string $key): string
    {
        return $this->settings[$key];
    }

    private function __clone()
    {
    }

    public function __wakeup(): void
    {
        throw new RuntimeException('Cannot unserialize a singleton');
    }
}

$a = AppConfig::getInstance();
$b = AppConfig::getInstance();

echo 'same instance: ', $a === $b ? 'true' : 'false', PHP_EOL;
echo 'app_name: ', $a->get('app_name'), PHP_EOL;
echo 'db_url: ', $b->get('db_url'), PHP_EOL;

// Template Method pattern in Go.
//
// Go has no inheritance, so the idiomatic form is composition: the
// template is a plain function that fixes the skeleton and takes an
// interface supplying the varying steps. This avoids the classic
// pattern's tight base-class coupling entirely.

package main

import "fmt"

type LineItem struct {
	Product string
	Units   int
	Price   float64
}

func (l LineItem) Subtotal() float64 {
	return float64(l.Units) * l.Price
}

// ReportSteps supplies only the varying steps.
type ReportSteps interface {
	Header() string
	Row(item LineItem) string
	Footer(total float64) string
}

// GenerateReport is the template method: iteration and totalling never vary.
func GenerateReport(steps ReportSteps, items []LineItem) string {
	out := steps.Header() + "\n"
	total := 0.0
	for _, item := range items {
		out += steps.Row(item) + "\n"
		total += item.Subtotal()
	}
	return out + steps.Footer(total)
}

type CsvReport struct{}

func (CsvReport) Header() string {
	return "product,units,price,subtotal"
}

func (CsvReport) Row(item LineItem) string {
	return fmt.Sprintf("%s,%d,%.2f,%.2f", item.Product, item.Units, item.Price, item.Subtotal())
}

func (CsvReport) Footer(total float64) string {
	return fmt.Sprintf("total,,,%.2f", total)
}

type MarkdownReport struct{}

func (MarkdownReport) Header() string {
	return "| Product | Units | Subtotal |\n| --- | --- | --- |"
}

func (MarkdownReport) Row(item LineItem) string {
	return fmt.Sprintf("| %s | %d | $%.2f |", item.Product, item.Units, item.Subtotal())
}

func (MarkdownReport) Footer(total float64) string {
	return fmt.Sprintf("\n**Total: $%.2f**", total)
}

func main() {
	items := []LineItem{
		{"Keyboard", 2, 80.00},
		{"Mouse", 1, 25.50},
		{"Monitor", 3, 210.00},
	}

	reports := []struct {
		name  string
		steps ReportSteps
	}{
		{"CsvReport", CsvReport{}},
		{"MarkdownReport", MarkdownReport{}},
	}

	for _, r := range reports {
		fmt.Printf("--- %s ---\n%s\n\n", r.name, GenerateReport(r.steps, items))
	}
}

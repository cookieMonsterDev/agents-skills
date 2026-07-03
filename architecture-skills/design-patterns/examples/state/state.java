// State pattern in Java.
//
// An enum is the idiomatic Java home for a fixed set of states: each
// constant overrides the behavior methods, and transitions assign a
// different constant. (Use separate classes instead when states need
// their own fields.)

public class state {

    enum MachineState {
        IDLE {
            @Override
            MachineState insertCoin(VendingMachine m) {
                System.out.println("coin accepted");
                return HAS_COIN;
            }

            @Override
            MachineState selectItem(VendingMachine m) {
                System.out.println("insert a coin first");
                return this;
            }
        },
        HAS_COIN {
            @Override
            MachineState insertCoin(VendingMachine m) {
                System.out.println("coin already inserted, returning it");
                return this;
            }

            @Override
            MachineState selectItem(VendingMachine m) {
                m.stock--;
                System.out.println("item dispensed (" + m.stock + " left)");
                return m.stock == 0 ? SOLD_OUT : IDLE;
            }
        },
        SOLD_OUT {
            @Override
            MachineState insertCoin(VendingMachine m) {
                System.out.println("sold out, returning coin");
                return this;
            }

            @Override
            MachineState selectItem(VendingMachine m) {
                System.out.println("sold out");
                return this;
            }
        };

        abstract MachineState insertCoin(VendingMachine m);
        abstract MachineState selectItem(VendingMachine m);
    }

    static final class VendingMachine {
        int stock;
        private MachineState state;

        VendingMachine(int stock) {
            this.stock = stock;
            this.state = stock > 0 ? MachineState.IDLE : MachineState.SOLD_OUT;
        }

        void insertCoin() {
            state = state.insertCoin(this);
        }

        void selectItem() {
            state = state.selectItem(this);
        }
    }

    public static void main(String[] args) {
        VendingMachine machine = new VendingMachine(2);
        machine.selectItem();  // insert a coin first
        machine.insertCoin();
        machine.insertCoin();  // coin already inserted
        machine.selectItem();  // item dispensed (1 left)
        machine.insertCoin();
        machine.selectItem();  // item dispensed (0 left)
        machine.insertCoin();  // sold out, returning coin
    }
}

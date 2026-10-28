// State pattern in Rust.
//
// An enum + match is the idiomatic Rust state machine: the compiler
// checks that every (state, event) pair is handled, and states can
// carry data in their variants. The GoF trait-object form
// (Box<dyn State> with a trait per behavior) exists too, but is only
// worth it when states are open-ended or defined across crates.

#[derive(Debug, Clone, Copy, PartialEq)]
enum MachineState {
    Idle,
    HasCoin,
    SoldOut,
}

struct VendingMachine {
    state: MachineState,
    stock: u32,
}

impl VendingMachine {
    fn new(stock: u32) -> Self {
        Self {
            state: if stock > 0 {
                MachineState::Idle
            } else {
                MachineState::SoldOut
            },
            stock,
        }
    }

    fn insert_coin(&mut self) {
        self.state = match self.state {
            MachineState::Idle => {
                println!("coin accepted");
                MachineState::HasCoin
            }
            MachineState::HasCoin => {
                println!("coin already inserted, returning it");
                MachineState::HasCoin
            }
            MachineState::SoldOut => {
                println!("sold out, returning coin");
                MachineState::SoldOut
            }
        };
    }

    fn select_item(&mut self) {
        self.state = match self.state {
            MachineState::Idle => {
                println!("insert a coin first");
                MachineState::Idle
            }
            MachineState::HasCoin => {
                self.stock -= 1;
                println!("item dispensed ({} left)", self.stock);
                if self.stock == 0 {
                    MachineState::SoldOut
                } else {
                    MachineState::Idle
                }
            }
            MachineState::SoldOut => {
                println!("sold out");
                MachineState::SoldOut
            }
        };
    }
}

fn main() {
    let mut machine = VendingMachine::new(2);
    machine.select_item(); // insert a coin first
    machine.insert_coin();
    machine.insert_coin(); // coin already inserted
    machine.select_item(); // item dispensed (1 left)
    machine.insert_coin();
    machine.select_item(); // item dispensed (0 left)
    machine.insert_coin(); // sold out, returning coin
}

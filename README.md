CS-216-TeamBlockBridges-Bitcoin_Scripting_

Bitcoin Script Comparison Old and New

A single test network shows how Bitcoin deals move step by step, handled through core tools and coded in Python. Behind each deal lies a hidden sequence - built, signed, sent, checked - all inside a private setup made for trials. What drives this task is curiosity about script mechanics tucked beneath surface actions. One path uses older formats tied to familiar patterns; another follows updated structures shaped differently under the hood.

Funds move through Bitcoin using a unique scripting system built on stacks. This setup checks if transfers meet specific rules before accepting them. Each transfer carries code spelling out exactly what must happen for money to be used. Code splits into pieces, each handling a different role in the process

Coins sit locked by rules written inside a scriptPubKey. These terms must match before moving money around. A spending key fits the lock like a physical key in a door. Without correct details, the network rejects the move. Conditions change based on setup - each one unique. Unlocking happens only when inputs satisfy what's coded. Rules guard every exit path for each coin held
A piece of code called the unlocking script supplies what's needed to meet the rules set by the locking script. It shows up before validation begins, carrying signatures or keys. Data inside it proves ownership during transaction checks. Instead of just linking parts, it activates the logic in the lock. When processed, it works together with the spending condition. Its role becomes clear only when paired correctly. Without matching details here, the transfer won’t go through

Once verification begins, the unlocking script runs alongside its matching lock. Should the result show TRUE at the end, validation passes. Running both scripts happens as one process. A correct outcome means approval.

Starting off, this project builds Legacy plus SegWit transactions from the ground up. Next comes breaking down each script step by step. Instead of just listing data, we look at size differences through actual decoding work. One key point stands out - SegWit cuts space needs in clear ways. Transaction weight shows a shift few noticed at first. Virtual size drops become obvious only after side-by-side checks. Efficiency gains emerge straight from the numbers, nothing added. The whole thing runs on real examples, not theory.

---

Team Members

Member Roll Number
|------|------|
Kumkum Kushwaha 240004028
Mhaske Prajwal Sanjay 240004033
Shruti Turare 240008029
Bhumika Kumari 240051006

---

Project Objective

This work looks into how Bitcoin deals get built, checking each step through Bitcoin Script. One path follows old-style transactions, another walks the newer SegWit version. Differences show up when counting data size, speed, and structure. What stands out comes from comparing their performance side by side. Each method reveals trade-offs shaped by design choices long ago.

The project aims to:

Create working P2PKH transactions
Create working SegWit P2SH-P2WPKH transactions
• Decode and analyze raw transaction scripts
Check script runs correctly with Bitcoin debugger
• Measure transaction size, weight, and virtual size
Legacy versus segwit transaction efficiency

Finding better ways to move data shows what SegWit can do - it streamlines transactions while cutting costs. Efficiency gains appear when changes take effect, dropping fees as a result of smarter design.

---

Background Concepts

Bitcoin Transactions

Ownership shifts happen when someone sends bitcoin from their address to another. Think of it like passing pieces of paper - each piece is an unspent result from earlier trades. These leftover bits aren’t kept in a bank-style account; they float around on the network. What counts is which past exchange created them - and who now holds the key. Each transfer builds on what was left unused before. The system checks old records to confirm new moves. Nothing gets erased, only updated through links between exchanges.

Each transaction consists of:

• Inputs – references to previous transaction outputs (UTXOs)
Coins head out in fresh directions, their paths shaped by updated rules. Where they land depends on how these new routes unfold. Movement follows a revised blueprint, shifting destinations without warning. Each step ahead ties back to changes behind the scenes. Direction bends with every adjustment made upstream
Outputs get spent based on rules written inside small programs. These little rule-sets decide exactly when a transaction can move forward. A program of this kind runs only if certain requirements are met first. Spending gets allowed once every condition lines up correctly. Such code lives within each output like a hidden key

Only when spent does a transaction's leftover amount turn into something called a UTXO. Until then, it just sits waiting.

---

Bitcoin Script

A script inside Bitcoin works like a line of steps that checks if payments are valid. Because it keeps things basic, the system stays safe and runs without surprises. Running on stacks means data piles up step by step during processing. Its design skips complex features so problems stay rare and clear. Complete flexibility was left out on purpose to avoid risky outcomes. Each piece follows strict rules so every result feels expected. Instead of allowing endless logic loops, only fixed paths work here. Security wins over advanced functions each time by default. It handles tasks one after another using simple building blocks. No extra layers appear because simplicity protects the whole chain.

Script execution works as follows:

1. A piece of code meant to unlock funds gets added to the stack first. This comes straight from the input section of a transaction record.
2. The code that locks the transaction gets added next - pulled straight from the earlier output.
3. Last one runs only after the first finishes. One follows the other without overlap.
4. Only when the last value on the stack equals true does validation pass.

Running the script looks like this example

```

Duplicate top stack item hash it compare with public key hash verify match then check signature
```

So the public key matches the address - plus, the signature checks out just right.

---

Transaction Types Implemented

Legacy Transactions (P2PKH)

P2PKH means Pay-to-Public-Key-Hash - this was how most Bitcoin transfers worked when the network first started. Though newer formats exist now, that setup laid the foundation for sending funds securely between users.

Locking Script:

```
Duplicate hash sixteen zero public key hash equal verify check signature
```

Unlocking Script:

```

```

Validation steps:

1. Duplicate public key
2. Turn the public key into a hash
3. Compare hash with expected address hash
4. Verify digital signature

Only when every test clears does the system accept the transfer.

---

SegWit Transactions (P2SH-P2WPKH)

Now here comes SegWit - meant to ease how Bitcoin handles growth while cleaning up flaws in transaction details. It reshapes data structure so signatures sit apart, making room for more activity without bloating blocks.

This time around, nesting SegWit shows up through P2SH-P2WPKH built right into the workflow. Backward compatibility comes along for older setups without skipping steps.

Key features:

• Signature data moved to the witness field
• Reduced transaction weight
• Lower transaction fees
• Fixes transaction malleability

Example locking script:

```
OP_HASH160  OP_EQUAL
```

Inside the witness part you will find these items

```


```

---

Project Structure

```
CS-216-TeamBlockBridges-Bitcoin_Scripting_

│
├── part1_legacy.py
│﻿﻿﻿﻿Script for creating and broadcasting Legacy transactions
│
├── part2_segwit.py
│﻿﻿﻿﻿Script for creating and broadcasting SegWit transactions
│
├── screenshots/
Inside sits unpacked trades along with logs from the debug tool
│
├── report/
│﻿﻿﻿﻿Detailed assignment report
│
└── README.md
```

---

Tools and Technologies Used

Bitcoin Core bitcoind full node software
Regtest Mode Private Blockchain For Testing
Python 3.x serves as the coding base when building transactions. Its structure supports clear steps in data handling. A version beyond 3 is required here. The system relies on its syntax rules during setup. Scripts written in it manage input flow accurately. Each operation follows defined patterns within this framework
• python-bitcoinlib – Library used to construct and manipulate transactions
• Bitcoin CLI – Interface used to interact with the node
One tool that helps see how scripts run line by line is btcdeb. It walks you through each part of a Bitcoin script as it processes. Watching every move becomes easier when steps unfold one at a time. This debugger shows what happens behind the scenes during validation. Execution details appear clearly so you can follow along closely

---

Environment Setup

Prerequisites

Got everything ready? Check these tools first. A working setup needs each piece in place. Without them, things might break. Installation comes before starting anything else

• Bitcoin Core
• Python 3.x
• python-bitcoinlib
Bitcoin script debugger

A fresh blockchain appears when Bitcoin Core switches to regtest. Blocks form right away, skipping live network rules. Testing happens safely, since no actual coins are needed. This setup runs offline, keeping experiments contained. Real Bitcoin stays untouched throughout.

---

Installation

Install Required Python Dependency

```
pip install python-bitcoinlib
```

---

Running the Project

Run Old Transaction Script

```
python part1_legacy.py
```

This script performs the following steps:

1. connects to the bitcoin node
2. Three legacy addresses created A B C
3. Funds address A
4. Makes a transfer from A to B
5. Creates second transaction using UTXO from B to C
6. Decodes raw transactions to extract script information

---

Enable SegWit Transaction Script

```
python part2_segwit.py
```

This time around, the process follows identical steps - only now it relies on SegWit rather than older address types. The structure stays unchanged, yet the addressing method shifts beneath the surface.

---

Transaction Workflow

The transaction chain implemented in this project is:

```
From Address A Through Address B To Address C
```

A single transaction's result feeds directly into the one that follows. Through this chain, Bitcoin checks each transfer step by step. Scripts handle the verification quietly behind the scenes. What looks like simple movement is actually precise logic at work.

---

Comparative Analysis Using Real Data

From the transactions we pulled off the terminal screen:

Bitcoin Transaction Efficiency Comparison. Legacy P2PKH Versus SegWit P2SH-P2WPKH. On-Chain Data Size And Fee Implications. Wallet Type Impact On Network Usage. Transaction Format Differences In Practice.
|------|------|------|
| Transaction ID | 12cba764... | 41ab2beb... |
Total Size 191 Bytes 215 Bytes
About 191 virtual bytes used in one case. Meanwhile, another situation shows just 134 vBytes taken up.
Weight 764 WU 533 WU

---

Segwit transactions use less space

Though the SegWit transaction took up a bit more space physically, its virtual footprint shrank by a noticeable amount.

A person might get less time because of how the system treats those who speak up. The rules adjust outcomes when someone gives evidence.

Weight calculation rules:

Last time around, old info weighed four units for every single byte. Heavy stuff back then moved slower than air through stone
Every byte seen turns into one unit of weight

Most of the space in a transaction comes from signatures. By shifting those into the witness area, the overall size shrinks noticeably. What once took up room now sits elsewhere, leaving more breathing space behind.

---

Key Benefits Observed

Reduced Transaction Fees

Now here's how it works - miners pick which deals go first by checking satoshis per virtual byte. Because of SegWit, some messages take up less space inside the system. That shrinkage means those trades cost less to push through. What looks bigger isn’t always heavier once you dig into the code.

Transaction Malleability Fix

Changing a signature used to alter the transaction ID in older systems. Because of SegWit, that no longer happens - witness info stays out when computing the TXID.

More Blocks Fit in Less Space

Inside blocks, SegWit deals take up lighter space - so extra transfers can squeeze into one chunk. A smaller footprint means room opens for others tagging along nearby.

Improved Network Scalability

Built into Bitcoin's code, SegWit lifts usable space per block while leaving the hard cap untouched. Instead of raising limits, it reorganizes data behind the scenes. More transactions fit because signatures take up less room. The ceiling stays fixed yet throughput improves anyway.

---

Conclusion

This work shows SegWit’s effect on Bitcoin speed by comparing old-style transfers with updated ones. Efficiency gains appear clearly when earlier methods meet the newer structure. What changes is where signature data lives - split away, it frees up space. Performance shifts happen not through extra power but smarter layout. Transaction size drops because witness info takes a separate path. Results come from real comparisons, not assumptions. The method works by removing clutter instead of adding force. Space saved means more room for activity across the network.

The results show SegWit transactions

• Consume less effective block space
• Require lower transaction fees
• Fix transaction malleability issues
• Improve scalability of the Bitcoin network

Faster transactions come through clearer data paths, thanks to changes packed into SegWit. Its role grows larger when outages strike less often. Performance climbs without extra layers bolted on top. Stability settles in because glitches find fewer cracks to slip through. The Bitcoin network runs smoother simply by cleaning up its internal logic.

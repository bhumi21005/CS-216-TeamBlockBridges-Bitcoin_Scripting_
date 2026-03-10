# CS-216-TeamBlockBridges-Bitcoin_Scripting_

# Bitcoin Transaction Script Analysis 

This project shows how to make, sign, send, and check Bitcoin transactions in a test environment using Bitcoin Core and Python. We wanted to see how Bitcoin Script works and spot the structure changes from old (P2PKH) to new (P2SH-P2WPKH) transactions.

Bitcoin transactions depend on Bitcoin Script, a stack-based script, to decide if a transaction is okay. Each transaction has scripts that set the rules for spending the coins. These scripts have two parts:

*   **Locking Script (scriptPubKey)** – Sets the rules for how the coins can be spent
*   **Unlocking Script (scriptSig / witness)** – Gives the info to meet the locking script rules

When a transaction is checked, both scripts run together. If the script ends with **TRUE**, the transaction is good.

In this project, we make and check both old and new transactions, read the scripts, and look at their sizes and weights to get how SegWit makes Bitcoin better.

***

# Team Members

| Member              | Roll Number |
| :------------------ | :---------- |
| Kumkum Kushwaha     | 240004028   |
| Mhaske Prajwal Sanjay | 240004033   |
| Shruti Turare       | 240008029   |
| Bhumika Kumari      | 240051006   |

***

# Project Goal

We want to get how Bitcoin transactions are made and checked using Bitcoin Script. We also want to see if new style transactions work better than the old ones.

Here's what we wanted to do:

*   Make good old style (P2PKH) transactions
*   Make good new style (P2SH-P2WPKH) transactions
*   Read and check the raw transaction scripts
*   Check script working with a Bitcoin Script tool
*   Measure transaction size and weight
*   See if old or new style ones are better

By doing this, we planned to see how new transactions make things quicker and cheaper on the Bitcoin system.

***

# Background

## Bitcoin Transactions

A Bitcoin transaction moves coins from one address to another. Bitcoin uses a UTXO model, meaning coins aren't kept in accounts but exist as outputs from old transactions.

Each transaction has:

*   **Inputs** – Points to old transaction outputs (UTXOs)
*   **Outputs** – New outputs that say where the coins will go
*   **Scripts** – Programs that set the rules for using outputs

A transaction output is a UTXO until it's used as an input in another transaction.

***

# Bitcoin Script

Bitcoin Script is a stack-based language that checks transactions. It's made to be simple and safe.

Here's how script checking works:

1.  The unlocking script (scriptSig) from the transaction input goes onto the stack.
2.  The locking script (scriptPubKey) from the output is added.
3.  Both scripts run.
4.  If the stack ends up with TRUE, the transaction is okay.

Like this:

```
<signature> <publickey>
OP_DUP OP_HASH160 <pubkeyhash> OP_EQUALVERIFY OP_CHECKSIG
```

This checks that the public key matches the address and the</pubkeyhash></publickey></signature> signature is good.

***

# Transaction Types

## Old Style Transactions (P2PKH)

P2PKH means Pay-to-Public-Key-Hash. It's the old way to do Bitcoin transactions.

Locking Script:

```
OP_DUP OP_HASH160 &lt;pubKeyHash&gt; OP_EQUALVERIFY OP_CHECKSIG
```

Unlocking Script:

```
<signature> <publickey>
```

Checking steps:

1.  Copy public key
2.  Make a hash of the public key
3.  Make sure the hash matches the</publickey></signature> address hash
4.  Make sure the signature is good

If everything is good, the transaction is okay.

***

## New Style Transactions (P2SH-P2WPKH)

Segregated Witness (SegWit) was made to make Bitcoin work better and fix transaction problems.

We used P2SH-P2WPKH, which works with old systems.

Key things:

*   Signature info moved to the witness part
*   Less transaction weight
*   Cheaper transaction costs
*   Fixes transaction problems

Locking script example:

```
OP_HASH160 Hash&gt; OP_EQUAL
```

The witness part has:

```
<signature>
<publickey>
```

***

# Project Files

```
CS-216-TeamBlockBridges-Bitcoin_Scripting_

│
├── part1_legacy.py
│ Script</publickey></signature> for making and sending old style transactions
│
├── part2_segwit.py
│ Script for making and sending new style transactions
│
├── screenshots/
│ Has transaction info and debugging
│
├── report/
│ Assignment report
│
└── README.md
```

***

# Tools Used

*   **Bitcoin Core (bitcoind)** – Complete Bitcoin system
*   **Regtest Mode** – Private test system
*   **Python 3.x** – Language for making transactions
*   **python-bitcoinlib** – Tool for making transactions
*   **Bitcoin CLI** – Tool to talk to the Bitcoin system
*   **btcdeb (Bitcoin Script Debugger)** – Tool to run scripts step by step

***

# Setup

## What You Need

Before you start, make sure you have:

*   Bitcoin Core
*   Python 3.x
*   python-bitcoinlib
*   Bitcoin Script Debugger (btcdeb)

Bitcoin Core must be in regtest mode to test quickly.

***

# How to Install

Install the Python tool:

```
pip install python-bitcoinlib
```

***

# How to Run

## Step 1: Run Old Transaction Script

```
python part1_legacy.py
```

This script:

1.  Connects to the Bitcoin system
2.  Makes three old style addresses (A, B, C)
3.  Sends coins to address A
4.  Makes a transaction from A to B
5.  Uses the coin output to make a new transaction from B to C
6.  Reads the raw transactions

***

## Step 2: Run New Transaction Script

```
python part2_segwit.py
```

This script does the same thing but with new style addresses.

***

# Transaction Steps

The transaction chain is:

```
Address A → Address B → Address C
```

This shows how a transaction output becomes the input of the next transaction.

***

# Comparison (Real Data)

From the terminal:

| Feature             | Old (P2PKH) | New (P2SH-P2WPKH) |
| :------------------ | :---------- | :---------------- |
| Transaction ID      | 12cba764... | 41ab2beb...        |
| Total Size          | 191 Bytes   | 215 Bytes          |
| Size               | 191 vBytes  | 134 vBytes         |
| Weight              | 764 WU      | 533 WU             |

***

# Why New Transactions Are Better

Even though the new transaction was a bit bigger, the size was way smaller.

This is where the Witness Discount comes in.

Weight rules:

Old data → **4 weight units per byte**  
Witness data → **1 weight unit per byte**

Signatures take up a lot of space, so moving them makes the transaction small.

***

# What We Saw

### Cheaper Transactions

Miners charge by size. Since new transactions have smaller sizes, they cost less.

### Transaction Fix

Old transactions could change IDs if the signature changed. New things stop this.

### Better Block Space

New transactions use less block weight, so more can fit in a block.

### Better Network

New transactions help make the system faster.

***

# End

By making and checking old and new transactions, we got how Segregated Witness makes Bitcoin work better.

New transactions:

*   Use less block space
*   Cost less
*   Fix transaction problems
*   Make Bitcoin scale better

These things make SegWit important for Bitcoin.

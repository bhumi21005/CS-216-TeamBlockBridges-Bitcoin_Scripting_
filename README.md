# CS-216-TeamBlockBridges-Bitcoin_Scripting_

# Bitcoin Transaction Script Analysis (Legacy vs SegWit)

This project demonstrates the creation, signing, broadcasting, and validation of Bitcoin transactions within a **Bitcoin regtest environment** using **Bitcoin Core and Python**. The primary purpose of this assignment is to explore the internal working of **Bitcoin Script** and analyze the structural differences between **Legacy (P2PKH)** transactions and **SegWit (P2SH-P2WPKH)** transactions.

Bitcoin transactions rely on a stack-based scripting language known as **Bitcoin Script**, which determines whether a transaction is valid or not. Every transaction contains scripts that define the conditions required to spend the funds. These scripts are divided into two parts:

• **Locking Script (scriptPubKey)** – defines the conditions under which coins can be spent  
• **Unlocking Script (scriptSig / witness)** – provides the data required to satisfy the conditions of the locking script  

When a transaction is verified, the unlocking script and locking script are executed together. If the script execution leaves **TRUE** on the stack, the transaction is considered valid.

In this project we create and analyze both **Legacy and SegWit transactions**, decode the scripts involved, and compare their **transaction sizes, weight units, and virtual sizes** to understand how SegWit improves efficiency in the Bitcoin network.

---

# Team Members

| Member | Roll Number |
|------|------|
| Kumkum Kushwaha | 240004028 |
| Mhaske Prajwal Sanjay | 240004033 |
| Shruti Turare | 240008029 |
| Bhumika Kumari | 240051006 |

---

# Project Objective

The goal of this project is to understand how Bitcoin transactions are constructed and validated using **Bitcoin Script**, and to compare the efficiency between **Legacy and SegWit transactions**.

The project aims to:

• Construct valid **Legacy (P2PKH) transactions**  
• Construct valid **SegWit (P2SH-P2WPKH) transactions**  
• Decode and analyze raw transaction scripts  
• Validate script execution using a Bitcoin Script Debugger  
• Measure transaction **size, weight, and virtual size**  
• Compare the efficiency of Legacy and SegWit transactions  

Through this implementation we demonstrate how SegWit improves transaction efficiency and reduces transaction fees.

---

# Background Concepts

## Bitcoin Transactions

A Bitcoin transaction transfers ownership of coins from one address to another. Bitcoin uses a **UTXO (Unspent Transaction Output) model**, meaning that coins are not stored in accounts but exist as outputs of previous transactions.

Each transaction consists of:

• **Inputs** – references to previous transaction outputs (UTXOs)  
• **Outputs** – new outputs that define where coins will go  
• **Scripts** – programs that define the conditions for spending outputs  

A transaction output becomes a **UTXO** until it is used as an input in another transaction.

---

# Bitcoin Script

Bitcoin Script is a **stack-based programming language** used for validating transactions. It is intentionally limited and not Turing complete in order to ensure security and predictability.

Script execution works as follows:

1. The unlocking script (scriptSig) from the transaction input is pushed onto the stack.
2. The locking script (scriptPubKey) from the referenced output is appended.
3. Both scripts execute sequentially.
4. If the final stack result is TRUE, the transaction is valid.

Example script execution format:

```
<signature> <publicKey>
OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```

This verifies that the public key corresponds to the address and that the signature is valid.

---

# Transaction Types Implemented

## Legacy Transactions (P2PKH)

P2PKH stands for **Pay-to-Public-Key-Hash**, which is the traditional transaction format used in early Bitcoin transactions.

Locking Script:

```
OP_DUP OP_HASH160 <pubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```

Unlocking Script:

```
<signature> <publicKey>
```

Validation steps:

1. Duplicate public key
2. Hash the public key
3. Compare hash with expected address hash
4. Verify digital signature

If all checks pass, the transaction is valid.

---

## SegWit Transactions (P2SH-P2WPKH)

Segregated Witness (SegWit) was introduced to improve Bitcoin scalability and fix transaction malleability.

In this project we implement **P2SH-P2WPKH**, which is a nested SegWit format compatible with legacy systems.

Key features:

• Signature data moved to the **witness field**  
• Reduced **transaction weight**  
• Lower **transaction fees**  
• Fixes **transaction malleability**  

Example locking script:

```
OP_HASH160 <scriptHash> OP_EQUAL
```

The witness section contains:

```
<signature>
<publicKey>
```

---

# Project Structure

```
CS-216-TeamBlockBridges-Bitcoin_Scripting_

│
├── part1_legacy.py
│       Script for creating and broadcasting Legacy transactions
│
├── part2_segwit.py
│       Script for creating and broadcasting SegWit transactions
│
├── screenshots/
│       Contains decoded transactions and debugger outputs
│
├── report/
│       Detailed assignment report
│
└── README.md
```

---

# Tools and Technologies Used

• **Bitcoin Core (bitcoind)** – Full Bitcoin node implementation  
• **Regtest Mode** – Private blockchain used for testing  
• **Python 3.x** – Programming language used for transaction creation  
• **python-bitcoinlib** – Library used to construct and manipulate transactions  
• **Bitcoin CLI** – Interface used to interact with the node  
• **btcdeb (Bitcoin Script Debugger)** – Used to step through script execution  

---

# Environment Setup

## Prerequisites

Before running the project, ensure the following are installed:

• Bitcoin Core  
• Python 3.x  
• python-bitcoinlib  
• Bitcoin Script Debugger (btcdeb)

Bitcoin Core must be running in **regtest mode** to allow instant block generation and testing without using real Bitcoin.

---

# Installation

Install the required Python dependency:

```
pip install python-bitcoinlib
```

---

# Running the Project

## Step 1: Run Legacy Transaction Script

```
python part1_legacy.py
```

This script performs the following steps:

1. Connects to the Bitcoin node
2. Generates three legacy addresses (A, B, C)
3. Funds address A
4. Creates a transaction from A → B
5. Uses the resulting UTXO to create a second transaction from B → C
6. Decodes raw transactions to extract script information

---

## Step 2: Run SegWit Transaction Script

```
python part2_segwit.py
```

This script performs the same workflow but uses **SegWit addresses** instead of legacy addresses.

---

# Transaction Workflow

The transaction chain implemented in this project is:

```
Address A → Address B → Address C
```

This workflow demonstrates how a transaction output becomes the input of the next transaction, allowing us to observe how Bitcoin validates transactions using scripts.

---

# Comparative Analysis (Actual Data)

Based on the decoded transactions from our terminal output:

| Metric | Legacy (P2PKH) | SegWit (P2SH-P2WPKH) |
|------|------|------|
| Transaction ID | 12cba764... | 41ab2beb... |
| Total Size | 191 Bytes | 215 Bytes |
| Virtual Size (vSize) | 191 vBytes | 134 vBytes |
| Weight | 764 WU | 533 WU |

---

# Why SegWit Transactions Are More Efficient

Even though the physical transaction size of the SegWit transaction was slightly larger, the **virtual size was significantly smaller**.

This happens due to the **Witness Discount mechanism**.

Weight calculation rules:

Legacy data → **4 weight units per byte**  
Witness data → **1 weight unit per byte**

Since signatures occupy a large portion of the transaction data, moving them to the witness field greatly reduces the effective transaction size.

---

# Key Benefits Observed

### Reduced Transaction Fees

Miners prioritize transactions based on **satoshis per virtual byte (sat/vB)**. Since SegWit transactions have smaller virtual sizes, they require lower transaction fees.

### Transaction Malleability Fix

In legacy transactions, modifying the signature could change the transaction ID. SegWit prevents this by excluding witness data from the TXID calculation.

### Improved Block Space Efficiency

SegWit transactions occupy less block weight, allowing more transactions to fit within the same block.

### Improved Network Scalability

SegWit increases effective block capacity without increasing the block size limit.

---

# Conclusion

Through the implementation and analysis of Legacy and SegWit transactions, this project demonstrates how Segregated Witness improves transaction efficiency in Bitcoin.

The results confirm that SegWit transactions:

• Consume less effective block space  
• Require lower transaction fees  
• Fix transaction malleability issues  
• Improve scalability of the Bitcoin network  

These improvements make SegWit an essential upgrade that enhances the performance and reliability of the Bitcoin network.

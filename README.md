# CS-216-TeamBlockBridges-Bitcoin_Scripting_
# Bitcoin Transaction Script Analysis (Legacy vs. SegWit)
This project demonstrates the creation, signing, and validation of Bitcoin transactions within a regtest environment. We specifically analyze the differences in Script Execution, Transaction Weight, and Virtual Size (vSize) between Legacy and SegWit formats.

**Team Members:**
* Member 1: Kumkum Kushwaha (Roll No: 240004028)
* Member 2: Mhaske Prajwal Sanjay (Roll No: 240004033)
* Member 3: Shruti Turare (Roll No: 24000)
* Member 4: Bhumika Kumari (Roll No: 24000)


## Objective
To validate the efficiency of Segregated Witness (SegWit) by:
Constructing valid P2PKH (Legacy) transactions.
Constructing P2SH-P2WPKH (Nested SegWit) transactions.
Comparing the vSize and Weight Units (WU) to quantify fee savings and block space optimization.

## How to Run
1.  Ensure `bitcoind` is running in `regtest` mode with the correct `bitcoin.conf` fee settings.
2.  Install the required Python library:
    ```bash
    pip install python-bitcoinlib
    ```
3.  Run the Legacy Transaction script:
    ```bash
    python part1_legacy.py
    ```
4.  Run the SegWit Transaction script:
    ```bash
    python part2_segwit.py
    ```

## Part 3: Comparative Analysis (Actual Data)
Based on the decoded transactions from our terminal, we observed the following:

| Metric | Legacy (P2PKH) | SegWit (P2SH-P2WPKH) |
| :--- | :--- | :--- |
| **Transaction ID** | `12cba764...` | `41ab2beb...` |
| **Total Size** | 191 Bytes | 215 Bytes |
| **Virtual Size (vSize)** | 191 vBytes | 134 vBytes |
| **Weight** | 764 WU | 533 WU |

### Why SegWit is Smaller
Even though the total physical size of our SegWit transaction was larger (215 bytes), the **vSize was ~30% smaller**. This is due to the **Witness Discount**:
* In Legacy, all data is weighted at 4 units per byte.
* In SegWit, the signature (witness) data is moved to a separate field and weighted at only 1 unit per byte.
* **Benefits:** Lower transaction fees, protection against Transaction Malleability, and increased block capacity.

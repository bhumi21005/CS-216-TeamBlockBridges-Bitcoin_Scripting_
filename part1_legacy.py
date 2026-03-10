from bitcoin.rpc import Proxy
from bitcoin.core import CTransaction, CTxIn, CTxOut, COutPoint
from bitcoin.core.script import CScript, OP_DUP, OP_HASH160, OP_EQUALVERIFY, OP_CHECKSIG

# Connect to local bitcoind
proxy = Proxy(service_url="http://youruser:yourpassword@127.0.0.1:18443/wallet/legacy_wallet")

def run_legacy():
    # 1. Generate Addresses
    addr_b = proxy.getnewaddress()
    addr_c = proxy.getnewaddress()
    
    # 2. Fund & Create Transaction Logic
    # (Note: Using Proxy commands to manage keys as per guidance)
    print(f"Legacy Address B: {addr_b}")
    
    # Send from A to B
    txid_ab = proxy.sendtoaddress(addr_b, 10)
    print(f"Transaction A->B TXID: {txid_ab.hex()}")

    # 3. Spend B to C
    unspent = proxy.listunspent(minconf=1, addrs=[str(addr_b)])[0]
    tx_in = CTxIn(unspent['outpoint'])
    tx_out = CTxOut(9.99 * 10**8, proxy.getnewaddress().to_scriptPubKey())
    
    raw_tx = CTransaction([tx_in], [tx_out])
    signed_tx = proxy.signrawtransactionwithwallet(raw_tx)
    
    sent_txid = proxy.sendrawtransaction(signed_tx['tx'])
    print(f"Transaction B->C Success! TXID: {sent_txid.hex()}")

if __name__ == "__main__":
    run_legacy()

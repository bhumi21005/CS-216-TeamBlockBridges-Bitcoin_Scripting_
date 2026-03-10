from bitcoin.rpc import Proxy

# Connect to SegWit wallet
proxy = Proxy(service_url="http://youruser:yourpassword@127.0.0.1:18443/wallet/segwit_wallet")

def run_segwit():
    # 1. Generate P2SH-SegWit Addresses
    addr_b = proxy.getnewaddress(address_type='p2sh-segwit')
    print(f"SegWit Address B': {addr_b}")

    # 2. Fund B'
    txid_ab = proxy.sendtoaddress(addr_b, 10)
    proxy.generate(1) # Mine confirmation

    # 3. Create & Sign SegWit Transaction B' -> C'
    unspent = proxy.listunspent(minconf=1, addrs=[str(addr_b)])[0]
    
    # Logic to spend utilizing Witness data
    inputs = [{'txid': unspent['txid'], 'vout': unspent['vout']}]
    outputs = {proxy.getnewaddress(): 9.99}
    
    raw_tx = proxy.createrawtransaction(inputs, outputs)
    signed_tx = proxy.signrawtransactionwithwallet(raw_tx)
    
    final_txid = proxy.sendrawtransaction(signed_tx['hex'])
    print(f"SegWit Transaction B'->C' Success! TXID: {final_txid}")

if __name__ == "__main__":
    run_segwit()
